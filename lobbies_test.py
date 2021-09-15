import discord
import io
import aiohttp
from discord import client, guild
from discord import message
from discord.ext import commands
from discord.channel import CategoryChannel
from discord.utils import get
import uuid
import shutil

TOKEN = 'ODcxOTU4MTI3MDExMDYxNzgw.YQi4SQ.6KHukN1LS6CbJpnZA2KTVfNc948'
GUILD_ID = '871947779298173029'

img_types = ['bmp','jpeg','jpg','png', 'PNG', 'BMP', 'JPEG', 'JPG']

lobby_channel_ID = 871947945908514837
lobby_category_ID = 872304366005157929
main_chat_ID = 876290643020881920
Cole_ID = 243563892242907146

bot = discord.Client()
# Ran when bot connects to discord
@bot.event
async def on_ready():
    print("Connected.")
    guild = bot.get_guild(GUILD_ID)

@bot.event
async def on_message(message):
    #checks to see if download command
    if is_lobbies_channel(message) and is_cole_command(message):
        lobby_channel = bot.get_channel(lobby_channel_ID)
        async for message in lobby_channel.history(limit=500):
            if is_image(message):
                imageName = str(uuid.uuid4()) + '.jpg'
                await message.attachments[0].save("./Pictures/Discordbot/" + imageName)
                print("downloaded image")

    #checks to see if image to repost
    if is_lobby_category(message) and not is_main_channel(message) and not is_lobbies_channel(message) and is_image(message):
        img_url = message.attachments[0].url
        lobby_channel = bot.get_channel(lobby_channel_ID)
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await lobby_channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await lobby_channel.send(file=discord.File(data, 'cool_image.png'))
                await lobby_channel.send("Join <@{}> for <#{}>" .format(message.author.id, message.channel.id))

def is_main_channel(message):
    if message.channel.id == main_chat_ID:
        return True
    else: return False

def is_lobby_category(message):
    if message.channel.category.id == lobby_category_ID:
        return True
    else: return False

def is_lobbies_channel(message):
    if message.channel.id == lobby_channel_ID:
        return True
    else: return False

def is_cole_command(message):
    if message.author.id == Cole_ID and message.content == "download":
        return True
    else: return False

def is_image(message):
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in img_types):
                return True
            return False
# Run the client on the server
bot.run(TOKEN)