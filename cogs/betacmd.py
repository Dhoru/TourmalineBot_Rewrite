import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class BetaCmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="info", help="Sends the bot info link")
	async def info(self, ctx: commands.Context):
		embed=discord.Embed(title='TourmalineBot', description='''
			__**Bot Info**__

			Owner: 
			<@!473870575081881600> 

			Contributors:
			<@!158556604155822090>

			Github Repository
			[Dhoru/TourmalineBot_Rewrite](https://github.com/Dhoru/TourmalineBot_Rewrite/)

			Discord Server (GOG):
			[Link](https://discord.gg/V6z8BmhZyQ)

			Written in:
			python / [pycord](https://github.com/Pycord-Development/pycord)
				
			'''
			, color=0xff0000)
		embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
		await ctx.send(embed=embed)

def setup(bot: commands.bot):
	bot.add_cog(BetaCmd(bot))