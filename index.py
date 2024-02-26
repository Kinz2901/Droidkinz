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
  # Pegando o canal de boas vindas
  canalbemvindo = client.get_channel(1211027616845271150)
  # Pegando o cargo
  role = member.guild.get_role(1211106560869408838)
  mensagem = await canalbemvindo.send(f"{member.mention} bem vindo mamaco.")
  await member.add_roles(role)

# Evento de comando
@client.event
async def on_message(message):
  if message.content == "!comandos":
    # Criar uma embed
    embed = discord.Embed(
      title = "Lista de Comandos:",
      description = "- !comandos\n- !teste\n- !teste2\n- !teste3\n- !teste4\n- !teste5\n- !teste6",
      color = 0xffff00
    )
    embed.set_footer(
      text="create by Kinz015",
      icon_url="https://pics.craiyon.com/2023-11-13/uMOzhnlCSe2Ri4P0kpR6-A.webp"
    )
    await message.channel.send(embed=embed)
    
  elif message.content == "!teste": 
    await message.channel.send(f"Testado!")


client.run(TOKEN)