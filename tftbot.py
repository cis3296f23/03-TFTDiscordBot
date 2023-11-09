
import os
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)

@bot.command(name='hi', help='Bot says hi')
async def say_hi(ctx):
    await ctx.send('Hi')

bot.run('ODM0OTY2NDU0NDczNzE5ODM4.GuxXin.gEaNLog5Nl-519jTdV_7tLUxr-qsBNSjeOZJlM')

