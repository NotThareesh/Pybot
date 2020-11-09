import discord
import os
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix="!", intents=intents)
TOKEN = 'NzczMzgwMDYzNDAzNDQyMTk3.X6IYTw.PZ0W120QywJgAXQVdzPWo5xzRns'


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

# Guild = 773381459306217502
#
# for i in discord.Guild.member_count:
#     print(i)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
