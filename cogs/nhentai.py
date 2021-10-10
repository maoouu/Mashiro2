from nextcord.ext import commands
from utils import default


class Nhentai(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()

  @commands.command(aliases=['sc'])
  async def sauce(self, ctx, nuke_code):
    # Rewrite Nhentai modules from previous project
    await ctx.send("Test")

def setup(bot):
  bot.add_cog(Nhentai(bot))
