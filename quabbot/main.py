import json
import os
import random
import sys
import datetime

import discord
from discord_slash import SlashCommand

from quabbot import __version__


class MyClient(discord.Client):
    async def on_ready(self):
        print("Ready")


os.makedirs("./quabbot/users", exist_ok=True)

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
)
async def adopt(ctx):
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        await ctx.send("You may not adopt another Quib, as you already have one!")
    else:
        with open(f"./quabbot/users/{ctx.author.id}.json", "w") as file:
            name = generate_name()
            jsons.dump({"name": name}, file)
            await ctx.send(f"Quib adopted; Their name is {name}!")


@slash.slash(
    name="disown",
    description="Disown your Quib",
)
async def disown(ctx):
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        os.remove(f"./quabbot/users/{ctx.author.id}.json")
        await ctx.send("Quib disowned.")
    else:
        await ctx.send("You may not disown a Quib, as you do not have one!")

@slash.slash(
    name="info",
    description="Find informmation on your Quib",
)
async def info(ctx):
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        with open(f"./quabbot/users/{ctx.author.id}.json", "r") as file:
            data = json.load(file)
            name = data["name"]
            embed = discord.Embed(title = name, description = 'stuff')
            embed.set_image(url='https://raw.githubusercontent.com/josphh/quabbot/master/quabbot/resources/quib.png')
            await ctx.send(embed=embed)
    else:
        await ctx.send("You may not find info on your Quib, as you do not have one!")


def launch():
    try:
        client.run(os.environ["QUABBOT_TOKEN"])
    except KeyError:
        print("Please set the environment variable QUABBOT_TOKEN.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    launch()
