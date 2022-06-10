import json
import os
import random
from urllib.request import urlopen
import requests
from discord.ext import commands


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    async def get_piggie_image(self):
        page = random.randint(1, 10)
        image = random.randint(1, 20)

        url = 'https://pixabay.com/api/'
        params = {'key': os.getenv('PIXABAY_TOKEN'), 'q': 'guinea pig', 'per_page': 50, 'page': page}

        r = requests.get(url=url, params=params)
        data = r.json()

        if len(data['hits']) < 1:
            return await self.get_piggie_image()

        return data['hits'][image]['webformatURL']

    @commands.command()
    async def dog(self, ctx):
        """Sends an almost as beautiful image"""  # Text for !help command
        url = "https://dog.ceo/api/breeds/image/random"
        json_response = urlopen(url)
        data = json.loads(json_response.read())

        await ctx.send(data['message'])

    @commands.command()
    async def piggy(self, ctx):
        """Sends a beautiful image"""  # Text for !help command
        await ctx.send(await self.get_piggie_image())

    @commands.command()
    async def roll_dice(self, ctx, number_of_dice: int, number_of_sides: int):
        """Rolls dice. !roll_dice {number of dice} {number of sides}"""  # Text for !help command
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @commands.command()
    async def guess(self, ctx, number: int):
        """ Guess a random number from 1 to 6. """

        value = random.randint(1, 6)

        emoji = '\N{WHITE HEAVY CHECK MARK}' if value == number else '\N{CROSS MARK}'
        await ctx.message.add_reaction(emoji)
