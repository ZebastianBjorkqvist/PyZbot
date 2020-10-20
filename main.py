# main.py
import os
from discord.ext import commands
from dotenv import load_dotenv
from Cogs.Greetings import Greetings
from Cogs.RandomCommands import RandomCommands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.add_cog(Greetings(bot))
bot.add_cog(RandomCommands(bot))

bot.run(TOKEN)
