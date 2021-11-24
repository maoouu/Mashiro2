from nextcord import ui
from nextcord.ext import commands, menus
#from nextcord.ext.menus import MenuPaginationButton
from utils import default


class ReactionMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        return await channel.send(f"Hello {ctx.author}")
    
    @menus.button('\N{THUMBS UP SIGN}')
    async def on_thumbs_up(self, payload):
        await self.message.edit(content=f"Thanks {self.ctx.author}!")
    
    @menus.button('\N{THUMBS DOWN SIGN}')
    async def on_thumbs_down(self, payload):
        await self.message.edit(content="Ohh... okay.")
    
    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        self.stop()
        await self.message.delete()



class ReaderMenu(menus.ButtonMenu):
    def __init__(self):
        super().__init__(timeout=10,disable_buttons_after=True)

    async def send_initial_message(self, ctx, channel):
        return await channel.send(f"Hello {ctx.author}", view=self)
    
    @ui.button(emoji='\N{Black Left-Pointing Triangle}')
    async def on_thumbs_up(self, button, interaction):
        await self.message.edit(content=f"Thanks {interaction.user}!")
    
    @ui.button(emoji='\N{Octagonal Sign}')
    async def on_stop(self, button, interaction):
        await self.message.edit(content="Reader has been stopped.")
        self.stop()
    
    @ui.button(emoji='\N{Black Right-Pointing Triangle}')
    async def on_thumbs_down(self, button, interaction):
        await self.message.edit(content="Ohh... okay.")
    
    async def on_timeout(self):
        await self.message.edit(content="Reader has timed out.")
        self.stop()



class TestPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=1)
    
    async def format_page(self, menu, entries):
        return '\n'.join(entries)


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reaction_buttons(self, ctx):
        await ReactionMenu().start(ctx)
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def discord_buttons(self, ctx):
        await ReaderMenu().start(ctx)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def basic_page(self, ctx):
        entries = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        pages = menus.ButtonMenuPages(
            source=TestPageSource(entries),
            clear_buttons_after=True
        )
        await pages.start(ctx)
        
        
def setup(bot):
    bot.add_cog(Test(bot))