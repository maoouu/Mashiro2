from nextcord.ext import commands
from utils import default
#from nextcord.ext.commands import errors

class Errors(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()
  
  


def setup(bot):
  bot.add_cog(Errors(bot))