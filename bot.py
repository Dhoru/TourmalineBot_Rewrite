import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from dotenv import load_dotenv
from os import getenv
import traceback
import sys

load_dotenv()

token = getenv("TOKEN")

description = "TourmalineBot - Made by dhoru#7700"
bot = commands.Bot(command_prefix="t.", description=description, intents=discord.Intents.all())
bot.remove_command('help')

bot.load_extension("cogs.maincommands")
bot.load_extension("cogs.listener")
bot.load_extension("cogs.ownerCommands")
bot.load_extension("cogs.helpme")

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

bot.run(token)

