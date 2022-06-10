# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from Cogs.Greetings import Greetings
from Cogs.RandomCommands import RandomCommands
from Cogs.Pokemon import PokemonCommands

import logging

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    print(f'{bot.user.name} has connected to Discord!')


bot.add_cog(Greetings(bot))
bot.add_cog(RandomCommands(bot))
bot.add_cog(PokemonCommands(bot))
bot.run(TOKEN)
