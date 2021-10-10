import discord
import os

print(os.getenv('TOKEN'))

client = discord.Client()

@client.event
async def on_ready():
    print('User is'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$world'):
        await message.channel.send('World!')

client.run(os.getenv('TOKEN'))