from hentai import Hentai
from nextcord.ext import commands
from utils import default, doujintools


class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(aliases=["sc"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def sauce(self, ctx, hentai_code):
        """Sends an embed of the particular Doujin ID."""
        message = await ctx.reply(f"Retrieving `{hentai_code}`")
        embed = doujintools.get_doujin_embed(hentai_code)
        await message.edit(content="", embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def read(self, ctx, hentai_code):
        """Turns doujin into a readable discord embed."""
        message = await ctx.reply("Initializing reader...")
        await doujintools.doujin_reader(ctx, message, hentai_code)

    @commands.command(hidden=True)
    @commands.is_owner()
    @commands.is_nsfw()
    async def test_doujin(self, ctx):
        try:
          await ctx.send(f"{Hentai.exists(177013)}")
        except Exception as e:
          await ctx.send(f"Cannot execute code: {e}")


def setup(bot):
    bot.add_cog(Nhentai(bot))
