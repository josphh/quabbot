import datetime
import os
import random
import sys

import discord
from discord_slash import SlashCommand
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option

from quabbot import __version__
from quabbot.quib import generate_quib
from quabbot.user_data import (
    delete_user_files,
    get_user_file,
    has_user_data,
    load_user_data,
    save_user_data,
)


class MyClient(discord.Client):
    async def on_ready(self):
        print("Ready")


activity = discord.Game(name=f"v{__version__}")
client = MyClient(activity=activity)
slash = SlashCommand(client, sync_commands=True)

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"


def generate_name():
    name = ""
    for _ in range(random.randint(2, 5)):
        name += random.choice(CONSONANTS)
        name += random.choice(VOWELS)
    return name.title()


@slash.slash(
    name="ping",
    description="Measure the latency of Quabbot's communication with Discord.",
)
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)}ms)")


@slash.slash(
    name="adopt",
    description="Adopt a Quib",
    options=[
        create_option(
            name="name",
            description="Choose a custom name for your Quib.",
            option_type=SlashCommandOptionType.STRING,
            required=False,
        )
    ],
)
async def adopt(ctx, name=None):
    if has_user_data(ctx.author):
        await ctx.send("You may not adopt another Quib, as you already have one!")
    else:
        await ctx.defer()
        if not name:
            name = generate_name()
        save_user_data(
            ctx.author,
            {"originName": name, "name": name, "timeCreated": datetime.datetime.now()},
        )
        generate_quib(ctx.author)
        await ctx.send(f"Quib adopted; Their name is {name}!")


@slash.slash(
    name="disown",
    description="Disown your Quib",
)
async def disown(ctx):
    if has_user_data(ctx.author):
        data = load_user_data(ctx.author)
        name = data["name"]
        delete_user_files(ctx.author)
        await ctx.send(f"You disowned {name}.")
    else:
        await ctx.send("You may not disown a Quib, as you do not have one!")


@slash.slash(
    name="info",
    description="Find information on your Quib",
)
async def info(ctx):
    if has_user_data(ctx.author):
        data = load_user_data(ctx.author)
        name = data["name"]
        embed = discord.Embed(
            title=name, description=data["timeCreated"].strftime("%d/%m/%Y")
        )
        await ctx.send(
            embed=embed, file=discord.File(get_user_file(ctx.author, "quib.png"))
        )
    else:
        await ctx.send("You may not find info on your Quib, as you do not have one!")


@slash.slash(
    name="rename",
    description="Rename your Quib",
    options=[
        create_option(
            name="name",
            description="Choose a custom name for your Quib.",
            option_type=SlashCommandOptionType.STRING,
            required=False,
        )
    ],
)
async def rename(ctx, name=None):
    data = load_user_data(ctx.author)
    if not name:
        name = generate_name()
    data["name"] = name
    save_user_data(ctx.author, data)
    await ctx.send(f"Quib renamed to {name}!")


@slash.slash(
    name="originalname",
    description="Rename your Quib to its Original name",
)
async def original_name(ctx):
    data = load_user_data(ctx.author)
    data["name"] = data["originName"]
    save_user_data(ctx.author, data)
    name = data["name"]
    await ctx.send(f"Quib renamed to {name}!")


def launch():
    try:
        client.run(os.environ["QUABBOT_TOKEN"])
    except KeyError:
        print("Please set the environment variable QUABBOT_TOKEN.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    launch()
