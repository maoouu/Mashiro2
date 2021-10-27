from nextcord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx):
        """Give credits"""
        await ctx.send(
            f"{ctx.bot.user}'s Discord functionalities has been powered by this source code: \nhttps://github.com/AlexFlipnote/discord_bot.py"
        )


def setup(bot):
    bot.add_cog(Information(bot))
