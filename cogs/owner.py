import os
import importlib

from nextcord.ext import commands
from utils import default, permissions


class Owner(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.config = default.config()

  @commands.command()
  @commands.is_owner()
  async def load(self, ctx, name: str):
    """ Loads extension. (Owner only) """
    try:
      self.bot.load_extension(f"cogs.{name}")
    except Exception as e:
      return await ctx.send(default.tracemaker(e))
    await ctx.send(f"Loaded extension: [`{name}`]")

  
  @commands.command()
  @commands.is_owner()
  async def unload(self, ctx, name: str):
    """ Unloads extension. (Owner only) """
    try:
      self.bot.unload_extension(f"cogs.{name}")
    except Exception as e:
      return await ctx.send(default.tracemaker(e))
    await ctx.send(f"Unloaded extension: [`{name}`]")
  

  @commands.command()
  @commands.is_owner()
  async def reload(self, ctx, name: str):
    """ Reloads an extension. (Owner only)"""
    try:
      self.bot.reload_extension(f"cogs.{name}")
    except Exception as e:
      return await ctx.send(default.traceback_maker(e))
    await ctx.send(f"Reloaded extension [`{name}`]")


  @commands.command()
  @commands.is_owner()
  async def reloadAll(self, ctx):
    """ Reloads all extensions. (Owner only) """
    error_collection = []

    for file in os.listdir("cogs"):
      if file.endswith(".py"):
        name = file[:-3]
        try:
          self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
          error_collection.append([file, default.traceback_maker(e, advanced_traceback_mode=False)])
      
      if error_collection:
        output = "\n".join([f"**{g[0]}** ```diff\n- {g[1]}```" for g in error_collection])

        return await ctx.send(f"Attempted to reload all extensions, was able to reload, "
                f"however the following failed...\n\n{output}")
      
    await ctx.send("All extensions have reloaded successfully.")


  @commands.command()
  @commands.is_owner()
  async def reloadUtil(self, ctx, name: str):
    """ Reload Utility Modules. (Owner only) """
    name_maker = f"utils/{name}"
    try:
      module_name = importlib.import_module(f"utils.{name}")
      importlib.reload(module_name)
    except ModuleNotFoundError:
      return await ctx.send(f"Couldn't find module: {name}")
    except Exception as e:
      error = default.traceback_maker(e)
      return await ctx.send(f"Module '{name}' cannot be reloaded:\n{error}")
      
    await ctx.send(f"Reloaded module: {name_maker}")


    
def setup(bot):
  bot.add_cog(Owner(bot))
