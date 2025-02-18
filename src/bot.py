import discord
from discord.ext import commands
import os

# Set the command prefix for the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs from the cogs directory
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# Run the bot with the token
if __name__ == '__main__':
    bot.run('YOUR_BOT_TOKEN')