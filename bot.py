# discord.py 모듈 import
import discord

# 토큰
token = ""

# 클라이언트
client = discord.Client()

# 봇이 작동 시작 시 console에 Log in 출력
@client.event
async def on_ready():
    print("Log in")