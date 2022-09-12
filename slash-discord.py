import discord
from discord import app_commands
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import random
import requests
from discord.ext import commands
from discord_buttons_plugin import  *
import asyncio, discord
import discord, datetime
import interactions
from discord.ext import tasks
from itertools import cycle
import os



class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('이지봇')          # ~~ 하는중
        await self.change_presence(status=discord.Status.online, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)












@tree.command(name = '따라하기',description='이지가 대화를 따라 할 수 있다')
async def slash2(interaction: discord.Interaction, 말: str):

    if 말 == "안녕":
        await interaction.response.send_message("안녕") 
    await interaction.response.send_message("{}".format(말)) 

@tree.command(name = '대화하기', description='이지와 대화를 할 수 있다') 
async def slash2(interaction: discord.Interaction, 할말: str):
    if 할말 == "안녕":
        interaction = await interaction.channel.send("안녕")
        await asyncio.sleep(1)
        await interaction.edit(content="뭐라고?")

    if 할말 == "ㅎㅇ":
        await interaction.response.send_message("ㅎㅇㅎㅇ") 
    
    if 할말 == "ㅂㅇ":
        await interaction.response.send_message("ㅂㅇㅂㅇ") 

    if 할말 == "잘가":
        await interaction.response.send_message("잘가...") 



@tree.command(name = '안녕', description='슬래시 설명문') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"슬래시 커맨드") 


@tree.command(name = '임베드', description='임베드 기초') 
async def slash2(interaction: discord.Interaction):
    embed = discord.Embed(title="큰 제목", description="조금 작은 제목", color=0x4000FF) #큰 제목과 작은 제목을 보여준다
    embed.add_field(name="아아아아", value="오오오오", inline=False) #작은 제목과 작은제목의 설명
    await interaction.response.send_message(embed=embed)





@tree.command(name = '문의', description = '봇을 통해 문의를 할 수 있습니다') 
async def slash2(interaction: discord.Interaction, 문의: str):

    
    embed = discord.Embed(title="📑 봇 문의 📑", description="ㅤ", color=0x4000FF) 
    embed.add_field(name="봇 문의가 접수되었습니다", value="ㅤ", inline=False)
    embed.add_field(name="문의 내용", value="```fix\n{}\n```".format(문의), inline=False) 
    embed.add_field(name="ㅤ", value="**▣ 문의 내용에 대한 답장은 관리자가 확인후\n24시간 내에 답장이 오니 기다려 주시면 감사하겠습니다**", inline=False) 
    embed.add_field(name="ㅤ", value="- **white_waffle (화이프)** -", inline=False) 
    embed.set_thumbnail(url="https://imgur.com/sJqXNLW.jpeg")
    embed.set_author(name="이지봇",
    url="https://www.youtube.com/channel/UCqn6PVL-JHe_8HQUnKkiacg",
    icon_url="https://imgur.com/jtXT6b3.jpeg")
    await interaction.response.send_message(embed=embed)
    
    



    users = await client.fetch_user("786487900291596328")
    await users.send("유저 아이디 {}  / 문의 내용 {}".format(interaction.user.id, 문의))





@tree.command(name = '문의답변', description = '봇을 통해 문의에 답변을 할 수 있습니다') 
async def slash2(interaction: discord.Interaction, 아이디: str, 답변: str):

    embed = discord.Embed(title="📑 봇 답변 📑", description="ㅤ", color=0x4000FF) 
    embed.add_field(name="문의에 대한 답변 내용", value="{}".format(답변) , inline=False) 



    await interaction.response.send_message(f"✅") 



    user = await client.fetch_user("{}".format(아이디))
    await user.send(embed=embed)
