# summoner_command.py

import requests
import discord
from discord.ext import commands


async def get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, matches_url, RIOT_GAMES_API_KEY):
    """Used to find a particular summoner

    Args:
        ctx (Any): User input directly after slash character
        name (Any): Name of the summoner
        summoner_url (Any): URL for this particular player's profile
        rank_url (Any): URL for this particular player's rank
        icon_url (Any): URL for this particular players Icon
        matches_url (Any): URL for this particular player's match history
        RIOT_GAMES_API_KEY (Any): The Riot Games API key
    """    
    try:
        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={RIOT_GAMES_API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Fetch data
        player_info = resp.json()
        summoner_level = player_info["summonerLevel"]
        puuid = player_info['puuid']
        profile_icon = player_info['profileIconId']

        # Get Icon 
        icon = f"{icon_url}{profile_icon}.png"

        # Rank information using summoner ID
        get_rank = f"{rank_url}/{player_info['id']}?api_key={RIOT_GAMES_API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Matches history info
        get_matches = f"{matches_url}{puuid}/ids?start=0&count=20&api_key={RIOT_GAMES_API_KEY}"
        matches_resp = requests.get(get_matches)
        matches = matches_resp.json()
        

        # Fetch TFT data
        rank_info = rank_resp.json()
        if rank_info:
            tft_rank = f"TFT Rank: {rank_info[0]['tier']} {rank_info[0]['rank']}"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"Summoner level: {summoner_level}\nSummoner PUUID: {puuid}\n{tft_rank}\nMatch history: {matches}\nProfile Icon: {icon}\n ")
        


    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching summoner information: {err}")


