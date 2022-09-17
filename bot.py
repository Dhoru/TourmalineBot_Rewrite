import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from dotenv import load_dotenv
from os import getenv
import typing
import traceback
import sys

load_dotenv()

token = getenv("TOKEN")

description = "TourmalineBot - Made by dhoru#7700"
bot = commands.Bot(command_prefix="t.", description=description, intents=discord.Intents.all())
bot.remove_command('help')

#bot.load_extension("cogs.mainCommands")
#bot.load_extension("cogs.ownerCommands")
#bot.load_extension("cogs.helpMe")
#bot.load_extension("cogs.miscCommands")
bot.load_extension("cogs.betaCmd")

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: typing.Optional[typing.Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

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