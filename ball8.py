import discord
from discord.ext import commands
import random
from config import *

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: 8ball module successfully imported!")

    @commands.command(name='8ball', description="Reaches into the future to find the answer to your question")
    async def _8ball(self, ctx, *, question = None):
        responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
               "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "IDK but you should sub to glowstik.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        #await ctx.send(f' :8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')
        if question == None:
            embed=discord.Embed()
            embed.add_field(name="Hey!, Please enter a question", value="`Command: {0}8ball <question>`".format(PREFIX),  inline=False)  
            #\u200b
            await ctx.send(embed=embed)
        else:
            response = random.choice(responses)
            embed=discord.Embed(title="The Magic 8 Ball has spoken!")
            embed.add_field(name=':8ball: Question: ', value=f'{question}', inline=True)
            embed.add_field(name=':8ball: Answer: ', value=f'{response}', inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EightBall(bot))