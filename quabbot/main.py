import os
import sys

import discord
from discord_slash import SlashCommand


class MyClient(discord.Client):
    async def on_ready(self):
        print("Ready")


client = MyClient()
slash = SlashCommand(client, sync_commands=True)


@slash.slash(
    name="ping",
    description="Measure the latency of Quabbot's communication with Discord.",
)
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)}ms)")


def launch():
    try:
        client.run(os.environ["QUABBOT_TOKEN"])
    except KeyError:
        print("Please set the environment variable RIBBOT_TOKEN.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    launch()