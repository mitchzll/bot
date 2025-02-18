import discord
from discord.ext import commands
import os

# Set the command prefix for the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs from the cogs directory
async def load_cogs():
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded extension: {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')
    await load_cogs()

# Run the bot with the token
if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        bot.run(token)
    else:
        print("Error: DISCORD_BOT_TOKEN environment variable not set.")