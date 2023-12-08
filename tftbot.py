import discord

from config import *
from discord.ext import commands
from summoner_info import *
from items import *
    
"""This class handles starting up the bot and all of the commands a user can use

Variables:
    summoner_url {string} -- URL used for finding a given summoner
    rank_url {string} -- URL used for finding the rank of a given summoner
    icon_url {string} -- URL used for finding the icon a given summoner
    matches_url {string} -- URL used for finding the match history a given summoner
    specific_match_url {string} -- URL used for finding details of a specific match
    
    intents {Intents} -- creates an instance of a Discord Intents object to enable the bot functionality
    bot {Bot} -- the bot object which you run commands through
"""

#summoner url for information
summoner_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name"
rank_url = "https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner"
icon_url = "http://ddragon.leagueoflegends.com/cdn/11.18.1/img/profileicon/"
leaderboard_url = "https://na1.api.riotgames.com/tft/league/v1/challenger"



# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True

# Pass the intents parameter to the Bot constructor
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    """Used for letting the developer know the bot is active
    
    Returns:
        a message to the console saying it's ready
    """    
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hi', help='Bot says hi')
async def say_hi(ctx):
    """Makes the bot say "hi" in the text chat

    Args:
        ctx (Any): User input directly after slash character
    """    
    await ctx.send('Hi')
    
  
@bot.command(name='items', help='Get information on the basic components')
async def item_command(ctx):
    """Returns pictures with detailed descriptions of all tier 1 items

    Args:
        ctx (Any): User input directly after slash character
    """    
    await display_image(ctx)

    
@bot.command(name='summoner', help='Get summoner information')
async def summoner_command(ctx, name):
    """Outputs the given summoner level, PUUID, TFT Rank and the game codes for the last 20 TFT games they played

    Args:
        ctx (Any): User input directly after slash character
        name (Ayn): name of the summoner the user wants to find
    """    
    await get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, matches_url, RIOT_GAMES_API_KEY)

@bot.command(name='match', help='Get match information')
async def match_command(ctx, name):
    """Outputs statistics of a given game

    Args:
        ctx (Any): User input directly after slash character
        name (Any): Unique match id
    """    
    await get_match_info(ctx, name, specific_match_url, RIOT_GAMES_API_KEY)



@bot.command(name='component', help='Get information on a specific component')
async def component_commands(ctx, component_name: str):
    """Outputs a picture of every possible build path for a given item

    Args:
        ctx (Any): User input directly after slash character
        component_name (str): Name of item
    """    
    await display_component(ctx, component_name)
 

@bot.command(name='droprates', help='Get the dropRate of every tier in every level')
async def drop_command(ctx):
    """Outputs chart of drop rates for champions at particular levels

    Args:
        ctx (Any): User input directly after slash character
    """    
    await display_drop(ctx)


@bot.command(name='leaderboard' , help= 'Get the top ranking players information')
async def tft_leaderboard(ctx):
    await get_tft_leaderboard(ctx, leaderboard_url, API_KEY)






bot.run(BOT_TOKEN)