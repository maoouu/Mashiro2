import os
import discord
import keep_alive

from utils import default
from utils.data import Bot, HelpFormat

config = default.config()
print("Logging in...")

bot = Bot(
  command_prefix=config["prefix"],
  prefix=config["prefix"],
  command_attrs=dict(hidden=True),
  help_command=HelpFormat(),
  intents=discord.Intents(
    guilds=True, members=True, messages=True,
    reactions=True, presences=True
  )
)

# Loading Cogs
for file in os.listdir("cogs"):
  if file.endswith(".py"):
    name = file[:-3]
    bot.load_extension(f"cogs.{name}")


try:
  # run the server
  keep_alive.keep_alive()
  # run the bot
  bot.run(os.environ['BOT_TOKEN'])
except Exception as e:
  print(f'Error when logging in: {e}')