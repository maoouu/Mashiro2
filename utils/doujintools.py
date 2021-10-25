from hentai import Hentai, Format
from nextcord import Embed
# from NHentai.entities.doujin import Doujin


def get_doujin_embed(doujin):
    title = ""
    jp_title = ""
    artists = []
    characters = []
    groups = []
    tags = []
    embed = Embed()

    if Hentai.exists(doujin.id):
        # Gets EN title if it exists
        if doujin.title(Format.English):
            #title = doujin.title.english
            title = doujin.title(Format.English)
        else:
            title = doujin.title(Format.Japanese)

        # Gets the artists
        if doujin.artist:
            artists = [f"`{getattr(artist, 'name')}`" for artist in doujin.artist]
            artists = ", ".join(artists)
        else:
            artists = "N/A"

        # Gets JP Title if it exists
        if doujin.title(Format.Japanese):
            jp_title = doujin.title(Format.Japanese)
        else:
            jp_title = "N/A"

        # Gets the characters if it exists
        if doujin.character:
            characters = [
                f"`{getattr(character, 'name')}`" for character in doujin.character
            ]
            characters = ", ".join(characters)
        else:
            characters = "N/A"
        
        # Gets the group that made the doujinshi
        if doujin.group:
            groups = [f"`{getattr(group, 'name')}`" for group in doujin.group]
        else:
            groups = "N/A"

        # Collect all of the doujin's tags
        if doujin.tags:
            tags = [getattr(tag, "name") for tag in doujin.tags]
            tags = ", ".join(tags)
        else:
            tags = "N/A"

        description = f""" ID: `{doujin.id}`
            Japanese Title: `{jp_title}`
            Artists: {artists}
            Groups: {groups}
            Characters: {characters}
            Pages: `{doujin.total_pages}`
            Tags: {tags} """

        # Assemble the embed
        embed.set_thumbnail(url=doujin.cover)
        embed.set_image(url=doujin.cover)
        embed.set_footer(text=f"Uploaded at {doujin.upload_date.strftime('%d-%m-%Y')}")
    else:
        title = "Error"
        description = "The doujin you are looking for does not exist."

    embed = Embed(title=title, description=description)
    embed.set_author(
        name="NHentai", icon_url="https://clipground.com/images/nhentai-logo-3.jpg"
    )
    return embed
