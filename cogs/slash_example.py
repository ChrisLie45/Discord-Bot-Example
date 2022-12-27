import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

# Basic slash and hybrid commands example
class SlashExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # A slash command is defined by the @app_commands.command() decorator above a function 
    # It will only act as a slash command. It will not be available as a prefix command
    # Instead of a Context, it will take an Interaction as an argument
    @app_commands.command()
    async def slash(self, interaction: discord.Interaction) -> None:
        """Slash command"""

        await interaction.response.send_message("This is a slash command")
    

    # Ephemeral messages are only visible to the user who sent the command
    @app_commands.command()
    async def slash_eph(self, interaction: discord.Interaction) -> None:
        """Ephemeral Slash command"""

        await interaction.response.send_message("This is a ephemeral slash command", ephemeral=True)


    # A hybrid command is defined by the @commands.hybrid_command() decorator above a function
    # It will act as both a slash command and a prefix command
    @commands.hybrid_command()
    async def hybrid(self, ctx: Context) -> None:
        """Hybrid command"""

        await ctx.send("This is a hybrid command")


async def setup(bot):
    await bot.add_cog(SlashExample(bot))