import random
import discord
from discord.ext import commands
from discord.ext.commands import Context

# Converter for RPS choices
class RPSChoice(commands.Converter):
    async def convert(self, ctx: Context, argument: str):
        # Convert the argument to lowercase
        argument = argument.lower()

        # Check if the argument is a valid choice
        if argument in ["rock", "paper", "scissors"]:
            return argument
        else:
            raise commands.BadArgument


class RandomExamples(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def embed(self, ctx: Context) -> None:
        """Sends an embed"""

        embed = discord.Embed(title="Embed", description="This is an embed", color=0x00ff00)
        
        await ctx.send(embed=embed)


    @commands.hybrid_command()
    async def botinfo(self, ctx: Context) -> None:
        """Shows info about the bot"""

        embed = discord.Embed(title="Bot Information", color=0x00ff00)
        embed.add_field(name="Bot Name", value=self.bot.user.name, inline=False)
        embed.add_field(name="Bot ID", value=self.bot.user.id, inline=False)
        embed.add_field(name="Bot Version", value="1", inline=False)

        await ctx.send(embed=embed)


    @commands.hybrid_command()
    async def user_info(self, ctx: Context) -> None:
        """Shows info about the current user"""

        user = ctx.author

        embed = discord.Embed(title="User Information", color=0x00ff00)
        embed.set_author(name=user.name, icon_url=user.avatar.url)
        embed.add_field(name="User Name", value=user.name, inline=False)
        embed.add_field(name="User ID", value=user.id, inline=False)
        embed.add_field(name="User Discriminator", value=user.discriminator, inline=False)

        await ctx.send(embed=embed)


    @commands.hybrid_command()
    async def rps(self, ctx: Context, choice: RPSChoice) -> None:
        """Rock Paper Scissors"""

        bot_choice = random.choice(["rock", "paper", "scissors"])

        await ctx.send(f"Bot chose {bot_choice}, {ctx.author.name} chose {choice}")

        # A dictionary of all the possible winning outcomes
        winner = {
            ("rock", "paper"): self.bot.user,
            ("paper", "scissors"): self.bot.user,
            ("scissors", "rock"): self.bot.user,
            ("rock", "scissors"): ctx.author,
            ("paper", "rock"): ctx.author,
            ("scissors", "paper"): ctx.author,
        }

        winning_user = winner.get((choice, bot_choice)) 

        if winning_user is None:
            await ctx.send("Tie")
        else:
            await ctx.send(f"{winning_user.name} wins")


    @commands.hybrid_command()
    async def coinflip(self, ctx: Context) -> None:
        """Flips a coin"""

        await ctx.send(random.choice(["Heads", "Tails"]))
    

    @commands.hybrid_command()
    async def emoji(self, ctx: Context) -> None:
        """Adds emojis to the message"""

        message = await ctx.send("This is a message with emojis")

        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
    

    @commands.hybrid_command()
    async def calculator(self, ctx: Context, num1: int, operator: str, num2: int) -> None: 
        """Basic Calculator
        
        Parameters 
        ----------
        num1 : int
            The first number
        operator : str
            The operator to use (+, -, *, /)
        num2 : int
            The second number
        """

        result = 0

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
            result = round(result, 2)

        await ctx.send(f"{num1} {operator} {num2} = {result}")


async def setup(bot):
    await bot.add_cog(RandomExamples(bot))