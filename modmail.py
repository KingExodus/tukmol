import discord
from discord.ext import commands

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

class ModMail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Modmail module successfully imported!")

    @commands.command(aliases=['modmail'])
    async def _test(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ModMail(bot))