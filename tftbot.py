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
    
    

@bot.command(name='items', help='Get information on the basic components')
async def display_image(ctx):
    image_path = 'items.png'

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
async def display_component(ctx, component_name: str):
    component_images = {
        'tears': 'tears.png',
        'spatula': 'spatula.png',
        'gloves': 'gloves.png',
        'belt': 'belt.png',
        'cloak': 'cloak.png',
        'rod': 'rod.png',
        'bow': 'bow.png',
        'sword': 'sword.png',
    }

    try:
        # Get the image path based on the component name
        image_path = component_images.get(component_name.lower())
        if image_path:
            with open(image_path, 'rb') as image_file:
                file = discord.File(image_file, f'{component_name}.png')
                await ctx.send(file=file)
        else:
            await ctx.send(f"Sorry, no information available for {component_name}.")
    except FileNotFoundError:
        await ctx.send(f"Sorry, the image file for {component_name} was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")












bot.run(BOT_TOKEN)
