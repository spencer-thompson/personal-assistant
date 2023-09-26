import discord
from dotenv import load_dotenv
import os
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
async def on_message(mess):
    # Ignores messages by bot to avoid repeated sending of messages
    if mess.author == client.user:
        return
    
    user_input = mess.content
    response = ai.run(user_input)
    print(response)

    # Sends message through bot to channel input was sent through
    await mess.channel.send(response)



client.run(os.getenv('bot_token'))