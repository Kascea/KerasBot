import discord
import Global
from Id import Id
import io
import aiohttp

def setup(bot):
    @bot.event
    async def on_ready():
        print("Connected.")
        guild = bot.get_guild(Id.GUILD_ID)

    @bot.event
    async def on_message(message):
        if image_repostable(message):
            #repost image
            img_url = message.attachments[0].url
            lobby_channel = bot.get_channel(Id.Lobby_channel_ID)
            async with aiohttp.ClientSession() as session:
                async with session.get(img_url) as resp:
                    if resp.status != 200:
                        return await lobby_channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await lobby_channel.send(file=discord.File(data, 'cool_image.png'))
                    await lobby_channel.send("Join <@{}> for <#{}>" .format(message.author.id, message.channel.id))

def image_repostable(message):
    if Global.lobby_category(message) and not Global.main_channel(message) and not Global.lobbies_channel(message) and Global.image(message):
        return True
        
