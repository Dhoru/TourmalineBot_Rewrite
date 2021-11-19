import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class BetaCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="invite", help="Sends the bot invite link")
	async def invite(self, ctx: commands.Context):
		embed=discord.Embed(title='TourmalineBot', description='''
				**Categories:**

				Do `t.help <category>` for more information on a category.

				**Categories:**

				`main`
				`owner` (<@!473870575081881600> only)
				`listeners`
				`misc`

				
				'''
				, color=0xff0000)
		embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
		await ctx.send(embed=embed)

def setup(bot: commands.bot):
	bot.add_cog(BetaCmd(bot))