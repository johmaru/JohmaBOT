import os
import json
from tracemalloc import start
import discord
from discord.ext import commands
import asyncio

INITIAL_EXTENSIONS = [
    'cogs.talk_and_question',
    'cogs.get_image',
    ]

try:
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='??',intents=intents)
except Exception as  e:
    print(e)
 
if os.path.exists('token.json') :
    pass
else :
    check_token = {'token': 'plz replace tihs text'}
    check_1PSID = {'1PSID': 'plz replace tihs text'}
    with open('token.json', 'w') as f:
     jsondata = [check_token, check_1PSID]
     json.dump(jsondata, f, indent=2)
     print('token.json created plz edit it file. file location is RootDirectory/token.json\r\n')
     exit()

@bot.event
async def on_ready():
    print(f'complete logging in! {bot.user}')
    try:
         await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$こんにちは'):
        await message.channel.send('こんにちは！')

with open('token.json', 'r') as f:
     data = json.load(f)
bot_token = data[0]['token']
try:
 async def load_extension():
  for cog in INITIAL_EXTENSIONS:
   await bot.load_extension(cog)
except Exception as  e:
    print(e)

async def main():
 async with bot:
  await load_extension()
  await bot.start(bot_token)
try:
   asyncio.run(main())
except Exception as e:
    print(e)
    exit()