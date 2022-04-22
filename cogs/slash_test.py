from main import db
from nextcord import Interaction
from nextcord.ext import commands
from utils import default
import nextcord


class SlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @nextcord.slash_command()
    async def test_slash_msg(self, interaction: Interaction):
        await interaction.response.send_message("Hello there, slash user~!")

    @nextcord.slash_command()
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("Pong!")

def setup(bot):
    bot.add_cog(SlashCommandsTest(bot))