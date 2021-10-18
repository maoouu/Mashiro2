from nextcord.ext import commands
from utils import default


class Server(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()
  
  
  @commands.command()
  @commands.guild_only()
  async def ping(self, ctx):
    """ Pong! """
    await ctx.send("Pong!")
  
  @commands.command()
  @commands.guild_only()
  async def prefix(self, ctx, prefix: str = None):
    """ Shows the server's prefix. Can be configured """
    if prefix == None:
      await ctx.send(f"My prefix is `{self.config['prefix']}`")

def setup(bot):
  bot.add_cog(Server(bot))