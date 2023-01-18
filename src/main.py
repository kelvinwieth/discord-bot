import os
from dotenv import load_dotenv

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())


@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name = "ping", description = "Answers with pong!")
async def ping_async(interaction):
    await interaction.response.send_message("Pong!")


load_dotenv()
token = os.getenv('MY_TOKEN')
bot.run(token)
