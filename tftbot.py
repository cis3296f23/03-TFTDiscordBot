import discord
import requests
import json

from discord.ext import commands
from summoner_info import get_summoner_info

#get bot token and api key from config.json
configJSON = json.load(open('config.json'))

# set bot token and Riot Games API Key
TOKEN = configJSON["BotToken"]
API_KEY = configJSON["APIKey"]


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
async def summoner_command(ctx, name):
    await get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, API_KEY)



bot.run(TOKEN)
