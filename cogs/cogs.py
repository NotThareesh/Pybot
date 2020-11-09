import discord
from discord.ext import commands
import random
import asyncio


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

        async def change_presence():
            await self.client.wait_until_ready()

            while not self.client.is_closed():
                statuses = ["I'm Busy",
                            "Listening to 'PYTHON BOT' Server",
                            "Listening to Not_Thareesh 魅",
                            "Processing the code",
                            "Fortnite",
                            "I'm being Bullied",
                            "Follow Not_Thareesh on Twitch"]

                status = random.choice(statuses)

                if status == "I'm Busy":
                    await self.client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))

                elif status == "Follow Not_Thareesh on Twitch":
                    await self.client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=status,
                                                                                                            url="https://www.twitch.tv/not_thareesh"))
                else:
                    await self.client.change_presence(status=discord.Status.online, activity=discord.Game(name=status))

                print(f"Bot Status changed to {status}")
                await asyncio.sleep(30)

        self.client.loop.create_task(change_presence())

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(773736558259994624)
        await channel.send(f"Welcome {member.mention}! Hope you have a great time in this server!")

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
    async def clear(self, ctx, amount=7):
        if amount == 1:
            delete_amount = 3
            await ctx.send(f"Tidying up your server")
            await ctx.channel.purge(limit=delete_amount)

        elif amount > 1:
            await ctx.send(f"Tidying up your server")
            await ctx.channel.purge(limit=amount + 2)

    @commands.command()
    async def stark(self, ctx):
        await ctx.send("Yeahhh Boii, Its Mr. Stark <:Stark:773581990058131466> ")

    @commands.command()
    async def kick(self, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason:
            channel = self.client.get_channel(773736558259994624)
            await channel.send(f"{member.mention} was kicked for {reason}!")
        else:
            channel = self.client.get_channel(773736558259994624)
            await channel.send(f"{member.mention} was kicked!")

    @commands.command(aliases=['link'])
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f"Here is an instant invite to your server:\n{link}")

    @commands.command()
    async def ban(self, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def ban(self, member: discord.Member, *, reason=None):
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
