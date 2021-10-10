from nextcord.ext import commands
from utils import default
from nextcord.ext.commands import errors

class Errors(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()
  
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, err):

    MISSING_REQUIREMENTS = isinstance(err, errors.MissingRequiredArguments)
    BAD_ARG = isinstance(err, errors.BadArgument)
    CMD_INVOKE_ERR = isinstance(err, errors.CommandInvokeError)
    CHECK_FAILURE = isinstance(err, errors.CheckFailure)
    MAX_CONCUR = isinstance(err, errors.MaxConcurrencyReached)
    COMMAND_COOLDOWN = isinstance(err, errors.CommandOnCooldown)
    COMMAND_NOT_FOUND = isinstance(err, errors.CommandNotFound)

    #elif NSFW_REQUIRED:
    #  await ctx.send("NSFW channels only.")

    if MISSING_REQUIREMENTS or BAD_ARG:
      helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
      return await ctx.send_help(helper)

    elif CMD_INVOKE_ERR:
      error = default.traceback_maker(err.original)

      if "2000 or fewer" in str(err) and len(ctx.message.clean_content) > 1900:
        return await ctx.send("You attempted to make the command display more than 2,000 characters...\nBoth error and command will be ignored.")
        
      return await ctx.send(f"There was an error processing the command: {error}")
      
    elif CHECK_FAILURE:
      pass
      
    elif MAX_CONCUR:
      return await ctx.send("You've reached max capacity of command usage at once, please finish the previous one...")
      
    elif COMMAND_COOLDOWN:
      return await ctx.send(f"Command on cooldown, try again after {err.retry_after:.2f} seconds")

    elif COMMAND_NOT_FOUND:
      pass
  


def setup(bot):
  bot.add_cog(Errors(bot))