from nextcord import Embed
from nextcord.ext import menus

class HentaiMenuPages(menus.ButtonMenuPages, inherit_buttons=False):
    def __init__(self, source, timeout=300):
        super().__init__(source, timeout=timeout, disable_buttons_after=True,)

        #Add custom buttons
        self.add_item(menus.MenuPaginationButton(emoji=self.FIRST_PAGE, label="First"))
        self.add_item(menus.MenuPaginationButton(emoji=self.PREVIOUS_PAGE, label="Prev"))       
        self.add_item(menus.MenuPaginationButton(emoji=self.NEXT_PAGE, label="Next"))
        self.add_item(menus.MenuPaginationButton(emoji=self.LAST_PAGE, label="Last"))
        self.add_item(CustomStopButton(emoji=self.STOP, label="Close"))

        #Disable buttons that are unavailable to be pressed
        self._disable_unavailable_buttons()
    
    async def on_timeout(self):
        await self.message.edit(embed=Embed(description="Reader has timed out."))
        self.stop()


class CustomStopButton(menus.MenuPaginationButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    async def callback(self, interaction):
        await interaction.response.edit_message(embed=Embed(description="Reader has been closed."))
        self.view.stop()


class HentaiPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=1)
    
    async def format_page(self, menu, page):
        embed = Embed(color=0xc93434)
        #embed.set_author(name="NHentai", icon_url=nhentai_icon,)
        embed.set_image(url=page)
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}", icon_url="https://clipground.com/images/nhentai-logo-3.jpg")
        return embed
