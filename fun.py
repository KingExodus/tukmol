import discord
from discord.ext import commands

import requests
import json
import random

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous?blacklistFlags=nsfw,racist&type=single")
  json_data = json.loads(response.text)
  joke = json_data["joke"]
  return (joke)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Fun module successfully imported")

    @commands.command(aliases=['quote'], description="Get inspire from a random quotes")
    async def _quote(self, ctx):
        quote = get_quote()
        embed = discord.Embed(description = quote, color=PRIMARY_COLOR)
        await ctx.send(embed=embed)

    @commands.command(aliases=['joke'], description="Shows a random jokes")
    async def _joke(self, ctx):
        jokes = get_joke()
        embed = discord.Embed(description=jokes, color=PRIMARY_COLOR)
        await ctx.send(embed=embed)

    @commands.command(aliases=['coinflip'], description="Flip a coin")
    async def _coinflip(self, ctx):
        coin = ["Heads", "Tails"]
        await ctx.send(f':coin:  {random.choice(coin)}')

    @commands.command(aliases=['embed'], description="Put text that you specify inside an embed")
    async def _embed(self, ctx, *, message):
        embed = discord.Embed(description = message, color=PRIMARY_COLOR)
        await ctx.send(embed=embed)

    @commands.command(aliases=['say'], description="Make the bot say whatever you want")
    async def _say(self, ctx, *, message):
        await ctx.send(message)

    

def setup(bot):
    bot.add_cog(Fun(bot))