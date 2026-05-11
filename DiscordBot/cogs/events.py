import discord
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        '''Prints to the terminal that the bot is connected.'''
        await self.client.change_presence(status=discord.Status.idle)
        guild = discord.utils.get(self.client.guilds, name=GUILD)  
        print('''{} has connected to the following server.\n{} (id:{})'''.format(self.client.user, guild.name, guild.id))
    
    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        '''If discord.DiscordException is raised, outputs the error to err.log'''
        with open('err.log', 'a') as file:
            if event == 'on_ready':
                file.write('Unhandled message: {}: {}\n'.format(args[0], datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                raise
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''If @command.command is not met by the user, throws an error and writes to err.log'''
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send(error)
            with open('err.log', 'a') as file:
                file.write('{}: {}: {} \n'.format(error, ctx.author, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        
        if isinstance(error, commands.CommandNotFound):
            '''Throws an error if the command does not exist'''
            await ctx.send('Command not found')
            with open('err.log', 'a') as file:
                file.write('{}: {}: {} \n'.format(error, ctx.author, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        
        if isinstance(error, commands.MissingRequiredArgument):
            '''Throws an error if an argument is missing'''
            await ctx.send('Missing argument(s) for the command. Check .help <command> to see required arguments.')
            with open('err.log', 'a') as file:
                file.write('{}: {}: {} \n'.format(error, ctx.author, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

async def setup(client):
    await client.add_cog(Events(client))