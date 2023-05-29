import discord
from discord import app_commands
from discord.ext import commands
from bardapi import Bard
import json

class Talk_and_question(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
      await self.bot.tree.sync()
      print('Working talk_and_question command')


    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name = "talk_and_question", description = "AIと話をしよう！")
    async def talk_and_question(self,interaction: discord.Interaction, text:str):
     try:
      await interaction.response.defer()
      with open('token.json', 'r') as f:
       ps_data = json.load(f)
       psid_token = ps_data[1]['1PSID']
      bard = Bard(token=psid_token)
      answer = bard.get_answer(text)
      await interaction.followup.send(answer['content'])
     except Exception as e:
      await interaction.response.send_message("エラーが発生しました。")
      await interaction.response.send_message.send(e)


async def setup(bot: commands.Bot):
 await bot.add_cog(Talk_and_question(bot))