async def get_match_info(ctx, name, specific_match_url, RIOT_GAMES_API_KEY):
    """Used to retrieve information on a specific match

    Args:
        ctx (Any): User input directly after slash character
        name (Any): Name of the summoner
        specific_match_url (Any): URL for this particular player's match
        RIOT_GAMES_API_KEY (Any): The Riot Games API key
    """    
    try:
        match_id = name
        get_match = f"{specific_match_url}{match_id}/?api_key={RIOT_GAMES_API_KEY}"
        match_resp = requests.get(get_match)
        match = match_resp.json()
        game_length_seconds = match['info']['game_length']
        
        # Time Caculate 
        minutes = int(game_length_seconds // 60)
        seconds = int(game_length_seconds % 60)

        await ctx.send(f"Game length: {minutes} minutes and {seconds} seconds")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching match information: {err}")


async def get_tft_leaderboard(ctx, API_KEY, region):
    """Used to retrieve the leaderboard for a given region

    Args:
        ctx (Any): User input directly after slash character
        API_KEY (Any): the Riot Games API key
        region (Any): The region in which to search for the leaderboard

    Returns:
        Any: The string to change the region for the leaderboard
    """    
    base_url = f"https://{region}.api.riotgames.com/tft/league/v1/challenger"
    leaderboard_api_url = f"{base_url}?api_key={API_KEY}&region={region}"


    try:
        # Fetch TFT leaderboard information 
        leaderboard_resp = requests.get(leaderboard_api_url)
        leaderboard_resp.raise_for_status()

        leaderboard_info = leaderboard_resp.json()

        top_10_entries = leaderboard_info['entries'][:10]

        # fix the display as its shown as I instead of Challenger, Gramaster etc so I need an def get_rank
            
        def get_rank(rank):
            ranks = {'I': 'Challenger', 'II': 'Grandmaster', 'III': 'Master'}
            return ranks.get(rank, rank)

        leaderboard_text = f"Top Challenger TFT Players in {region}:\n"
        for index, entry in enumerate(top_10_entries, start=1):
            
            summoner_name = entry['summonerName']
            league_points = entry['leaguePoints']
            wins = entry['wins']
            losses = entry['losses']
            rank = get_rank(entry['rank'])

            player_info = f"{index}. {summoner_name} ({rank}) - LP: {league_points} | Wins: {wins} | Losses: {losses}\n"
            leaderboard_text += player_info

      
        message = await ctx.send(f"{leaderboard_text}\n\u200B")
        
        # Region managing 
        
        # Europe
        await message.add_reaction("😁")   
        # Brazil 
        await message.add_reaction("😄") 
        #North America
        await message.add_reaction("🚀")   
        #Latin America North (LAN)
        await message.add_reaction("💻")   
        #Oceania (OCE)
        await message.add_reaction("📚")   
        #Korea (KR) 
        await message.add_reaction("🎉")   
        #Japan (JP)
        await message.add_reaction("🌟")   
        

        def check(reaction, user):
            """Checks when an emoji on the leaderboard output message is clicked on

            Args:
                reaction (String): the emoji clicked on
                user (Any): The sender of the emoji

            Returns:
                Any: The string to change the region for the leaderboard
            """            
            valid_emojis = {"😁", "🚀", "😄", "💻", "📚", "🎉", "🌟"}
            return (
                user == ctx.author
                and str(reaction.emoji) in valid_emojis
                and reaction.message.id == message.id
)

        reaction, _ = await ctx.bot.wait_for("reaction_add", check=check, timeout=60)

        if str(reaction.emoji) == "😁":
            await message.add_reaction("😁")
            await get_tft_leaderboard(ctx, API_KEY, "euw1")
        elif str(reaction.emoji) == "😄":
            await message.add_reaction("😄")
            await get_tft_leaderboard(ctx, API_KEY, "br1")


        elif str(reaction.emoji) == "🚀":
            await message.add_reaction("🚀")
            await get_tft_leaderboard(ctx, API_KEY, "na1")
            
            
        elif str(reaction.emoji) == "💻":
            await message.add_reaction("💻")
            await get_tft_leaderboard(ctx, API_KEY, "la1")
            
        elif str(reaction.emoji) == "📚":
            await message.add_reaction("📚")
            await get_tft_leaderboard(ctx, API_KEY, "oc1")
    
        elif str(reaction.emoji) == "🎉":
            await message.add_reaction("🎉")
            await get_tft_leaderboard(ctx, API_KEY, "kr")
            
        elif str(reaction.emoji) == "🌟":
            await message.add_reaction("🌟")
            await get_tft_leaderboard(ctx, API_KEY, "jp1")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        

async def get_emoji(ctx):
    """Finds given emoji

    Args:
        ctx (Any): The clicked emoji
    """    
    image_path = 'emoji.png'

    try:
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'emoji.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send("The image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        

async def rank_info(ctx, name, summoner_url, rank_url, RIOT_GAMES_API_KEY):
    """Retrieves rank information for a given summoner

    Args:
        ctx (Any): User input directly after slash character
        name (Any): Name of the summoner
        summoner_url (Any): URL for the particular summoner's profile
        rank_url (Any): URL for the particular sumoner's official rank
        RIOT_GAMES_API_KEY (Any): The Riot Games API key
    """    
    try:
        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={RIOT_GAMES_API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Get Summoner Information 
        summoner_info = resp.json()
        summoner_id = summoner_info['id']

        # Rank information using summoner ID
        get_rank = f"{rank_url}/{summoner_id}?api_key={RIOT_GAMES_API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Fetch TFT data
        rank_info = rank_resp.json()

        if rank_info:
            tier = rank_info[0]['tier']
            rank = rank_info[0]['rank']
            tft_rank = f"TFT Rank: {tier} {rank}"

            # Display rank_image
            image_filename = f"rank_image/{tier.lower()}.png"
            with open(image_filename, 'rb') as f:
                await ctx.send(file=discord.File(f, 'rank_image.png'))

            # WinRate 
            if 'wins' in rank_info[0] and 'losses' in rank_info[0]:
                wins = rank_info[0]['wins']
                losses = rank_info[0]['losses']
                winrate = (wins / (wins + losses)) * 100
                tft_rank += f"\nWins: {wins}, Lost: {losses}, Winrate: {winrate:.2f}%"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"{tft_rank}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching match information: {err}")
