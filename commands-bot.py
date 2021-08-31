import discord
import json
import requests

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def request(ctx):
    await ctx.send('Fetching API request...')
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    await ctx.send(response.json())

        
client.run('ODgyMDgwMTQ5OTYzNjc3NzI2.YS2LKA.L44RVOeu1kOaYLaZptd7sITKHhc')
