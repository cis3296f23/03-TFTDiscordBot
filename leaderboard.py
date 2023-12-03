import requests
import discord
from discord.ext import commands


async def get_tft_leaderboard(ctx, API_KEY, region):
    
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
    image_path = 'emoji.png'

    try:
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'emoji.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send("The image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
