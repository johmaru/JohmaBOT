import asyncio
import os
from turtle import delay
from bardapi import Bard
import discord
from discord import app_commands
from discord.ext import commands
import json
import urllib.error
import urllib.request


class GetImageAI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
      await self.bot.tree.sync()
      print('Working get_image command')


    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name = "get_image", description = "画像を送ってもらおう！")
    async def get_image(self,interaction: discord.Interaction, text:str):
     try:
      await interaction.response.defer()
      with open('token.json', 'r') as f:
       ps_data = json.load(f)
       psid_token = ps_data[1]['1PSID']
      bard = Bard(token=psid_token)
      answer = bard.get_answer(text)
      await asyncio.sleep(1)
      image = answer['images']
      unpack = tuple(image)
      await interaction.followup.send(unpack[0])
     except Exception as e:
      print(e)
      if e == "tuple index out of range":
          await interaction.followup.send("{0} 日本語を使用できません。 申し訳ないですが英語でお願い致します。".format(e))
      if e != "tuple index out of range":
       await interaction.followup.send("想定外のエラーが発生しました。{0}".format(e))


async def setup(bot: commands.Bot):
 await bot.add_cog(GetImageAI(bot))