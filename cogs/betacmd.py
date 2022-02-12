import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class betaCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

'''
	@commands.command(name='say')
	async def say(self, ctx: commands.Context, *, args):
		am = discord.AllowedMentions(
			users=False,
			everyone=False,
			roles=False,
			replied_user=False,
			)
		await ctx.send(args, allowed_mentions=am)
'''

def setup(bot: commands.bot):
	bot.add_cog(betaCmd(bot))