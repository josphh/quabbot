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
    description="Measure the latency of Ribbot's communication with Discord.",
)
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)}ms)")


try:
    client.run(os.environ["RIBBOT_TOKEN"])
except KeyError:
    print("Please set the environment variable RIBBOT_TOKEN.", file=sys.stderr)
    sys.exit(2)
