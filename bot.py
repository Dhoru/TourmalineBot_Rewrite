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

bot.load_extension("cogs.mainCommands")
bot.load_extension("cogs.listener")
bot.load_extension("cogs.ownerCommands")
bot.load_extension("cogs.helpMe")
bot.load_extension("cogs.miscCommands")
bot.load_extension("cogs.betaCmd")

@bot.event
async def on_ready():
    activity = discord.Game(name="Dhoru is Epic | t.help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    botUserName = bot.user.name
    botUserId = bot.user.id
    initMessage = '''
    --------
    Bot is ready!
    Logged in as:
    {}
    {}
    --------
    '''
    initMessage = initMessage.format(botUserName, botUserId)
    print(initMessage)

bot.run(token)