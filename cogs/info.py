import nextcord
from nextcord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx):
        """Fetches MashiroBot's source code link."""
        description = f"""{ctx.bot.user.name}'s source code can be found here:\nhttps://github.com/maoouu/Mashiro2\n\nMashiroBot's basic functions have been derived from AlexFlipNote's discord bot framework:\nhttps://github.com/AlexFlipnote/discord_bot.py
        """

        embed = nextcord.Embed(
          title="Source Code",
          description = description,
          color=0xEE6611
        )
        embed.set_thumbnail(url="https://ih1.redbubble.net/image.148295913.6095/flat,1000x1000,075,f.u4.jpg")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
