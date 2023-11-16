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
    
    
    

bot.run(TOKEN)
