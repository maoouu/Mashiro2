import os
import nextcord
import keep_alive

from utils import default
from utils.data import Bot, HelpFormat

config = default.config()


def get_prefix(bot, message):
    """Gets the custom guild prefix,
    returns default prefix if it doesn't exist."""
    db = default.database()
    prefix = config["prefix"]
    guild_id = str(message.guild.id)

    if guild_id in db.keys():
        prefix = db[guild_id]
    else:
        db[guild_id] = prefix

    return prefix


def main():
    print("Logging in...")
    bot = Bot(
        command_prefix=get_prefix,  # config["prefix"],
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
