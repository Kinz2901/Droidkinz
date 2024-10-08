class CommandsBan:
  def __init__(self, ctx, member, reason=None):
    self.ctx = ctx
    self.member = member
    self.reason = reason

  async def ban(self):
    mod = self.ctx.message.author
    channel = self.ctx.channel
    try: 
      msg = f"{self.member.mention} foi banido por {mod.mention}\nMotivo: {self.reason}" 
      await self.member.ban()
      await channel.send(msg)
    except:
      msg = f"Se coloque no seu lugar {mod.mention}."
      await channel.send(msg)