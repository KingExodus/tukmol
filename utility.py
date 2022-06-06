import discord
from discord.ext import commands
from googletrans import Translator
import datetime
import asyncio

from config import *

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

QUERY_ERROR = commands.CommandError('Query failed, try again later.')

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Utility module successfully imported!")

    @commands.command(aliases=['weather'], description="View weather information")
    async def _weather(self, ctx, *, location: str):
		#Check the weather at a location.

        

        if APIXU_KEY is None:
            raise commands.CommandError('The host has not set up an API key.')
            
        url = 'http://api.weatherstack.com/current'
        params = {
                'access_key': APIXU_KEY,
                'query': location
            }
        
        async with ctx.channel.typing():
            try:
                async with ctx.http.get(url, params=params) as resp:
                    if resp.status != 200:
                        raise QUERY_ERROR
                    data = await resp.json()
            except asyncio.TimeoutError:
                raise QUERY_ERROR

            if data.get('success', True) is False:
                raise commands.CommandError('Unable to find a location match.')

            location = data['location']
            current = data['current']

            observation_time = datetime.strptime(current['observation_time'], '%I:%M %p').time()

            embed = discord.Embed(
				title='Weather for {}, {} {}'.format(location['name'], location['region'], location['country'].upper()),
				description='*{}*'.format(' / '.join(current["weather_descriptions"])),
				timestamp=datetime.combine(datetime.today(), observation_time)
			)

            embed.set_footer(text='Observed')

            if current['weather_icons']:
                embed.set_thumbnail(url=current['weather_icons'][0])

            embed.add_field(name='Temperature', value='{}°C'.format(current['temperature']))
            embed.add_field(name='Feels Like', value='{}°C'.format(current['feelslike']))
            embed.add_field(name='Precipitation', value='{} mm'.format(current['precip']))
            embed.add_field(name='Humidity', value='{}%'.format(current['humidity']))
            embed.add_field(name='Wind Speed', value='{} kph'.format(current['wind_speed']))
            embed.add_field(name='Wind Direction', value=current['wind_dir'])

            await ctx.send(embed=embed)

    @commands.command(aliases=['translate'], description="Translates between languages")
    async def _translate(self, ctx, lang, *, words):
        translator = Translator()
        word = translator.translate(words, dest=lang)
        await ctx.send(word.text)
        #await ctx.send(translator.detect(f'{word}'))

    @commands.command(aliases=['calcu', 'calc', 'compute'], description="Calculates things")
    async def _calcu(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['poll'], description="Sets up a poll in your server.")
    async def _poll(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['addtag'], description="Creates a tag that can be ran to this server")
    async def _addtag(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['edittag'], description="Updates an already made tag")
    async def _edittag(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['removetag'], description="Removes an already made tag")
    async def _removetag(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['tag'], description="Executes a created tag and shows you a list of tags created")
    async def _tag(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(Utility(bot))