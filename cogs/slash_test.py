from nextcord import Interaction
from nextcord.ext import commands
from utils import default, doujintools
import nextcord


test_guilds = [357495283401097218, 888829455223627828, 699583140234002484]

class SlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @nextcord.slash_command(guild_ids=test_guilds)
    async def test_slash_msg(self, interaction: Interaction):
        await interaction.response.send_message("Hello there, slash user~!")

    @nextcord.slash_command(guild_ids=test_guilds)
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("Pong!")

    @nextcord.slash_command(guild_ids=test_guilds)
    async def say(self, interaction: Interaction, message: str):
        await interaction.response.send_message(message, ephemeral=True)


class NHentaiSlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @nextcord.slash_command(
        description="Sends an embed of the particular Doujin ID.",
        guild_ids=test_guilds
    )
    async def sauce(self, interaction: Interaction, id: str):
        embed = doujintools.get_doujin_embed(id)
        await interaction.response.send_message(content="", embed=embed, ephemeral=True)

    @nextcord.slash_command(
        description="Turns doujin into a readable discord embed",
        guild_ids=test_guilds
    )
    async def read(self, interaction: Interaction, id: str):
        await doujintools.slash_reader(interaction, id)


def setup(bot):
    bot.add_cog(SlashCommandsTest(bot))
    bot.add_cog(NHentaiSlashCommandsTest(bot))