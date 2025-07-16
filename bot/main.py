import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} ({bot.user.id})')

# Load cogs
initial_extensions = ['bot.cogs.poker']
for ext in initial_extensions:
    bot.load_extension(ext)

bot.run(BOT_TOKEN)
