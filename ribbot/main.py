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


client.run("RIBBOT_TOKEN")
