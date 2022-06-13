import random
import requests
from discord.ext import commands
import discord
from matplotlib import colors


async def get_random_flavour_text(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    r = requests.get(url=url)
    species_data = r.json()
    flavor_texts = [_["flavor_text"]
                    for _ in species_data["flavor_text_entries"]
                    if _["language"]["name"] == "en"]

    result = random.choice(flavor_texts)

    # PokeApi returns the flavor texts with random \n in them.
    # They need to be replaced with a space to prevent wierd formatting
    return result.replace('\n', ' ')


class PokemonCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def pokemon_info(self, ctx, arg):
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{arg.lower()}'
        pokemon_r = requests.get(url=pokemon_url)
        pokemon_json = pokemon_r.json()

        pokemon_name = pokemon_json["name"].capitalize()
        pokemon_id = pokemon_json["id"]
        sprite_url = pokemon_json["sprites"]["front_default"]
        pokemon_types = ", ".join(_["type"]["name"].capitalize()
                                  for _ in pokemon_json["types"])

        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
        species_r = requests.get(url=species_url)
        species_json = species_r.json()

        species_color_name = species_json["color"]["name"]

        # Uses matplotlib colors function to_rgba to convert color name to rgba in float values and then times 255
        # and cast to int so discords from_rgb can convert it to a discord.color class
        pokemon_color = discord.colour.Color.from_rgb(r=int(colors.to_rgba(species_color_name)[0] * 255.0),
                                                      g=int(colors.to_rgba(species_color_name)[1] * 255.0),
                                                      b=int(colors.to_rgba(species_color_name)[2] * 255.0))

        embed_var = discord.Embed(title=pokemon_name,
                                  description=await get_random_flavour_text(pokemon_id),
                                  color=pokemon_color)

        embed_var.set_thumbnail(url=sprite_url)

        if ',' in pokemon_types:            # if there is a ',' in pokemon_types there are several types so use "types"
            embed_var.add_field(name="Types",
                                value=pokemon_types,
                                inline=False)
        else:
            embed_var.add_field(name="Type",
                                value=pokemon_types,
                                inline=False)

        await ctx.send(embed=embed_var)
