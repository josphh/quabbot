import discord
from discord_slash import SlashCommand

class MyClient(discord.Client):
    async def on_ready(self):
        print('Ready')

    async def on_message(self, message):
        if not message.author.bot:
            await message.channel.send('No')

client = MyClient()
slash = SlashCommand(client, sync_commands=True)

@slash.slash(name='ping',
            description="Measure the latency of Ribbot's communication with Discord.")
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)}ms)")


client.run('ODY0NTc2NzMwNjc3MTE2OTI4.YO3d0w.l4hX5R6BjtHQBFT_orfdzAqo5Rs')
