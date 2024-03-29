import discord
from discord import app_commands
from discord.ext import commands


class betaCmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@app_commands.command(name="command-1")
	async def my_command(self, interaction: discord.Interaction) -> None:
		""" /command-1 """
		await interaction.response.send_message("Hello from command 1!", ephemeral=True)

	@app_commands.command(name="command-2")
	@app_commands.guilds(discord.Object(id=725560468558839851))
	async def my_private_command(self, interaction: discord.Interaction) -> None:
		""" /command-2 """
		await interaction.response.send_message("Hello from private command!", ephemeral=True)
	
def setup(bot: commands.bot):
	bot.add_cog(betaCmd(bot))