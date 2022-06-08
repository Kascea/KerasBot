import Id

img_types = ['bmp','jpeg','jpg','png', 'PNG', 'BMP', 'JPEG', 'JPG']

def main_channel(message):
    if message.channel.id == Id.main_chat_ID:
        return True
    else: return False

def lobby_category(message):
    if message.channel.category.id == Id.lobby_category_ID:
        return True
    else: return False

def lobbies_channel(message):
    if message.channel.id == Id.lobby_channel_ID:
        return True
    else: return False

def cole_command(message):
    if message.author.id == Id.Cole_ID and message.content == "!download":
        return True
    else: return False

def image(message):
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in img_types):
                return True
            return False