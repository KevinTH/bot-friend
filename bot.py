import discord

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

client.run(ODk2NTA3NzQzMjg3MDA5MzEx.YWIH5g.gRpFiq0E82Rog6XEj5zHoPvXF1w)