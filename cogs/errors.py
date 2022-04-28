from nextcord import Interaction
from nextcord.ext import commands, application_checks
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

        elif isinstance(error, commands.NotOwner):
            await ctx.send("This command is for the owner only.")

    @commands.Cog.listener()
    async def on_application_command_error(self, interaction: Interaction, error):
        """Global Slash Command Error Handler

        Args:
            interaction (Interaction)
            error (_type_): error to be handled
        """
        # Ignore commands that have local error handlers
        if interaction.application_command.has_error_handler():
            return
        
        ignored = ()
        
        error = getattr(error, "original", error)
        
        # If error is listed in 'ignored', return
        if isinstance(error, ignored):
            return
        
        elif isinstance(error, application_checks.errors.ApplicationNSFWChannelRequired):
            await interaction.response.send_message(
                "Must be in `NSFW` channel in order to proceed.", 
                ephemeral=True
            )
        
        elif isinstance(error, application_checks.errors.ApplicationNotOwner):
            await interaction.response.send_message(
                "Only the bot owner can execute this command.",
                ephemeral=True
            )
    
def setup(bot):
    bot.add_cog(Errors(bot))
