from nextcord.ext import commands
from utils import default


class Server(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()
  
  
  @commands.command()
  async def ping(self, ctx):
    """ Pong! """
    await ctx.send("Pong!")


def setup(bot):
  bot.add_cog(Server(bot))