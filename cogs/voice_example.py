import os 
import discord
from discord.ext import commands
from discord.ext.commands import Context

class VoiceExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def join(self, ctx: Context) -> None:
        """Joins the voice channel the user is currently in"""

        # Check if the user is in a voice channel
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
            return

        # Check if the bot has permission to connect to the voice channel
        permission = ctx.author.voice.channel.permissions_for(ctx.guild.me).connect
        if not permission:
            await ctx.send("I do not have permission to connect to that voice channel")
            return

        # Check if the bot is already in a voice channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
            await ctx.author.voice.channel.connect()
    
    
    # Must have ffmpeg installed and added to PATH environment variable
    @commands.command()
    async def play(self, ctx: Context) -> None:
        """Plays a sound file in the voice channel the bot is currently in"""

        # join the voice channel if the bot is not already in one
        if ctx.voice_client is None:
            await self.join(ctx)

             # Check if bot successfully joined a voice channel
            if ctx.voice_client is None: 
                return
       
        # Get the path to the sound file
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(curr_dir)
        audio_file_path = parent_dir + "/media/ElevatorMusic.mp3"

        # Create a discord.FFmpegPCMAudio object from the sound file
        player = discord.FFmpegPCMAudio(audio_file_path)

        # Play the sound file
        ctx.voice_client.play(player, after=lambda e: print("done"))


    @commands.command()
    async def leave(self, ctx: Context) -> None:
        """Leaves the voice channel the bot is currently in"""

        # Check if the bot is in a voice channel
        if ctx.voice_client is None:
            await ctx.send("I am not in a voice channel")
            return

        await ctx.voice_client.disconnect()


async def setup(bot):
    await bot.add_cog(VoiceExample(bot))