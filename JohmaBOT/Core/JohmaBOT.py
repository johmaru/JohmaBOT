import os
import json
from bardapi import Bard
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
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

with open('token.json', 'r') as f:
 ps_data = json.load(f)
 psid_token = ps_data[1]['1PSID']

@bot.event
async def on_ready():
    print(f'complete logging in! {bot.user}')
    try:
         await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.tree.command(name="talk_and_question", description="AIと話をしよう！")
async def talk_and_question(interaction: discord.Interaction, text:str):
 try:
  
  await interaction.response.defer()
  bard = Bard(token=psid_token)
  answer = bard.get_answer(text)
  await interaction.followup.send(answer['content'])
 except Exception as e:
  await interaction.response.send_message("エラーが発生しました。")
  await interaction.response.send_message.send(e)

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
   bot.run(bot_token)
except Exception as e:
    print(e)
    exit()