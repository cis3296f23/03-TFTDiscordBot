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
    try:
        component_name_lower = component_name.lower()

        if component_name_lower == 'list':
            items_list = ', '.join(component_images.keys())
            await ctx.send(f"Available components: {items_list}")

        else:
            # Get the image path based on the component name
            image_path = f'imageholder/{component_name_lower}.png'
            if image_path:
                with open(image_path, 'rb') as image_file:
                    file = discord.File(image_file, f'{component_name_lower}.png')
                    await ctx.send(file=file)

    except FileNotFoundError:
        await ctx.send(f"Sorry, the image file for {component_name_lower} was not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

