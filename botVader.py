import os
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f"{client.user} has connected to: {guild.name}. Guild id: {guild.id}")

@client.event
async def on_member_join(member):
    guild = member.guild
    await member.create_dm()
    to_send = f"{member.name} welcome to {guild.name}. You're stuck here forever or shorter."
    await member.dm_channel.send(to_send)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "there is no escape" or message.content == "There is no escape":
        response = "Don't make me destroy you."
        await message.channel.send(response)

    if message.content == "Luke you do not yet realize your importance." or message.content == "Luke, you do not yet realize your importance.":
        response = "You have only begun to discover your power. Join me and I will complete your training."
        await message.channel.send(response)



client.run(TOKEN)
