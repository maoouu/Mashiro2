from nextcord import Interaction
from nextcord.ext import commands, application_checks
from utils import default, doujintools
import nextcord, os


test_guilds = [os.environ['TEST_1'], os.environ['TEST_2'], os.environ['TEST_3']]

class SlashCommandsTest(commands.Cog):
    
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


class AdminSlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #def is_owner(interaction: Interaction):
    #   return interaction.message.author.id == os.environ["OWNER_ID"]
    
    @nextcord.slash_command(
        description="Loads extension. (Owner only)",
        guild_ids=test_guilds
    )
    @application_checks.is_owner()
    async def load(self, interaction: Interaction, name: str):
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await interaction.response.send_message(default.traceback_maker(e))
        await interaction.response.send_message(f"Loaded extension: [`{name}`]")
        
    @nextcord.slash_command(
        description="Unloads extension. (Owner only)",
        guild_ids=test_guilds
    )
    @application_checks.is_owner()
    async def unload(self, interaction: Interaction, name: str):
        pass
        
def setup(bot):
    bot.add_cog(SlashCommandsTest(bot))
    bot.add_cog(NHentaiSlashCommandsTest(bot))