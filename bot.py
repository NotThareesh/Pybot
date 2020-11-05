import random
import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix="!", intents=intents)
TOKEN = 'NzczMzgwMDYzNDAzNDQyMTk3.X6IYTw.Ilq2nU0oIjH-HnVM5jZjRFqW_k8'


@client.event
async def on_ready():
    print("PYTHON BOT IS ONLINE!")


@client.event
async def on_member_join(member):
    channel = client.get_channel(773736558259994624)
    await channel.send(f"Welcome {member.mention}! Hope you have a great time in this server!")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(773736558259994624)
    await channel.send(f"{member.mention} left the server!")


@client.command(aliases=['lachy'])
async def pog(ctx):
    await ctx.send(f"POGGERS!!")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command()
async def clear(ctx, amount=7):
    if amount == 1:
        delete_amount = 3
        await ctx.send(f"Tidying up your server")
        await ctx.channel.purge(limit=delete_amount)

    elif amount > 1:
        await ctx.send(f"Tidying up your server")
        await ctx.channel.purge(limit=amount+2)


@client.command()
async def latency(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")


@client.command()
async def commands(ctx):
    await ctx.send(
        """All commands have '!' as the prefix \n
        pog: POGGERS!!\n 
        latency: Displays the latency of the bot.\n 
        clear: Deletes the messages in the channel. (Default: 5)\n 
        8ball: Asks your question to Magic 8Ball.\n
        stark: Displays a fancy message."""
    )


@client.command()
async def stark(ctx):
    await ctx.send("Yeahhh Boii, Its Mr. Stark <:Stark:773581990058131466> ")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    if reason:
        channel = client.get_channel(773736558259994624)
        await channel.send(f"{member.mention} was kicked for {reason}!")
    else:
        channel = client.get_channel(773736558259994624)
        await channel.send(f"{member.mention} was kicked!")


@client.command()
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age=300)
    await ctx.send(f"Here is an instant invite to your server:\n{link}")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member.mention} was unbanned")
            return

client.run(TOKEN)
