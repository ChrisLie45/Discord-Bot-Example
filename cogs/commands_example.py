from discord.ext import commands
from discord.ext.commands import Context

# Basic prefix commands with arguments example 
class CommandsExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def args(self, ctx: Context, arg1, arg2) -> None:
        """
        Command with arguments
        
        Usage: 
        args <arg1> <arg2>
        """

        await ctx.send(f"arg1: {arg1}, arg2: {arg2}")
    

    @commands.command()
    async def args_optional(self, ctx: Context, arg1=None) -> None:
        """
        Command with optional arguments
        
        Usage: 
        args_optional <arg1> <arg2>
        """

        if arg1 is None:
            await ctx.send("No arguments provided")
        else:
            await ctx.send(f"arg1: {arg1}")
    

    @commands.command()
    async def args_variable(self, ctx: Context, *args) -> None:
        """
        Command with variable amount of arguments
        
        Usage: 
        args_unlimited <arg1> <arg2> <arg3> ...
        """

        arguments = ', '.join(args)
        await ctx.send(f'{len(args)} arguments: {arguments}')
    

    # This command will throw an error if the user does not provide a number as the second argument
    @commands.command()
    async def args_type(self, ctx: Context, arg1: str, arg2: int) -> None:
        """
        Command with argument type conversion
        
        Usage: 
        args_type <str> <int>
        """

        await ctx.send(f"arg1 is str = {type(arg1) is str}")
        await ctx.send(f"arg2 is int = {type(arg2) is int}")


async def setup(bot):
    await bot.add_cog(CommandsExample(bot))