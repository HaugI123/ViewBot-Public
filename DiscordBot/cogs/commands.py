import subprocess
import validators
import discord
from discord.ext import commands, tasks
from time import sleep

def localCommand(command):
    '''Opens a new terminal instance and runs a given command and returns the output of the command'''
    result = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command], stderr=subprocess.STDOUT, stdout=subprocess.PIPE) 

def checkPythonFile(file):
    '''Returns a boolean based on if a python file is running'''
    result = subprocess.check_output('pgrep -a python', shell=True).decode('utf-8')
    splitResult = result.split('\n')
    for value in splitResult:
        if value.find('python {}'.format(file)) > -1:
            return value
    else:
        return False

class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_role('ITK')
    @commands.guild_only()
    async def resetStatus(self, ctx):
        '''Sets the discord bot's status to idle'''
        await self.client.change_presence(activity=None, status=discord.Status.idle)
        await ctx.send('Set to idle status')
        
    @commands.command()
    @commands.has_role('ITK')
    @commands.guild_only()
    async def ViewBot(self, ctx, url, lengthOnPage: int, views: int):
        '''Runs a viewbot for a specified URL.'''
        global checkOutput
        if url.find('https://') == -1:
            url = 'https://{}'.format(url)
        urlValidator = validators.url(url)
        if not urlValidator:
            await ctx.send('Invalid URL')
            return
        await self.client.change_presence(activity=discord.Game('Sending views to {}'.format(url)), status=discord.Status.online)
        cmd = 'cd ..; python3 viewBot.py'
        with open('urlList.py', 'w') as file:
            file.write('url = "{}"\nlengthOnPage = {}\nviews = {}'.format(url, lengthOnPage, views))
        await ctx.send('Now trying to send {} views to {}'.format(views, url))
        test = localCommand(cmd)
        sleep(3)
        
        checkOutput.start()
        
        @tasks.loop(seconds=lengthOnPage)
        async def checkOutput():
            result = checkPythonFile('viewBot.py')
            if result == False:
                await self.client.change_presence(activity=None, status=discord.Status.idle)
                await ctx.send('Finished sending {} views to {}'.format(views, url))
                checkOutput.cancel()
        
    @commands.command()
    @commands.has_role('ITK')
    @commands.guild_only()
    async def Stop(self, ctx):
        '''Stops the viewbot from running'''
        result = checkPythonFile('viewBot.py')
        if result != False:
            pythonFile = result.split(' ')
            pid = pythonFile[0]
            killCmd = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'kill {}'.format(pid)], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            await ctx.send('The viewbot has been stopped.')
            await self.client.change_presence(activity=None, status=discord.Status.idle)
            checkOutput.cancel()
        elif result == False:
            await ctx.send('ViewBot is not running.')

    @commands.command('Ping')
    async def Ping(self, ctx):
        '''Returns the value pong to the discord server'''
        await ctx.send('Pong! {}ms'.format(round(self.client.latency * 1000, 2)))
        
    @commands.command()
    @commands.has_role('ITK')
    async def Check(self, ctx):
        '''Checks if the viewbot is running'''
        checkValue = checkPythonFile('viewBot.py')
        if checkValue != False:
            await ctx.send('ViewBot is actively running.')
        else:
            await ctx.send('ViewBot is not active.')
            await self.client.change_presence(activity=None, status=discord.Status.idle)

async def setup(client):
    '''Adds the cogs to the discord client'''
    await client.add_cog(Commands(client))
