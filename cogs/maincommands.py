import discord
import wikipedia
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

	@commands.command(name="snipe")
	async def snipe(self, ctx: commands.Context):
		if not self.last_msg: 
			await ctx.send("There is no message to snipe!")
			return

		author = self.last_msg.author
		content = self.last_msg.content

		embed = discord.Embed(title=f"Message from {author}", description=content)
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

	@commands.command(name='entode', help='english to german dictionary')
	async def entode(self, ctx: commands.Context, args):
		resultthing = args
		await ctx.send("https://www.dict.cc/?s={resultthing}")

def setup(bot: commands.bot):
	bot.add_cog(MainCommands(bot))