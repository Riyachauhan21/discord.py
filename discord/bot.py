
import discord
import os
from discord import client
from discord import message

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
        
client.run(os.getenv('TOKEN'))       

 