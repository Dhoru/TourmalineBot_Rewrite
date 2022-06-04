import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="t.")

class mainCommands(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="ping", help="Show bot latency")
	async def ping(self, ctx):
		await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

	@commands.command(name="invite", help="Sends the bot invite link")
	async def invite(self, ctx: commands.Context):
		embed=discord.Embed(title="Invite Link", url="https://discord.com/oauth2/authorize?client_id=749910944951435264&permissions=4294967295&scope=bot")
		embed.colour = 0xFFFFFF 
		
		await ctx.send(embed=embed)

	@commands.command(name="info", help="Sends the bot info")
	async def info(self, ctx: commands.Context):
		embed=discord.Embed(title='TourmalineBot', description='''
			__**Bot Info**__

			Owner: 
			<@!473870575081881600> 

			VERY Helpful Contributor [Current contributions: Renaming a file for me]:
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
	bot.add_cog(mainCommands(bot))