import discord 
from Id import Id
from discord.ext import commands

def main():
    MW2Bot = commands.Bot(command_prefix='!')
    MW2Bot.load_extension("Events")
    MW2Bot.load_extension("Commands")
    MW2Bot.run(Id.TOKEN)

if __name__ == "__main__":
    main()

