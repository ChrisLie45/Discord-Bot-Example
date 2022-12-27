import discord
from discord.ext import commands
from discord.ext.commands import Context

# Button class
class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Button", style=discord.ButtonStyle.red)
    async def gray_button(self, interaction:discord.Interaction, button:discord.ui.Button,):
        await interaction.response.send_message(content=f"You clicked the button!")
    
    
# Basic button example
class ButtonExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button(self, ctx: Context) -> None:
        """Button command"""

        view = Buttons()
        view.add_item(discord.ui.Button(label="In-depth Examples", style=discord.ButtonStyle.link, url="https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4"))

        await ctx.send("This is a button command",view=view)


async def setup(bot):
    await bot.add_cog(ButtonExample(bot))