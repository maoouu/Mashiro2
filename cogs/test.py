from nextcord.ext import commands#, menus
#from nextcord.ext.menus import MenuPaginationButton
from utils import default


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command()
    async def test(self, ctx):
        #pages = menus.ButtonMenuPages(source=Source())
        #await pages.start(ctx)
        pass

        
def setup(bot):
    bot.add_cog(Test(bot))