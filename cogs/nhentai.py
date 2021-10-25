#from NHentai import NHentai
from hentai import Hentai, Format
from nextcord import Embed
from nextcord.ext import commands
from utils import default#, doujintools



class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()


    # Async Commands
    @commands.command(aliases=["sc"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def decode(self, ctx, nuke_code):
        """#Sends an embed of the particular Doujin ID."""
        message = await ctx.send(f"Retrieving `{nuke_code}`")
        #doujin = Hentai(nuke_code)
        #nhentai = NHentai()
        #doujin = nhentai.get_doujin(id=nuke_code)
        embed = self.get_doujin_embed(nuke_code)
        await message.edit(content="",embed=embed)
        #await message.edit(content=doujin.title(Format.English))

    def get_doujin_embed(self, nuke_code):
        doujin = ""
        title = ""
        jp_title = ""
        artists = []
        characters = []
        groups = []
        tags = []
        embed = Embed()

        if Hentai.exists(nuke_code):
          doujin = Hentai(nuke_code)
          title = "Test"
          description = "It Works!"
        else:
          title = "Error"
          description = "The doujin you are looking for does not exist"
        
        embed = Embed(title=title, description=description)
        embed.set_author(
            name="NHentai",
            icon_url="https://clipground.com/images/nhentai-logo-3.jpg"
        )
        return embed
      #return Embed(title=doujin.title(Format.English), description="Test").set_image(url=doujin.cover)
      # TODO: fix embedding of Hentai API


def setup(bot):
    bot.add_cog(Nhentai(bot))
