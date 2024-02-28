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

admin = "MOD"

@client.event
async def on_ready():
  print(f'Iniciado')

# Evendo de boas vindas.
@client.event
async def on_member_join(self):
  canalbemvindo = client.get_channel(1211027616845271150)
# Pegando o cargo
  role = self.guild.get_role(1211106560869408838)
  mensagem = await canalbemvindo.send(f"{self.mention} bem vindo ao {self.guild}.")
  await self.add_roles(role)

# !comandos
@client.command()
async def comandos(ctx):
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
  mensagem = await ctx.channel.send(embed=embed)
  time.sleep(10)

# !perfil
@client.command()
async def perfil(ctx):
# !perfil
  embed = discord.Embed(
    title = f"Perfil de {ctx.author.global_name}",
    description = "Esse é o seu perfil",
    color = 0x993399
  )
  roles = ""
  for role in ctx.author.roles:
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
    url=ctx.author.avatar.url
  )
  embed.set_footer(
    text="created by Kinz015",
    icon_url=client.user.avatar.url
  )
  await ctx.channel.send(embed=embed)

@client.command()
@commands.has_any_role(admin)
async def apagar(ctx, amount:str):
  if amount == "tudo":
    await ctx.channel.purge()
  else: 
    await ctx.channel.purge(limit=(int(amount) + 1))

client.run(TOKEN)