from nextcord import Embed, Interaction
from nextcord.ext import commands, application_checks
from utils import default, doujintools
import nextcord, os


#TEST_GUILDS = [int(os.environ['TEST_1']), int(os.environ['TEST_2']), int(os.environ['TEST_3'])]


class SlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Pong!") #guild_ids=TEST_GUILDS)
    async def ping(self, interaction: Interaction):
        """Pong!

        Args:
            interaction (Interaction)
        """
        latency = round(self.bot.latency * 1000)
        embed = Embed(description=f"Latency: {latency}ms")
        await interaction.response.send_message(content="", embed=embed, ephemeral=True)

    @nextcord.slash_command(description="I will say it back.") #guild_ids=TEST_GUILDS)
    async def say(self, interaction: Interaction, message: str):
        """I will say it back.

        Args:
            interaction (Interaction)
            message (str): message string
        """
        await interaction.response.send_message(message, ephemeral=True)


class NHentaiSlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Sends an embed of the particular Doujin ID.") #guild_ids=TEST_GUILDS)
    @application_checks.is_nsfw()
    async def sauce(self, interaction: Interaction, id: str):
        """Sends an embed of the particular Doujin ID.

        Args:
            interaction (Interaction)
            id (str): NHentai Doujin ID
        """
        embed = doujintools.get_doujin_embed(id)
        await interaction.response.send_message(content="", embed=embed)

    @nextcord.slash_command(description="Turns doujin into a readable discord embed") #guild_ids=TEST_GUILDS)
    @application_checks.is_nsfw()
    async def read(self, interaction: Interaction, id: str):
        """Turns doujin into a readable discord embed

        Args:
            interaction (Interaction)
            id (str): NHentai Doujin ID
        """
        await doujintools.slash_reader(interaction, id)


class AdminSlashCommandsTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Loads extension. (Owner only)") #guild_ids=TEST_GUILDS)
    @application_checks.is_owner()
    async def load(self, interaction: Interaction, name: str):
        """Loads extension. (Owner only)

        Args:
            interaction (Interaction)
            name (str): name of cog extension

        Returns:
            Coroutine[Any, Any, None]
        """
        try:
            self.bot.load_extension(f"cogs.{name}")
            await self.bot.rollout_application_commands()
        except Exception as e:
            return await interaction.response.send_message(default.traceback_maker(e))
        await interaction.response.send_message(f"Loaded extension: [`{name}`]", ephemeral=True)
        
    @nextcord.slash_command(description="Unloads extension. (Owner only)") #guild_ids=TEST_GUILDS)
    @application_checks.is_owner()
    async def unload(self, interaction: Interaction, name: str):
        """Unloads extension. (Owner only)

        Args:
            interaction (Interaction)
            name (str): name of cog extension

        Returns:
            Coroutine[Any, Any, None]
        """
        try:
            self.bot.unload_extension(f"cogs.{name}")
            await self.bot.rollout_application_commands()
        except Exception as e:
            return await interaction.response.send_message(default.traceback_maker(e))
        await interaction.response.send_message(f"Unloaded extension: [`{name}`]", ephemeral=True)

    @nextcord.slash_command(description="Reloads extension. (Owner only)") #guild_ids=TEST_GUILDS)
    @application_checks.is_owner()
    async def reload(self, interaction: Interaction, name: str):
        """Reloads extension. (Owner only)

        Args:
            interaction (Interaction)
            name (str): name of cog extension

        Returns:
            Coroutine[Any, Any, None]
        """
        try:
            self.bot.reload_extension(f"cogs.{name}")
            await self.bot.rollout_application_commands()
        except Exception as e:
            return await interaction.response.send_message(default.traceback_maker(e))
        await interaction.response.send_message(f"Reloaded extension: [`{name}`]", ephemeral=True)
    
        
def setup(bot):
    bot.add_cog(SlashCommandsTest(bot))
    bot.add_cog(NHentaiSlashCommandsTest(bot))
    bot.add_cog(AdminSlashCommandsTest(bot))