from Id import Id

img_types = ['bmp','jpeg','jpg','png', 'PNG', 'BMP', 'JPEG', 'JPG']

def main_channel(message):
    if message.channel.id == Id.Main_chat_ID:
        return True
    else: return False

def lobby_category(message):
    if message.channel.category.id == Id.Lobby_category_ID:
        return True
    else: return False

def lobbies_channel(message):
    if message.channel.id == Id.Lobby_channel_ID:
        return True
    else: return False

def image(message):
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in img_types):
                return True
            return False