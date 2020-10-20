# main.py
import os
import Cogs
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.add_cog(Cogs.Greetings(bot))
bot.add_cog(Cogs.RandomCommands(bot))

bot.run(TOKEN)
