"""
WIP! Current functionality includes ChatGPT integration.

The bot is currently in my test server and will be rolled out to Google Developers soon.

Requirements: Discord bot with 'bot' scopes, bot added to server, and bot token_id
"""
import discord
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, '../src')
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
    print(f'Current model: {ai._model}\n'
          f'GPT: {response}')

    # Sends message through bot to channel input was sent through
    await message.channel.send(f'GPT: \n'
                               f'{response}')



client.run(os.getenv('bot_token'))