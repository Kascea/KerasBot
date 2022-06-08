import discord
from Global import GUILD_ID
from Global import lobby_channel_ID
from Global import lobbies_channel
from Global import lobby_category
from Global import main_channel
from Global import image
from App import MW2Bot
import io
import aiohttp

@MW2Bot.event
async def on_ready():
    print("Connected.")
    guild = MW2Bot.get_guild(GUILD_ID)

@MW2Bot.event
async def on_message(message):
    if image_repostable:
        repost_image(message)

async def image_repostable(message):
    if lobby_category(message) and not main_channel(message) and not lobbies_channel(message) and image(message):
        return True

async def repost_image(message):
    #checks to see if image to repost
        img_url = message.attachments[0].url
        lobby_channel = MW2Bot.get_channel(lobby_channel_ID)
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await lobby_channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await lobby_channel.send(file=discord.File(data, 'cool_image.png'))
                await lobby_channel.send("Join <@{}> for <#{}>" .format(message.author.id, message.channel.id))
