import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time 
from discord.utils import get

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot('!', case_insensitive = True, intents = intents)

admin = "👻 MOD"

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
    description = "- !comandos\n- !perfil\n- !play\n- !sair",
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
  embed = discord.Embed(
    title = f"Perfil de {ctx.author.global_name}",
    description = "Entrou no servidor ...",
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

# !apagar
                    # CORRIGIR ERRO SE NÃO FOR MOD #
@client.command()
@commands.has_any_role(admin)
async def apagar(ctx, amount:str):
  if amount == "tudo":
    await ctx.channel.purge()
  else: 
    await ctx.channel.purge(limit=(int(amount) + 1))

# COMANDOS YT / MUSICA
@client.command()
async def join(ctx, ags):
  try:
    call = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
      await voice.move_to(call)
    else:
      voice = await call.connect()
      await discord.send_audio_packet(ags, encode=True)
  except AttributeError:
    await ctx.channel.send("Você precisa esta conectado a um canal de voz.")

@client.command()
async def play(ctx, ags):
  try:
    call = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
      await voice.move_to(call)
    else:
      voice = await call.connect()
      await discord.send_audio_packet(ags, encode=True)
  except AttributeError:
    await ctx.channel.send("Você precisa esta conectado a um canal de voz.")

@client.command()
async def pause(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")
  

@client.command()
async def resume(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")

@client.command()
async def stop(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")

@client.command()
async def sair(ctx):
  try:
    voice = get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()
  except AttributeError:
    await ctx.channel.send("O bot não esta conectado em nenhum canal de voz.")
   
@client.command()
async def test(ctx):
  print(ctx.voice_client)

client.run(TOKEN)