import os
import nextcord
import keep_alive

from nextcord.ext import commands
from utils import default
from utils.data import Bot, HelpFormat

config = default.config()

def get_prefix(bot, message):
    """Gets the custom guild prefix,
    returns default prefix if it doesn't exist."""
    # prefix = config["prefix"]
    # guild_id = str(message.guild.id)
    # db = default.database()
    
    # try:
    #     if guild_id in db.keys():
    #         prefix = db[guild_id]
    #     else:
    #         db[guild_id] = prefix
    # except Exception as e:
    #     # Default to '!!' prefix
    #     prefix = "!!"
    #     print(f"Error when fetching database: {e}")
    #     print(f"Switching to default prefix [{prefix}]")
    # finally:
    #     #return prefix
    return commands.when_mentioned_or(config['prefix'])(bot, message)


def main():
    print("Logging in...")
    bot = Bot(
        command_prefix=get_prefix,
        command_attrs=dict(hidden=True),
        help_command=HelpFormat(),
        owner_id=int(os.environ["OWNER_ID"]),
        intents=nextcord.Intents(
            guilds=True, members=True, messages=True, reactions=True, presences=True
        ),
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
        bot.run(os.environ["BOT_TOKEN"])
    except Exception as e:
        print(f"Error when logging in: {e}")


if __name__ == "__main__":
    main()
