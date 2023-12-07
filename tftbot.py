import discord

from config import *
from discord.ext import commands
from summoner_info import *
from items import *

#summoner url for information
summoner_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name"
rank_url = "https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner"
icon_url = "http://ddragon.leagueoflegends.com/cdn/11.18.1/img/profileicon/"
matches_url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"
specific_match_url = "https://americas.api.riotgames.com/tft/match/v1/matches/"


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
async def item_command(ctx):
    await display_image(ctx)

    
@bot.command(name='summoner', help='Get summoner information')
async def summoner_command(ctx, name):
    await get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, matches_url, RIOT_GAMES_API_KEY)

@bot.command(name='match', help='Get match information')
async def match_command(ctx, name):
    await get_match_info(ctx, name, specific_match_url, RIOT_GAMES_API_KEY)



@bot.command(name='component', help='Get information on a specific component')
async def component_commands(ctx, component_name: str):
    await display_component(ctx, component_name)
 

@bot.command(name='droprates', help='Get the dropRate of every tier in every level')
async def drop_command(ctx):
    await display_drop(ctx)


@bot.command(name='leaderboard' , help= 'Get the top ranking players information')
async def tft_leaderboard(ctx):
    await get_emoji(ctx)
    await get_tft_leaderboard(ctx, RIOT_GAMES_API_KEY , "na1")



@bot.command(name='rank', help= 'Get the TFT rank of the player with Winrate')
async def rank_command(ctx, name):
    await rank_info(ctx, name,summoner_url, rank_url, RIOT_GAMES_API_KEY)


bot.run(BOT_TOKEN)