
# Discord Bot

An Discord bot featuring example commands built using the [discord.py](https://github.com/Rapptz/discord.py) library.

## Featured examples

- Cogs
- prefix and slash commands
- Buttons
- Error handling
- Voice playback

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- [discord.py](https://github.com/Rapptz/discord.py) 2.0 or higher
- [Discord API token](https://discord.com/developers/docs/intro) - You will need to create a bot account and get the API token in order to run the bot. Make sure the following are additionally ticked to ensure every feature works:
    - `applications.commands` Under OAUTH2
    - `PRESENCE INTENT` Under Bot
    - `SERVER MEMBERS INTENT` Under Bot
    - `MESSAGE CONTENT INTENT` Under Bot
- [FFMPEG](https://ffmpeg.org/) - You will need this installed and added to your PATH environment variable to use voice playback functions

### Installing

1. Clone the repository
`git clone https://github.com/ChrisLie45/Discord-Bot-Example.git`

2. Install the dependencies
`pip install -r requirements.txt`

3. Replace `YOUR_TOKEN_HERE` in `bot.py` with your Discord API token. Alternatively, you can also uncomment `BOT_TOKEN = os.environ.get("DISCORD_TOKEN")` above and use that to initialize your token if you have an environment variable setup. 

4. Run the bot
`python bot.py`

## Slash Commands

In order to use slash commands, you must first sync them. To sync, you can use the `sync` command that comes with the bot. To sync commands globally, pass in `g` as an argument for the command and to sync to the current guild, dont pass in any argument.

You will not need to do this to use prefix commands.

## Deployment

- You can use a service like [Heroku](https://www.heroku.com/) to deploy your bot. While no longer free, it still offers student for up to $156 USD. However i have had trouble getting consistent voice playback working on the platform recently.

## Acknowledgments

- [discord.py documentation](https://discordpy.readthedocs.io/en/latest/index.html) - Excellent resource for learning how to use the library
- [Discord API documentation](https://discord.com/developers/docs/intro) - Comprehensive documentation for the Discord API
- [Button examples](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - Comprehensive guide and examples for buttons
- [Error handler example](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handler example used in this project