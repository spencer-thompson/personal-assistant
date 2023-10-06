"""
WIP! Current functionality includes ChatGPT integration.

The bot is currently in my test server and will be rolled out to Google Developers soon.

Requirements: Discord bot with 'bot' scopes, bot added to server, and bot token_id
"""
import discord
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, r'C:\Users\Laptop Checkout\OneDrive - Utah Valley University\Personal-Assistant\personal-assistant\src')
from gpt import GPT

load_dotenv()

ai = GPT()

intents = discord.Intents.default()
# Allows bot to read messages
intents.message_content = True
# Allows bot to edit members (used for roles)
intents.members = True
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
    

    embed = discord.Embed(
            title='GPT:',
            description=f'{response}',
            color=discord.Colour.green()
        )
    await message.channel.send(embed=embed)
    # Sends message through bot to channel input was sent through
    # await message.channel.send(response)
    
# Message ID in my private disc server
# When reaction added, role given
target_message_id = 1156079576401850450

# 'On message reaction'
@client.event
async def on_raw_reaction_add(payload):
    """
    Give a role based on reaction emoji
    """

    if payload.message_id != target_message_id:
        return

    guild = client.get_guild(payload.guild_id)

    if payload.emoji.name == '🥔':
        role = discord.utils.get(guild.roles, name='Potato')
        await payload.member.add_roles(role)
    elif payload.emoji.name == '💩':
        role = discord.utils.get(guild.roles, name='Chocolate ;)')
        await payload.member.add_roles(role)
    elif payload.emoji.name == '🐒':
        role = discord.utils.get(guild.roles, name='monkey')
        await payload.member.add_roles(role)

# 'On reaction removal'
@client.event
async def on_raw_reaction_remove(payload):
    """
    Remove a role b ased on a reaction emoji
    """

    if payload.message_id != target_message_id:
        return

    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name == '🥔':
        role = discord.utils.get(guild.roles, name='Potato')
        await member.remove_roles(role)
    elif payload.emoji.name == '💩':
        role = discord.utils.get(guild.roles, name='Chocolate ;)')
        await member.remove_roles(role)
    elif payload.emoji.name == '🐒':
        role = discord.utils.get(guild.roles, name='monkey')
        await member.remove_roles(role)





client.run(os.getenv('bot_token'))