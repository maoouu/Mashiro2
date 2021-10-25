from NHentai import NHentai
from NHentai.entities.doujin import Doujin
from nextcord.ext import commands
from utils import default, hentai


class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    # Async Commands
    @commands.command(aliases=["sc"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def decode(self, ctx, nuke_code: str):
        """Sends an embed of the particular Doujin ID."""
        message = await ctx.send(f"Retrieving `{nuke_code}`")
        nhentai = NHentai()
        doujin = nhentai.get_doujin(id=nuke_code)
        # message = await ctx.send(embed=hentai.get_doujin_embed(doujin))
        await message.edit(content="", embed=hentai.get_doujin_embed(doujin))


def setup(bot):
    bot.add_cog(Nhentai(bot))
