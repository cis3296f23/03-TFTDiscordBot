import discord
import requests
import riotwatcher

from config import *
from discord.ext import commands
from summoner_info import get_summoner_info
from riotwatcher import TftWatcher
from items import display_component

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
    
    

@bot.command(name='items', help='Get information on the basic components')
async def display_image(ctx):
    
    folder_path = 'imageholder'

    image_path =  Path(folder_path) /'items.png'

    try:
   
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'items.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send(" the image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

 
 
@bot.command(name='summoner', help='Get summoner information')
async def summoner_command(ctx, name):
    await get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, RIOT_GAMES_API_KEY)




@bot.command(name='component', help='Get information on a specific component')
async def component_commands(ctx, component_name: str):
    await display_component(ctx, component_name)
 










bot.run(BOT_TOKEN)
