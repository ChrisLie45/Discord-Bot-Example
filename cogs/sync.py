from typing import Literal, Optional
from discord.ext import commands
from discord.ext.commands import Context

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # This command is used to sync commands to the current guild or globally
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: Context, spec: Optional[Literal["g"]] = None) -> None:
        """Sync commands to the current guild or globally
        Global commands are synced to all guilds and may take up to an hour to update
        
        Warning: There is a rate limit on syncing commands. Do not spam this command or you will be rate limited. 

        Parameters
        ----------

        spec: Optional:char
            The specifier for the sync. If "g" is passed, the commands will be synced globally. Otherwise, they will be synced to the current guild
        """

        if spec == "g":
            synced_commands = await self.bot.tree.sync()
        else:
            self.bot.tree.copy_global_to(guild=ctx.guild)
            synced_commands = await self.bot.tree.sync(guild=ctx.guild)

        if len(synced_commands) == 0:
            await ctx.send("No commands to sync")
        else:
            synced_commands_str = '\n   '.join(f"{command.name}" for command in synced_commands)
            await ctx.send(f"Synced the following commands {'to the current guild' if spec is None else 'globally'}:\n{synced_commands_str}")


async def setup(bot) -> None:
    await bot.add_cog(Sync(bot))