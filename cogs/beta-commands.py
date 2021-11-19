import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class PrivCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot



def setup(bot: commands.bot):
	bot.add_cog(PrivCmd(bot))