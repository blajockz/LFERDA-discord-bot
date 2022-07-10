import discord
from discord.ext import commands 

client = commands.bot(command_prefix = ".")

@client.event
async def on_ready():
  print("Bot successfully connected")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

client.run("Njg1OTQ5MzM2NDExOTYzNTYw.GQzx9G.id5-TrlW0AoBQ1NrJ4-ryKHpsT-O8dAFyxc5Po")
