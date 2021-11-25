import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class BetaCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name='entode', help='english to german dictionary')
	async def entode(self, ctx: commands.Context, args):
		resultthing = args
		await ctx.send("https://www.dict.cc/?s={resultthing}")

def setup(bot: commands.bot):
	bot.add_cog(BetaCmd(bot))