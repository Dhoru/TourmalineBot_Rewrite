import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")

class listener(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'test' in message.content.lower():
            await message.channel.send('oh look it worked yay')
        elif 'ping' in message.content.lower():
            await message.channel.send(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot: commands.bot):
    bot.add_cog(listener(bot))