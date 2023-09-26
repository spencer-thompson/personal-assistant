"""
WIP! Current functionality includes ChatGPT integration.

The bot is currently in my test server and will be rolled out to Google Developers soon.

Requirements: Discord bot with 'bot' scopes, bot added to server, and bot token_id
"""
import discord
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, '..')
# Currently, "gpt.py" needs to be changed to "gpt1.py" to run. Otherwise it will pull from the incorrect "gpt.py" file.
from gpt import GPT

load_dotenv()

ai = GPT()

intents = discord.Intents.default()
# Allows bot to read messages
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Client is Online')

# AI communication testing
@client.event
async def on_message(message):
    # Ignores messages by bot to avoid repeated sending of messages
    if message.author == client.user:
        return
    
    user_input = message.content
    response = ai.run(user_input)
    print(response)

    # Sends message through bot to channel input was sent through
    await message.channel.send(response)



client.run(os.getenv('bot_token'))