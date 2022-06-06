import discord
from discord.ext import commands

import requests
import json
from random import choice

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

all_tokens = requests.get("https://api.coingecko.com/api/v3/coins/list")
all_tokens_json = all_tokens.json()

unknown_coin = ["Unknown coin.", "Coin not found.", "Invalid coin."]
unknown_coin_2 = ["Please try again", "Invalid input"]

def repsonse_to_string(response):
  data = {}
  data[
    'status_maintenance'] = ':green_circle: No Maintenance' if not response[
    'status_maintenance'] else ':red_circle: Maintenance undergoing'
  data['status_battles'] = get_battle_status(response['status_battles'])
  data['status_graphql'] = ':green_circle: Game servers OK' if response[
    'status_graphql'] else ':red_circle: Game servers Offline'
  data['status_cloudflare'] = ':green_circle: Marketplace OK' if response[
    'status_cloudflare'] else ':red_circle: Marketplace Offline'
  return data

def get_battle_status(status):
  if (status == 0): return ':green_circle: Battle servers OK'
  if (status == 1):
    return ':yellow_circle: Battle servers running with restrictions'
  if (status == 2): return ':black_circle: Battle servers offline'
  else: return ':red_circle: Undefined Status'

def usage_msg(cmd, usage):
  return '**Usage**: {0} {1}'.format(cmd, usage)

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Crypto module successfully imported!")

    @commands.command(aliases=['axiestats'], description="Display game/server status of axie infinity ")
    async def _axiestats(self, ctx):
        response = requests.get('https://axie.zone:3000/server_status', verify=False)
        json_data = repsonse_to_string(json.loads(response.text))

        embed = discord.Embed(title="Axie Infinity Server Status", color=PRIMARY_COLOR)
        embed.set_thumbnail(url="https://www.cryptonewsz.com/wp-content/uploads/2021/07/Axie-Infinity-Price-Analysis.jpg")
        embed.add_field(name="**Maintenance**", value=json_data['status_maintenance'], inline=False)
        embed.add_field(name="**Battle Server**", value=json_data['status_battles'], inline=False)
        embed.add_field(name="**Marketplace**", value=json_data['status_cloudflare'], inline=False)
        embed.add_field(name="**Game API Server**", value=json_data['status_graphql'], inline=False)
        embed.set_footer(text="Source: Axie Infinity")
        await ctx.send(embed=embed)

    @commands.command(aliases=['price'], description="Search current crypto/token price in the market")
    async def _price(self, ctx, *, token = None):
        if len(ctx.message.content.split()) == 2:
            symbol = ctx.message.content.lower().split()[1]
            index = next((i for i, item in enumerate(all_tokens_json)
            if item["symbol"] == symbol), None)
            
            if index != None:
                id = all_tokens_json[index]["id"]
                name = all_tokens_json[index]["name"]

                response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php,usd"
                .format(all_tokens_json[index]["id"]))
                response_json = response.json()
                price = "{:,.8f}".format(response_json[id]["usd"]).rstrip("0").rstrip(".")
                php = "{:,.8f}".format(response_json[id]["php"]).rstrip("0").rstrip(".")
                    
                title = f'{symbol.upper()}'
                description = f'{name}'
                color = discord.Color.green()

                commands_embed = discord.Embed(title=title, description=description, color=color)
                commands_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1qCcyuRCGMQXS38p_iwJCXQ32FnEBVExlDmFIytBYFTBpDzW0KH6n02xwLnZs5n2dd-E&usqp=CAU")
                commands_embed.add_field(name="Price", value=f'$ {price}', inline=False)
                commands_embed.add_field(name="Php", value=f'₱ {php}', inline=False)
                commands_embed.set_footer(text="Source: Coingecko")
                await ctx.send(embed=commands_embed)
                
            else:
                await ctx.send(f"{choice(unknown_coin)} {choice(unknown_coin_2)}")

        elif token == None:
            await ctx.send("Please enter crypto token")

        elif len(ctx.message.content.split()) == 1:
            await ctx.send("Please input a token")
            
        else:
            await ctx.send("Too many parameters. Try again.")

def setup(bot):
    bot.add_cog(Crypto(bot))