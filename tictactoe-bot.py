import discord
import requests
import json

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hithere"):
        await message.channel.send("im working just fine")
        

        
client.run('ODgyMDgwMTQ5OTYzNjc3NzI2.YS2LKA.L44RVOeu1kOaYLaZptd7sITKHhc')