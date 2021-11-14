from nextcord.ext import commands
from utils import default, doujintools


class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(aliases=["dc"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def decode(self, ctx, hentai_code):
        """Sends an embed of the particular Doujin ID."""
        message = await ctx.send(f"Retrieving `{hentai_code}`")
        embed = doujintools.get_doujin_embed(hentai_code)
        await message.edit(content="", embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def read(self, ctx, hentai_code):
        """Turns doujin into a readable discord embed."""
        embed = doujintools.get_readable_doujin(hentai_code)
        message = await ctx.send(embed[0])


def setup(bot):
    bot.add_cog(Nhentai(bot))
