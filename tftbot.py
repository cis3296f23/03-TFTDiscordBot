import discord
import requests
import riotwatcher

from config import *
from discord.ext import commands
from summoner_info import get_summoner_info
from riotwatcher import TftWatcher

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
    await get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, RIOT_GAMES_API_KEY)


#display items

@bot.command(name='items', help = 'get information on the basic item components')
async def display_image(ctx):
    image_url = 'items.png'

    # Create and send an embed with the image
    embed = discord.Embed()
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)














bot.run(BOT_TOKEN)
