import discord
import json
import requests

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def request(ctx, arg1):
    await ctx.send('Fetching API request...')
    url = "https://612d6bcae579e1001791db78.mockapi.io/games/"
    response = requests.get(url)
    json_data = response.json()
    boardID = str(arg1)
    
    for i in range(8):
        if json_data[i]['id'] == boardID:
           embed = discord.Embed(
               title= "Board #" + json_data[i]['board'],
                description="ID #" + json_data[i]['id'],
               )
           embed.add_field(name="Player ID", value= json_data[i]['player'])
           embed.add_field(name="Winner #", value= json_data[i]['winner'])
           await ctx.send(embed=embed )
        
client.run('Bot token here')
