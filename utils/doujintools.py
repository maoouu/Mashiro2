from hentai import Hentai, Format
from nextcord import Embed


def get_doujin_embed(doujin_id):
    doujin = ""
    title = ""
    description = ""
    # footer = ""
    jp_title = ""
    # cover = ""
    # thumbnail = ""
    artists = []
    characters = []
    groups = []
    tags = []
    embed = Embed()

    # First, check if doujin id exists in NHentai
    if Hentai.exists(doujin_id):
        try:
            doujin = Hentai(doujin_id)

            # Get EN Title if it exists, else get JP title
            if doujin.title(Format.English):
                title = doujin.title(Format.English)
            else:
                title = doujin.title(Format.Japanese)

            # Get the Artist
            if doujin.artist:
                artists = [f"`{getattr(artist, 'name')}`" for artist in doujin.artist]
                artists = ", ".join(artists)
            else:
                artists = "N/A"

            # Get JP Title if it exists
            if doujin.title(Format.Japanese):
                jp_title = doujin.title(Format.Japanese)
            else:
                jp_title = "N/A"

            # Gets the characters if it exist
            if doujin.character:
                characters = [
                    f"{getattr(character, 'name')}" for character in doujin.character
                ]
                characters = ", ".join(characters)
            else:
                characters = "N/A"

            # Gets the author group
            if doujin.group:
                groups = [f"{getattr(group, 'name')}" for group in doujin.group]
                groups = ", ".join(groups)
            else:
                groups = "N/A"

            # Collect all the doujin's tags
            if doujin.tag:
                tags = [getattr(tag, "name") for tag in doujin.tag]
                tags = ", ".join(tags)
            else:
                tags = "N/A"

            description = f"""ID: `{doujin.id}`
            Japanese Title: `{jp_title}`
            Artists: `{artists}`
            Groups: `{groups}`
            Characters: `{characters}`
            Pages: `{doujin.num_pages}`
            Tags: `{tags}`"""

            # Assemble the embed
            embed = Embed(title=title, description=description)
            embed.set_thumbnail(url=doujin.thumbnail)
            embed.set_author(
                name="NHentai",
                icon_url="https://clipground.com/images/nhentai-logo-3.jpg",
            )
            embed.set_image(url=doujin.cover)
            embed.set_footer(
                text=f"Uploaded at {doujin.upload_date.strftime('%d-%m-%Y')}"
            )
            return embed

        except Exception as e:
            print(f"There's something wrong with the embed: {e}")

    else:
        title = "Error"
        description = "The doujin you are looking for does not exist"
        embed = Embed(title=title, description=description)
        embed.set_author(
            name="NHentai", icon_url="https://clipground.com/images/nhentai-logo-3.jpg"
        )
        return embed
