import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t.")


class ban(commands.Cog):
    """A couple of simple commands. """

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="ban")
    async def ban(ctx, member:discord.User=None, delete_message_days = 1, *, message=None):
        message = message or "Message"
        await Client.ban(member, days=0)
        await ctx.send('User has been banned for **'+ str(days) + ' day(s)**')
        ban_list.append(member)
        day_list.append(ctx.message.server)
        if (ctx.message.author.has_permissions(ban_members=False)):
            ctx.send('You do not have permission to ban members!')

        
        


def setup(bot: commands.bot):
    bot.add_cog(ban(bot))

