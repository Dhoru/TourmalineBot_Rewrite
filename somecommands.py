import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")


class SomeCommands(commands.Cog):
    """A couple of simple commands. """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", description="Show bot latency")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus", description="Changes the status of the bot", Hidden=True)
    @commands.is_owner()                     
    async def setstatus(self, ctx, *, text: str):
    	await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.command(name="invite", description="Sends the bot invite link")
    async def invite(ctx):
        embed=discord.Embed(title="Invite Link", url="https://discord.com/oauth2/authorize?client_id=749910944951435264&permissions=4294967295&scope=bot")
        embed.colour = 0xFFFFFF 
        
        await ctx.send(embed=embed)


def setup(bot: commands.bot):
    bot.add_cog(SomeCommands(bot))
