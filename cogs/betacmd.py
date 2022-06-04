from discord import slash_command
from discord.ext import commands


class betaCmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@slash_command(name = 'hello', description = 'hello cmd', guild_ids=[725560468558839851])
	async def hello(self, ctx):
		await ctx.respond("Hi, this is a slash command from a cog!")

	@slash_command()
	async def slashtest(self, ctx):
		await ctx.respond("response")

def setup(bot: commands.bot):
	bot.add_cog(betaCmd(bot))