import discord
import os

client = discord.Client()

def is_image(attachment):
    return attachment.height != None

async def add_reaction(message):
    await message.add_reaction('⬆')
    await message.add_reaction('⬇')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if len(message.attachments) == 0:
        return

    for attachment in message.attachments:
        if is_image(attachment):
            await add_reaction(message)

client.run(os.getenv("DISCORD_TOKEN"))
