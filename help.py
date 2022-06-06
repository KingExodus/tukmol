import discord
from discord.ext import commands
from discord import Embed

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()

class Helps(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Help module successfully imported")

    @commands.command(name="help", description="Shows bot help")
    async def _help(self, ctx):
        name = str(ctx.guild.name)
        icon = str(ctx.guild.icon)
        #icon = "https://m.media-amazon.com/images/I/71I9zJauHfL._SS500_.jpg" 
        embed = discord.Embed(title="**{0} Help Commands**".format(name), color = PRIMARY_COLOR)
        embed.set_thumbnail(url=icon)
        embed.add_field(name = "Fun", value = "` 8ball ` ` coinflip ` \n ` tictactoe `  ` embed ` \n ` say ` ` quote ` ` joke ` \n ` bstats ` ` binfo ` \n ` ping ` ` invitebot `", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name = "Info", value = "` help ` ` avatar ` \n ` userinfo ` \n ` invite  ` ", inline=True)        
        embed.add_field(name = "Music", value = "` play ` ` pause ` ` resume ` ` stop ` ` now | current | playing ` \n ` queue ` ` shuffle ` ` skip ` ` remove ` ` loop ` ` volume ` \n ` summon ` ` join ` ` leave | disconnect `", inline=False)
        embed.add_field(name = "Utility", value = "` calcu ` ` translate ` ` tag ` \n ` poll `", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name = "Crypto", value = "` axiestats ` ` price ` ", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Helps(bot))