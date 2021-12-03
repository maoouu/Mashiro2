from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_reaction_add(self, reaction, user):
        """Takes the last, longest word in the message; Adds 'Mama mo' as its prefix."""
        if not reaction.emoji == '\N{woman}':
            return
        elif user.bot: # Ignore bot-created reactions
            return
        elif reaction.count > 1: # Ignore more than one reaction
            return
        
        words = reaction.message.clean_content.strip().split(' ')
        words.sort(key=len)
        await reaction.message.reply(f"Mama mo {words[-1].lower()}")


def setup(bot):
    bot.add_cog(Fun(bot))