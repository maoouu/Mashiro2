import asyncio

from hentai import Hentai, Format
from nextcord import Embed, Interaction
from utils.reader import HentaiMenuPages, HentaiPageSource

colors = {
    "RED": 0xc93434,
}

nhentai_icon = "https://clipground.com/images/nhentai-logo-3.jpg"
nhentai_HOME = "https://nhentai.net/"

def get_doujin_embed(doujin_id):
    """Prepares an embed to display information according to the parsed doujin_id.
    
    Parameters
    ----------
    doujin_id : str
        user-input Nhentai Doujin ID.
    """

    # First, check if doujin id exists in NHentai
    if Hentai.exists(doujin_id):
        try:
            # Get Hentai object from parsing doujin_id
            doujin = Hentai(doujin_id)

            # Get EN Title if it exists, else get JP title
            title = doujin.title(Format.English) if doujin.title(Format.English) else doujin.title
            (Format.Japanese)

            # Get the Artist
            artists = "N/A"
            if doujin.artist:
                artists = [f"`{getattr(artist, 'name')}`" for artist in doujin.artist]
                artists = ", ".join(artists)

            # Get JP Title if it exists
            jp_title = "N/A"
            if doujin.title(Format.Japanese):
                jp_title = doujin.title(Format.Japanese)

            # Gets the characters if it exist
            characters = "N/A"
            if doujin.character:
                characters = [
                    f"{getattr(character, 'name')}" for character in doujin.character
                ]
                characters = ", ".join(characters)

            # Gets the author group
            groups = "N/A"
            if doujin.group:
                groups = [f"{getattr(group, 'name')}" for group in doujin.group]
                groups = ", ".join(groups)

            # Collect all the doujin's tags
            tags = "N/A"
            if doujin.tag:
                tags = [getattr(tag, "name") for tag in doujin.tag]
                tags = ", ".join(tags)

            description = f"""ID: `{doujin.id}`
            Japanese Title: `{jp_title}`
            Artists: `{artists}`
            Groups: `{groups}`
            Characters: `{characters}`
            Pages: `{doujin.num_pages}`
            Tags: `{tags}`"""

            # Assemble the embed
            embed = Embed(title=title, description=description, url=doujin.url)
            embed.set_thumbnail(url=doujin.thumbnail)
            embed.set_author(
                name="NHentai",
                icon_url=nhentai_icon,
                url=doujin.HOME
            )
            embed.set_image(url=doujin.cover)
            embed.set_footer(
                text=f"Uploaded on {doujin.upload_date.strftime('%d-%m-%Y')}"
            )
            return embed

        except Exception as e:
            print(f"There's something wrong with the embed: {e}")

    else:
        embed = Embed(title="Error", description="The doujin you are looking for does not exist", color=colors["RED"])
        embed.set_author(
            name="NHentai", icon_url=nhentai_icon
        )
        return embed


async def doujin_reader(ctx, message, doujin_id):
    """ Handles the initialization and preparing readable discord embeds for doujin_id.
    
    Parameters
    ----------
    ctx : nextcord.ext.Commands.Context
        Nextcord command context.

    message : nextcord.Message
        previous message by the bot.

    doujin_id : str
        parseable nhentai doujin ID.
    """
    if Hentai.exists(doujin_id):
        try:
            #Initialize data
            doujin = Hentai(doujin_id)
            title = doujin.title(Format.Pretty)
            pages = tuple(getattr(pages, "url") for pages in doujin.pages)
            await message.edit(content=f"Reading **{title}**...")
            reader = HentaiMenuPages(source=HentaiPageSource(pages))
            await reader.start(ctx)
        except Exception as e:
            await ctx.send(f"There was something wrong with loading the doujin, please try again: `{e}`")
    else:
        embed = Embed(title="Error", description="The doujin you are looking for does not exist.", color=colors["RED"])
        embed.set_author(
            name="NHentai", icon_url=nhentai_icon
        )
        await message.edit(content="", embed=embed)
    

async def slash_reader(interaction: Interaction, doujin_id: str):
    """ The slash command variant of doujin_reader().
    
    Parameters
    ----------
    interaction : nextcord.Interaction
        Nextcord slash interaction.
    
    doujin_id : str
        parseable nhentai doujin ID.
    """
    if Hentai.exists(doujin_id):
        try:
            #Initialize data
            doujin = Hentai(doujin_id)
            title = doujin.title(Format.Pretty)
            pages = tuple(getattr(pages, "url") for pages in doujin.pages)
            reader = HentaiMenuPages(source=HentaiPageSource(pages))
            await reader.start(interaction=interaction, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"There was something wrong with loading the doujin, please try again: `{e}`")
    else:
        embed = Embed(title="Error", description="The doujin you are looking for does not exist.", color=colors["RED"])
        embed.set_author(
            name="NHentai", icon_url=nhentai_icon
        )
        await interaction.response.send_message(content="", embed=embed)