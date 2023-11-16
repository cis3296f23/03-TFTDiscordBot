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
    api_url = f"{api_summoner_url}/{name}?api_key={API_KEY}"

    try:
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        player_info = resp.json()
        summoner_level = player_info["summonerLevel"]
        puuid = player_info['puuid']

        await ctx.send(f"Summoner level: {summoner_level}\nSummoner puuid: {puuid}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching summoner information: {err}")
        
        
        


bot.run(TOKEN)
