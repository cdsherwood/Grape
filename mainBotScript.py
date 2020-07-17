import discord
from discord.ext import commands
import json
import discord.file
import os
import random



baseURL = 'http://www.thebluealliance.com/api/v3/'
header = {'X-TBA-Auth-Key':'(TRLvDFJBpyh7myOiGYwLRggiRnd7BG8rHeW5lcfjcGS4TwqdKBI64vQ45kP0Jjvq )'}

client = commands.Bot(command_prefix='g!')







@client.event
async def on_ready():
    print("The bot is ready.")

@client.command(aliases=[ "Ping," ])
async def ping(ctx):
    await ctx.send(f' Pong!{round (client.latency *1000)} ms test' )














@client.command(aliases=["Hug,"])
async def hug(ctx, id):
    # print(user)
    #userLen = len(user)
    #print(userLen)
    id = id.replace('<', '')
    id = id.replace('>', '')
    id = id.replace('!', '')
    id = id.replace('@', '')
    #print(id)
    #print(user)
    user = str(await client.fetch_user(id))
    userlen = len(user)-5
    print(user)
    user = user[0:userlen]

    author = str(ctx.message.author)
    print(author)
    authLen = len(author)-5
    author = author[0:authLen]

    hugMessage =[
        f'{author} hugs {user}!',
        f'{author} wraps their arms around {user}!',
        f'{author} warmly embraces {user}!',
        f'{author} traps {user} in their arms!'


                 ]


    #await ctx.send(f'{author} hugs {user}!')
    await ctx.send(random.choice(hugMessage))










client.run('NjgyNjkzNDI3MTcxMDMzMTU3.XlgvVQ.hxHQbrTBTt0s7FyjZGQBdEPdDrQ')
