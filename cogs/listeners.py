import psutil
import os
import nextcord
import datetime

from nextcord.ext import commands
from utils import default

class Listeners(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()
    self.process = psutil.Process(os.getpid())


    @commands.Cog.listener()
    async def on_command(self, ctx):
      try:
        print(f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}")
      except AttributeError:
        print(f"Private message > {ctx.author} > {ctx.message.clean_content}")
    

    @commands.Cog.listener()
    async def on_ready(self):
      if not hasattr(self.bot, 'uptime'):
        self.bot.uptime = datetime.utcnow()

      # Check if user wants different status
      status = self.config["status"].lower()
      status_type = {"idle": nextcord.Status.idle, "dnd": nextcord.Status.dnd}

      # Check if user wants different activity
      activity = self.config["activity_type"].lower()
      activity_type = {"listening": 2, "watching": 3, "competing": 5}

      await self.bot.change_presence(
        activity.nextcord.Game(
          type=activity_type.get(activity, 0),
          name=self.config["activity"]
        ),
        status=status_type.get(status, nextcord.Status.online)
      )

      # Indicate successful bootup
      print(f'Ready: {self.bot.user} | Servers: {len(self.bot.guilds)}')


def setup(bot):
  bot.add_cog(Listeners(bot))
      