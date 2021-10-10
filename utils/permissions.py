import os
import discord
import random

from utils import default
from discord.ext import commands

owner = os.environ['OWNER_ID']
config = default.config()


def is_owner(ctx):
  """ Checks if author is owner """
  return ctx.author.id == owner


def check_permissions(ctx, perms, *, check=all):
  """ If author has permissions to a permission """
  if is_owner(ctx):
    return True
  
  resolved = ctx.channel.permissions_for(ctx.author)
  return check(getattr(resolved, name, None) == value for name, value in perms.items())


async def check_priv(ctx, member):
  """ Checks permissions for moderation commands """
  try:
    # Self-check
    if member == ctx.author:
      return await ctx.send(f"You can't {ctx.command.name} yourself")
    if member.id == ctx.bot.user.id:
      return await ctx.send("Do you really distrust me this much? ;_;")

    # Check if user bypasses
    if ctx.author.id == ctx.guild.owner.id:
      return False

    # Permissions check
    if member.id == owner:
      if ctx.author.id != owner:
        return await ctx.send(f"I can't delete my creator :<")
      else:
        pass

    if member.id == ctx.guild.owner.id:
      return await ctx.send(random.choice(config['owner_deletion_messages']))
      
    if ctx.author.top_role == member.top_role:
      return await ctx.send("You can't do that with the same perms as you.")
    
    if ctx.author.top_role < member.top_role:
      return await ctx.send("You can't do that to someone higher than you.")

  except Exception:
    pass


def has_permissions(*, check=all, **perms):
  """ discord.Commands method if author has permissions """
  async def pred(ctx):
    return await check_permissions(ctx, perms, check=check)
  
  return commands.check(pred)


def can_handle(ctx, permission: str):
  """ If bot has permissions or in DM's """
  return isinstance(ctx.channel, discord.DMChannel) or getattr(ctx.channel.permissions_for(ctx.guild.me), permission)