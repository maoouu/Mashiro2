from nextcord import Embed
from NHentai.entities.doujin import Doujin


def get_doujin_embed(doujin: Doujin):
    title = ""
    jp_title = ""
    artists = []
    characters = []
    groups = []
    tags = []
    embed = Embed()

    if doujin is not None:
        # Gets EN title if it exists
        if doujin.title.english:
            title = doujin.title.english
        else:
            title = doujin.title.japanese

        # Gets the artists
        if doujin.artists:
            artists = [f"`{getattr(artist, 'name')}`" for artist in doujin.artists]
            artists = ", ".join(artists)
        else:
            artists = "N/A"

        # Gets JP Title if it exists
        if doujin.title.japanese:
            jp_title = doujin.title.japanese
        else:
            jp_title = "N/A"

        # Gets the characters if it exists
        if doujin.characters:
            characters = [
                f"`{getattr(character, 'name')}`" for character in doujin.characters
            ]
            characters = ", ".join(characters)
        else:
            characters = "N/A"

        # Collect all of the doujin's tags
        if doujin.tags:
            tags = [getattr(tag, "name") for tag in doujin.tags]
            tags = ", ".join(tags)
        else:
            tags = "N/A"

        description = f""" ID: `{doujin.id}`
            Japanese Title: `{jp_title}`
            Artists: {artists}
            Characters: {characters}
            Pages: `{doujin.total_pages}`
            Tags: {tags} """

        # Assemble the embed
        embed.set_thumbnail(url=doujin.cover.src)
        embed.set_image(url=doujin.cover.src)
        embed.set_footer(text=f"Uploaded at {doujin.upload_at.strftime('%d-%m-%Y')}")
    else:
        title = "Error"
        description = "The doujin you are looking for does not exist."

    embed = Embed(title=title, description=description)
    embed.set_author(
        name="NHentai", icon_url="https://clipground.com/images/nhentai-logo-3.jpg"
    )
    return embed
