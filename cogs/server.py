from nextcord import Embed
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
        embed = Embed(description=f"Latency: {latency}ms")
        await message.edit(content="", embed=embed)

    @commands.command()
    @commands.guild_only()
    async def prefix(self, ctx, new_prefix: str = None):
        """Shows the server's prefix. Can be configured"""
        guild_id = str(ctx.guild.id)
        guild_prefix = self.db[guild_id]
        if new_prefix == None:
            embed = Embed(description=f"My prefix is `{guild_prefix}`")
            await ctx.send(embed=embed)
        elif new_prefix == guild_prefix:
            embed = Embed(description=f"My prefix is `{guild_prefix}`")
            await ctx.send(embed=embed)
        else:
            self.db[guild_id] = new_prefix
            embed = Embed(description=f"Prefix is now set to `{new_prefix}`")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Server(bot))
