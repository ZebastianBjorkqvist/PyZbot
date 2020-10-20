# main.py
import os
from Cogs.RandomCommands import RandomCommands
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
from Cogs.Greetings import Greetings

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(help='Simulates rolling dice. $roll_dice {number of dice} {number of sides}')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.add_cog(Greetings(bot))
bot.add_cog(RandomCommands(bot))

bot.run(TOKEN)
