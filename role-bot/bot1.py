# bot.py
import os
import random
import csv
import time

from dotenv import load_dotenv

# 1
from discord.ext import commands
from discord import File

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
	
@bot.command(name='roll_dice', help='Simulates rolling dice.')
@commands.has_role('Server Admin')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
	
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.command(name='mw_members', help='Simulates rolling dice.')		
async def stat(ctx):
    """Returns a CSV file of all users on the server."""
    await bot.request_offline_members(ctx.message.guild)
    before = time.time()
    nicknames = [m.display_name for m in ctx.message.guild.members]
    with open('temp.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for v in nicknames:
            writer.writerow([v])
    after = time.time()
    await ctx.send(file=File('temp.csv'))
	
bot.run(token)