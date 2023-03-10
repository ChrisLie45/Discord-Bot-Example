# Error handler class modified from:
# https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612

import discord
import traceback
import sys
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = ()

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found')

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Pass in all required arguments')
        
        elif isinstance(error, commands.ConversionError):
            await ctx.send('Invalid argument type')

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'rps':  # Check if the command being invoked is 'rps'
                await ctx.send('Only rock, paper or scissors are valid arguments.')

        elif isinstance(error, commands.UserInputError):
            await ctx.send('Invalid argument')

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            print(error)


async def setup(bot):
    await bot.add_cog(CommandErrorHandler(bot))