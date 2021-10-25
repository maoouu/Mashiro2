from nextcord.ext import commands
from utils import default

# from nextcord.ext.commands import errors


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Command Error Handler.
        Credits to Evieepy: https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612"""
        # This prevents any commands with local handlers from being handled.
        if hasattr(ctx.command, "on_error"):
            return

        ignored = (commands.CommandNotFound,)

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, "original", error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f"{ctx.command} has been disabled.")

        elif isinstance(error, commands.NSFWChannelRequired):
            await ctx.send("This command is only available in `NSFW` channels.")


def setup(bot):
    bot.add_cog(Errors(bot))
