import discord
from discord.ext import commands
from catfacts import catfacts
import pyquran as q

bot = commands.Bot(command_prefix = 't.')

class miscCommands(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name='catfact')
	async def catfact(self, ctx: commands.Context):
		await ctx.send(random.choice(catfacts))

	@commands.command(name='say')
	async def say(self, ctx: commands.Context, *, args):
		am = discord.AllowedMentions(
			users=False,
			everyone=False,
			roles=False,
			replied_user=False,
			)
		await ctx.send(args, allowed_mentions=am)

	@commands.command(name='dictcc', help='english to german dictionary')
	async def dictcc(self, ctx: commands.Context, args):
		resultThing = args
		link = 'https://www.dict.cc/?s={}'
		newLink = link.format(resultThing)
		await ctx.send(newLink)

	@commands.command(name='ayat', help='get an ayat')
	async def ayat(self, ctx: commands.Context, sn: int, an: int):
		indexayat = "{sn}:{an}"
		embed=discord.Embed(title=q.quran.get_sura_name(sn), description=q.quran.get_verse(sura_number=sn, verse_number=an, with_tashkeel=True))
		embed.set_footer(text=indexayat.format(sn=sn, an=an))
		embed.color = 0xFFFFFF
		await ctx.send(embed=embed)

def setup(bot: commands.bot):
	bot.add_cog(miscCommands(bot))