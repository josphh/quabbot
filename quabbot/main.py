import datetime
import os
import random
import sys

import discord
import jsons
from discord_slash import SlashCommand
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option

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
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        await ctx.send("You may not adopt another Quib, as you already have one!")
    else:
        with open(f"./quabbot/users/{ctx.author.id}.json", "w") as file:
            if not name:
                name = generate_name()
            file.write(
                jsons.dumps({"name": name, "timeCreated": datetime.datetime.now()})
            )
            await ctx.send(f"Quib adopted; Their name is {name}!")


@slash.slash(
    name="disown",
    description="Disown your Quib",
)
async def disown(ctx):
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        with open(f"./quabbot/users/{ctx.author.id}.json", "r") as file:
            data = jsons.loads(file.read())
            name = data["name"]
        os.remove(f"./quabbot/users/{ctx.author.id}.json")
        await ctx.send(f"You disowned {name}.")
    else:
        await ctx.send("You may not disown a Quib, as you do not have one!")


@slash.slash(
    name="info",
    description="Find information on your Quib",
)
async def info(ctx):
    if os.path.exists(f"./quabbot/users/{ctx.author.id}.json"):
        with open(f"./quabbot/users/{ctx.author.id}.json", "r") as file:
            data = jsons.loads(file.read())
            name = data["name"]
            embed = discord.Embed(
                title=name, description=data["timeCreated"].strftime("%d/%m/%Y")
            )
            embed.set_image(
                url="https://raw.githubusercontent.com/josphh/quabbot/master/quabbot/resources/quib.png"
            )
            await ctx.send(embed=embed)
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
            required=True,
        )
    ],
)
async def adopt(ctx, name):
    with open(f"./quabbot/users/{ctx.author.id}.json", "r") as file:
        data = jsons.loads(file.read())
    data["name"] = name
    with open(f"./quabbot/users/{ctx.author.id}.json", "w") as file:
            file.write(
                jsons.dumps(data)
            )
    await ctx.send(f"Quib renamed to {name}!")

def launch():
    try:
        client.run(os.environ["QUABBOT_TOKEN"])
    except KeyError:
        print("Please set the environment variable QUABBOT_TOKEN.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    launch()
