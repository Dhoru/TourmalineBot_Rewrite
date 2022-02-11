import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class BetaCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def hello(self, ctx: commands.Context):
		await ctx.send('hi')

def setup(bot: commands.bot):
	bot.add_cog(BetaCmd(bot))