import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "!", description = "Bot")
status = ["!help"]

@bot.event
async def on_ready():
    print("Ready !")
    changeStatus.start()

@bot.command()
async def start(ctx, secondes = 5):
    changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.dnd, activity = game)

bot.run("Njg1OTQ5MzM2NDExOTYzNTYw.GQzx9G.id5-TrlW0AoBQ1NrJ4-ryKHpsT-O8dAFyxc5Po")
