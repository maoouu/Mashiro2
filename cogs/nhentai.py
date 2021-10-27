# from NHentai import NHentai
from hentai import Hentai, Format
from nextcord import Embed
from nextcord.ext import commands
from utils import default, doujintools


class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    # Async Commands
    @commands.command(aliases=["sc"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def decode(self, ctx, doujin_id):
        """Sends an embed of the particular Doujin ID."""
        message = await ctx.send(f"Retrieving `{doujin_id}`")
        embed = doujintools.get_doujin_embed(doujin_id)
        await message.edit(content="", embed=embed)


def setup(bot):
    bot.add_cog(Nhentai(bot))
