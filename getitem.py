import discord
from discord.ext import commands

async def display_image(ctx):
    
    image_path =  'items.png'

    try:
   
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'items.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send(" the image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")