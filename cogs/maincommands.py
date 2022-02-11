import discord
from discord.ext import commands
import pyquran as q
import random
from catfacts import catfacts

bot = commands.Bot(command_prefix="t.")

class MainCommands(commands.Cog):
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

	@commands.command(name='say')
	async def say(self, ctx: commands.Context, *, args):
		am = discord.AllowedMentions(
			users=False,
			everyone=False,
			roles=False,
			replied_user=False,
			)
		await ctx.send(args, allowed_mentions=am)

	@commands.command(name='catfact')
	async def catfact(self, ctx: commands.Context):
		await ctx.send(random.choice(catfacts))

	@commands.command(name='ayat', help='get an ayat')
	async def ayat(self, ctx: commands.Context, sn: int, an: int):
		indexayat = "{sn}:{an}"
		embed=discord.Embed(title=q.quran.get_sura_name(sn), description=q.quran.get_verse(sura_number=sn, verse_number=an, with_tashkeel=True))
		embed.set_footer(text=indexayat.format(sn=sn, an=an))
		embed.color = 0xFFFFFF
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

	@commands.command(name='dictcc', help='english to german dictionary')
	async def dictcc(self, ctx: commands.Context, args):
		resultThing = args
		link = 'https://www.dict.cc/?s={}'
		newLink = link.format(resultThing)
		await ctx.send(newLink)

def setup(bot: commands.bot):
	bot.add_cog(MainCommands(bot))