import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t.')

bot.remove_command('help')

class helpme(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx: commands.Context, args=None):
		if args == None:
			embed=discord.Embed(title='TourmalineBot', description='''
				**Categories:**

				Do `t.help <category>` for more information on a category.

				**Categories:**

				`main`
				`owner` (<@!473870575081881600> only)
				`listeners`
				'''
				, color=0xff0000)
			embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
			await ctx.send(embed=embed)

		elif args == 'main':
			embed = discord.Embed(title="Main Commands", description="""
				`t.help <optional category>`
					> Shows this

				`t.ayat <surah number> <ayat number>`
					> Get an ayat from quran

				`t.say <args>`
					> Make the bot say something you want

				`t.snipe`
					> Sends the last sent message in a channel (coming soon)

				`t.invite`
					> Sends bot invite link

				`t.ping` 
					> Checks bot latency
				""")
			embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
			embed.colour = 0xFF0000
			await ctx.send(embed=embed)

		elif args == 'owner':
			embed=discord.Embed(title="Owner Only Commands", description="""
				`t.setstatus`
					> Change bot playing status message

				`t.load`
					> Load a cog

				`t.unload`
					> Unload a cog

				`t.reload`
					> Reload a cog
				""")
			embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
			embed.colour = 0xFF0000
			await ctx.send(embed=embed)

		elif args == 'listeners':
			embed=discord.Embed(title="Listeners", description="""
				*These are ARs (Autoresponders) and not commands*

				`test`
					> Does a test
				""")
			embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
			embed.colour = 0xFF0000
			await ctx.send(embed=embed)

		else:
			await ctx.send(args)

def setup(bot: commands.bot):
	bot.add_cog(helpme(bot))