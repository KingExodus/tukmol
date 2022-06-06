import discord
from discord.ext import commands

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Role module successfully imported!")

    @commands.command(aliases=['autorole'], description="Changes the roles members get on join")
    async def _autorole(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)

    @commands.command(aliases=['getrole'], description="Gives the user the requested role if setup with the `selfrole` command")
    async def _getrole(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['reactionrole'], description="Makes a message in your server able for members to press reactions to get roles.")
    async def _reactionrole(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['selfrole'], description="Manages the roles members can self-assign using the `getrole` command")
    async def _selfrole(self, ctx):
        embed = discord.Embed(title="embed test")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Role(bot))