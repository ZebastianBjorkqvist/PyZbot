import json
import random
from urllib.request import urlopen
import requests
from discord.ext import commands


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def dog(self, ctx):
        url = "https://dog.ceo/api/breeds/image/random"
        json_response = urlopen(url)
        data = json.loads(json_response.read())

        await ctx.send(data['message'])

    @commands.command()
    async def piggy(self, ctx):
        page = random.randint(1, 10)
        image = random.randint(1, 20)

        url = 'https://pixabay.com/api/'
        params = {'key': '18241563-32b85cbf1a4e1ca5932c8b396', 'q': 'guinea pig', 'per_page': 50, 'page': page}

        r = requests.get(url=url, params=params)
        data = r.json()
        print(data)
        await ctx.send(data['hits'][image]['webformatURL'])