from nextcord import ButtonStyle, Interaction
from nextcord.ui import button, Button, view

class Decode(view):
    def __init__(self):
        super().__init__()
        self.value = None
    
    @button(label="Delete", style=ButtonStyle.green)
    async def delete(self, button: Button, interaction: Interaction):
        pass
        #await interaction.response()