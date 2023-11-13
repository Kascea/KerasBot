from dotenv import load_dotenv
import os

dotenv_path = '/Users/colecarlson/Code/KerasBot/config.env'
load_dotenv(dotenv_path)

class Id:
    Main_chat_ID = int(os.getenv("MAIN_CHAT_ID"))
    Lobby_channel_ID = int(os.getenv("LOBBY_CHANNEL_ID"))
    Lobby_category_ID = int(os.getenv("LOBBY_CATEGORY_ID"))
    Cole_ID = int(os.getenv("COLE_ID"))
    TOKEN = os.getenv("TOKEN")
    GUILD_ID = int(os.getenv("MW2_SERVER_ID"))