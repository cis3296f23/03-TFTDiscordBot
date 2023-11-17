import discord
import requests

from discord.ext import commands





# Prompt the user to enter the token
import discord
from discord.ext import commands

# Prompt the user to enter the token
TOKEN = input("Enter your Discord bot token: ")

#api key
API_KEY = "RGAPI-93f45e9a-2a32-4b4d-8b2e-411239b2875d" 


#summoner url for information

summoner_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name"
rank_url = "https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner"
icon_url = "http://ddragon.leagueoflegends.com/cdn/11.18.1/img/profileicon/"



# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True

# Pass the intents parameter to the Bot constructor
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hi', help='Bot says hi')
async def say_hi(ctx):
    await ctx.send('Hi')
    
    
 
@bot.command(name='summoner', help='Get summoner information')
async def get_summoner(ctx, name):
    try:
        
   


        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Fetch data
        player_info = resp.json()
        summoner_level = player_info["summonerLevel"]
        puuid = player_info['puuid']
        profile_icon = player_info['profileIconId']

       #Get Icon 
        
        icon = f"{icon_url}{profile_icon}.png"


        # Rank information using summoner ID
        get_rank = f"{rank_url}/{player_info['id']}?api_key={API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Fetch TFT data
        rank_info = rank_resp.json()
        if rank_info:
            tft_rank = f"TFT Rank: {rank_info[0]['tier']} {rank_info[0]['rank']}"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"Summoner level: {summoner_level}\nSummoner PUUID: {puuid}\n{tft_rank}\nProfile Icon: {icon}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching summoner information: {err}")
        


bot.run(TOKEN)
