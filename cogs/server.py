import nextcord
from nextcord.ext import commands
from utils import default


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self.db = default.database()

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """Pong!"""
        latency = round(self.bot.latency * 1000)
        message = await ctx.send("Pong!")
        await message.edit(content=f"Latency: {latency}ms")

    @commands.command()
    @commands.guild_only()
    async def prefix(self, ctx, prefix: str = None):
        """Shows the server's prefix. Can be configured"""
        if prefix == None:
            await ctx.send(f"My prefix is `{self.bot.command_prefix}`")
        # elif prefix == self.bot.command_prefix:
        #    await ctx.send(f"Prefix is already `{prefix}`.")
        # else:
        #    self.bot.command_prefix = prefix
        #    await ctx.send(f"Prefix is now set to `{self.bot.command_prefix}`")


def setup(bot):
    bot.add_cog(Server(bot))
