import discord
from discord.ext import commands

description = "TourmalineBot - Made by dhoru#7700"
bot = commands.Bot(command_prefix="t.", description=description, intents=discord.Intents.all())

bot.load_extension("somecommands")

@bot.event
async def on_ready():
    activity = discord.Game(name="Dhoru is Epic | t.help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("------")
    print("Bot is ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run("TOKEN")

