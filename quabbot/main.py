import os
import sys

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
        with open(f"./quabbot/users/{ctx.author.id}.json", "w"):
            await ctx.send("Quib adopted!")


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


def launch():
    try:
        client.run(os.environ["QUABBOT_TOKEN"])
    except KeyError:
        print("Please set the environment variable QUABBOT_TOKEN.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    launch()
