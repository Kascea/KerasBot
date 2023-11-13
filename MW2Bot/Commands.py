import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello, world!')
