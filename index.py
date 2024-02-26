import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time 

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
      description = "- !comandos\n- !perfil",
      color = 0xffff00
    )
    embed.set_author(
      name=client.user.name, 
      icon_url=client.user.avatar.url)
    embed.set_footer(
      text="created by Kinz015",
      icon_url=client.user.avatar.url
    )
    await message.channel.send(embed=embed)

  elif message.content == "!perfil":
    print(message)
    embed = discord.Embed(
      title = f"Perfil de {message.author.global_name}",
      description = "Esse é o seu perfil",
      color = 0x993399
    )
    roles = ""
    for role in message.author.roles:
      if role.name != "@everyone":
        roles = f"- {role.mention}\n" + roles
    embed.add_field(
        name="Tags:",
        value=roles,
        inline= False
      )
    embed.set_author(
      name=client.user.name, 
      icon_url=client.user.avatar.url)
    embed.set_image(
      url=message.author.avatar.url
    )
    embed.set_footer(
      text="created by Kinz015",
      icon_url=client.user.avatar.url
    )
    await message.channel.send(embed=embed)

  elif message.content == "!teste": 
    await message.channel.send(f"Testado!")


client.run(TOKEN)