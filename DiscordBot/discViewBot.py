import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension('cogs.{}'.format(filename[:-3]))

async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())