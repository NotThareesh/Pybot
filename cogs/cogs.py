import discord
from discord.ext import commands, tasks
import random

statuses = ["I'm Busy",
            "PYTHON BOT Server",
            "Not_Thareesh's Stream",
            "Compiling the code",
            "Fortnite",
            "Follow Not_Thareesh on Twitch",
            "!"]


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot_status.start()
        print("Bot is online")
        print(f"Logged in as: {self.client.user}")

    @tasks.loop(seconds=30)
    async def bot_status(self):
        status = random.choice(statuses)
        if status in "I'm Busy":
            await self.client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))

        elif status in "Follow Not_Thareesh on Twitch":
            await self.client.change_presence(activity=discord.Streaming(name=status,
                                                                         url="https://www.twitch.tv/not_thareesh"))

        elif status in ("PYTHON BOT Server", "Not_Thareesh's Stream"):
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                        name=status))

        elif status in "p!":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                        name=status))

        else:
            await self.client.change_presence(activity=discord.Game(name=status))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(773736558259994624)
        await channel.send(f"Welcome {member.mention}! Hope you have a great time in this server!")
        role = discord.utils.get(member.guild.roles, name="Testers")
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(773736558259994624)
        await channel.send(f"{member.mention} left the server!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command(aliases=['lachy'])
    async def pog(self, ctx):
        await ctx.send("POGGIES!")

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

    @commands.command()
    @commands.has_role('Coordinators')
    async def clear(self, ctx, amount: int):
        await ctx.send(f"Tidying up your server")
        await ctx.channel.purge(limit=amount+2)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the amount of messages to delete.")

    @commands.command()
    async def stark(self, ctx):
        await ctx.send("Yeahhh Boii, Its Mr. Stark <:Stark:773581990058131466> ")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason:
            await ctx.send(f"{member.mention} was kicked for {reason}!")
        else:
            await ctx.send(f"{member.mention} was kicked!")

    @commands.command(aliases=['link'])
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f"Here is an instant invite to your server:\n{link}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member.mention} was unbanned")
                return

    @commands.command(aliases=["server", "info"])
    async def server_info(self, ctx):

        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner)
        server_id = str(ctx.guild.id)
        region = str(ctx.guild.region).capitalize()
        icon = str(ctx.guild.icon_url)
        member_count = str(ctx.guild.member_count)
        bot_users = 0
        for i in ctx.guild.members:
            if i.bot:
                bot_users += 1
        text_channels = str(len(ctx.guild.text_channels))
        voice_channels = str(len(ctx.guild.voice_channels))

        embed = discord.Embed(title=name + " Server Information", color=discord.Color.red())

        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Server ID", value=server_id)
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Member Count", value=member_count)
        embed.add_field(name="Bots", value=str(bot_users))
        embed.add_field(name="Text Channels", value=text_channels, inline=False)
        embed.add_field(name="Voice Channels", value=voice_channels)
        embed.set_thumbnail(url=icon)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Commands(client))
