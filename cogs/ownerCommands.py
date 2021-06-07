import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class ownerCommands(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name='unload')
	@commands.is_owner()
	async def unload(self, ctx: commands.Context, args):
		ctx.bot.unload_extension(args)
		await ctx.message.add_reaction("<:greentick:719778001373364304>")

	@commands.command(name='load')
	@commands.is_owner()
	async def load(self, ctx: commands.Context, args):
		ctx.bot.load_extension(args)
		await ctx.message.add_reaction("<:greentick:719778001373364304>")

	@commands.command(name='reload')
	@commands.is_owner()
	async def reload(self, ctx: commands.Context, args):
		ctx.bot.reload_extension(args)
		await ctx.message.add_reaction("<:greentick:719778001373364304>")

	@commands.command(name="setstatus", help="Changes the status of the bot", Hidden=True)
	@commands.is_owner()
	async def setstatus(self, ctx, *, text: str):
		await self.bot.change_presence(activity=discord.Game(name=text))

def setup(bot: commands.bot):
	bot.add_cog(ownerCommands(bot))