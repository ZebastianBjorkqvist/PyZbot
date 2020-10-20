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

    async def get_piggie_image(self):  # We need to have this in a separate function so we can call it if the hits in
        # the request is empty. Seems to happen approx 1 in 10 times
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
        url = "https://dog.ceo/api/breeds/image/random"
        json_response = urlopen(url)
        data = json.loads(json_response.read())

        await ctx.send(data['message'])

    @commands.command()
    async def piggy(self, ctx):
        await ctx.send(await self.get_piggie_image())
