import discord
import wikipedia
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")


class SomeCommands(commands.Cog):

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="ping", help="Show bot latency")
	async def ping(self, ctx):
		await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

	@commands.command(name="setstatus", help="Changes the status of the bot", Hidden=True)
	@commands.is_owner()
	async def setstatus(self, ctx, *, text: str):
		await self.bot.change_presence(activity=discord.Game(name=text))

	@commands.command(name="invite", help="Sends the bot invite link")
	async def invite(ctx):
		embed=discord.Embed(title="Invite Link", url="https://discord.com/oauth2/authorize?client_id=749910944951435264&permissions=4294967295&scope=bot")
		embed.colour = 0xFFFFFF 
		
		await ctx.send(embed=embed)

	@commands.command(name="snipe")
	async def snipe(self, ctx: commands.Context):
		if not self.last_msg: 
			await ctx.send("There is no message to snipe!")
			return

		author = self.last_msg.author
		content = self.last_msg.content

		embed = discord.Embed(title=f"Message from {author}", description=content)
		await ctx.send(embed=embed)

	@commands.command(name="dontpingme")
	async def dont_ping_me(self, ctx: commands.Context):
		am = discord.AllowedMentions(
			users=False,
		)
		await ctx.send(f"Hello, {ctx.author.mention}", allowed_mentions=am)

	@commands.command(name='say')
	async def say(self, ctx: commands.Context, *, args):
		am = discord.AllowedMentions(
			users=False,  # Whether to ping individual user @mentions
			everyone=False,  # Whether to ping @everyone or @here mentions
			roles=False,  # Whether to ping role @mentions
			replied_user=False,  # Whether to ping on replies to messages
			)
		await ctx.send(args, allowed_mentions=am)

def setup(bot: commands.bot):
	bot.add_cog(SomeCommands(bot))
