from asyncio.windows_events import NULL
import discord
import io
import aiohttp
from discord import client, guild
from discord import message
from discord.ext import commands
from discord.channel import CategoryChannel
from discord.utils import get
import uuid
import tensorflow as tf
from tensorflow import keras

#keras model info
image_size = (180, 180)
batch_size = 32
model = keras.models.load_model('./trainedmodel')

#token adn server info
TOKEN = '*'
GUILD_ID = '*'

img_types = ['bmp','jpeg','jpg','png', 'PNG', 'BMP', 'JPEG', 'JPG']

#channel and id info
lobby_channel_ID = NULL
lobby_category_ID = NULL
main_chat_ID = NULL
Cole_ID = NULL

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
            if is_lobby_image(message):
                imageName = str(uuid.uuid4()) + '.jpg'
                await message.attachments[0].save("./images2/" + imageName)
                print("downloaded image")

    #checks to see if image to repost
    if is_lobby_category(message) and not is_main_channel(message) and not is_lobbies_channel(message) and is_lobby_image(message):
        img_url = message.attachments[0].url
        lobby_channel = bot.get_channel(lobby_channel_ID)
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await lobby_channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await lobby_channel.send(file=discord.File(data, 'image.png'))
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

def is_lobby_image(message):
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in img_types):
                img = keras.preprocessing.image.load_img( attachment, target_size=image_size)
                img_array = keras.preprocessing.image.img_to_array(img)
                img_array = tf.expand_dims(img_array, 0)  # Create batch axis
                predictions = model.predict(img_array)
                score = predictions[0]
                percent = (100 * (1-score))
                if percent > 99:
                    return True
                return False
            return False
# Run the client on the server
bot.run(TOKEN)