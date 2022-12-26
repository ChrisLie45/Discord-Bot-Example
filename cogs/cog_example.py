from discord.ext import commands
from discord.ext.commands import Context

# This is the class that will be loaded as a cog
class CogExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # This command will be loaded as apart of the cog category
    # A command is defined by the @commands.command() decorator above a function
    @commands.command()
    async def ping(self, ctx: Context):
        """Ping command to test response time of the bot"""

        # Latency is in seconds, so we multiply by 1000 to get milliseconds
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! Latency is {latency}ms")


# This function is called when the cog is loaded
# It must be asynchronous and take a bot as an argument
# It must also add the cog to the bot
async def setup(bot):
    await bot.add_cog(CogExample(bot))