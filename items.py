import discord
from discord.ext import commands

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

async def display_component(ctx, component_name: str):
    """Retrieves the build path for a given item

    Args:
        ctx (Any): User input directly after slash character
        component_name (str): Name of item which user wants a build path for
    """    
    if component_name.lower() == 'list':
        items_list = ', '.join(component_images.keys())
        await ctx.send(f"Available components: {items_list}")
    
        
    try:
        # Get the image path based on the component name
        image_path = f'imageholder/{component_name.lower()}.png'
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
        
    
async def display_drop(ctx):
    """Retrieves image for the drop rate chart

    Args:
        ctx (Any): User input directly after slash character
    """    
    image_path =  'drop.png'

    try:
   
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'drop.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send(" the image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        
        
async def display_image(ctx):
    """Output image file to the text chat

    Args:
        ctx (Any): User input directly after slash character
    """    
    image_path =  'items.png'

    try:
   
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, 'items.png')
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send(" the image file was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
