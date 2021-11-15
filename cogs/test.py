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


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reaction_buttons(self, ctx):
        await ReactionMenu().start(ctx)

        
def setup(bot):
    bot.add_cog(Test(bot))