import discord 
from discord.ext import commands
import os 

BOT_TOKEN = os.environ.get("DISCORD_TOKEN")
# BOT_TOKEN = "YOUR_TOKEN_HERE"

class MyClient(commands.Bot):
    def __init__(self, **options):
        # Call the parent class init and pass in the options
        super().__init__(**options)


    # on_ready is called when the bot has finished logging in and setting things up
    async def on_ready(self):
        print(f'Logged on as {self.user}')

        print("Loading extensions...")
        await self.load_cogs()


    # on_message is called whenever a message is sent in a channel that the bot can see
    # This event is not exclusive to users messages, but also includes messages sent by bots
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Process commands if the message is a command
        await self.process_commands(message)
        

    # Load all cogs in the cogs folder
    async def load_cogs(self):
        # Get the path of the cogs folder
        cogs_path = os.path.dirname(os.path.realpath(__file__)) + "/cogs"

        extensions = []
        # Loop through all files in the cogs folder and add them to the extensions list
        for filename in os.listdir(cogs_path):
            if filename.endswith(".py"):
                # The extension is the path to the file without the .py extension
                extension = f"cogs.{filename[:-3]}"
                extensions.append(extension)

        # Load all extensions
        for extension in extensions:
            try:
                await self.load_extension(extension)
                print(f"Loaded extension {extension}")
            except Exception as e:
                print(f"Failed to load extension {extension}")
                print(f"{type(e).__name__}: {e}")


intents = discord.Intents.default() # The default intents for your bot
intents.message_content = True # Whether to receive messages
command_prefix = "!" # The prefix for your bot commands

client = MyClient(intents=intents, command_prefix=command_prefix)
client.run(BOT_TOKEN)

                