import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot('!', case_insensitive = True, intents = intents)

@client.event
async def on_ready():
  print(f'Iniciado')

# Evendo de boas vindas.
@client.event
async def on_member_join(member):
  canalbemvindo = client.get_channel(1211027616845271150)
  mensagem = await canalbemvindo.send(f"{member.mention} bem vindo mamaco.")

# Evento de comandos
@client.event
async def on_message(message):
  if message.content == "!teste": 
    await message.channel.send(f"Testado!")

client.run(TOKEN)