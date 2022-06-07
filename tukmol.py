import discord
from discord.ext import commands
import time
from config import *

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()

class Heist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Shows Tukmol latency to Discord's API")
    async def _ping(self, ctx):
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("Loading...")
        ping = int((time.monotonic() - before) * 1000)

        await message.edit(content=f'🏓 WS: {before_ws}ms | REST: {ping}ms')

    @commands.command(name="bstats", description="Shows various Tukmol statistics")
    async def _bcheck(self, ctx):
        embed = discord.Embed(description="Hello, i'm alive and watching you!", color=PRIMARY_COLOR)
        #await ctx.send(embed=embed)
        await ctx.send(content="test", embeds=[embed])

    @commands.command(name="binfo", description="Display information about Tukmol")
    async def _binfo(self, ctx):
        app = await self.bot.application_info()
        self.botMember = self.bot.user

        embed = discord.Embed(description = app.description, color = PRIMARY_COLOR)
        embed.set_author(name = "{0} Information".format(self.botMember.name), icon_url = self.botMember.avatar)
        embed.add_field(name = "Username", value = self.botMember, inline = True)
        embed.add_field(name = "Status", value = "✅ Online", inline = True)
        embed.add_field(name = "Activity", value = self.bot.activity, inline = True )

        created = self.bot.user.created_at
        embed.add_field(name = "Created at", value = created.strftime("%d.%m.%Y at %H:%M %p"),inline = True)

        embed.add_field(name = "Server Count", value = len(ctx.guild.name))
        #embed.add_field(name = "Server Count", value = len(guild.name)) #self.bot.users))
        
        print('Servers connected to:')
        for guild in self.bot.guilds:
            print(guild.name)
        
        await ctx.send(embed = embed)

    @commands.command(name="invitebot", description="Invite Tukmol to other server") 
    async def _binvite(self, ctx): 
        app = ctx.bot.user
        #await self.bot.application_info()
        #icon = str(ctx.guild.icon_url)
        icon = "https://m.media-amazon.com/images/I/71I9zJauHfL._SS500_.jpg" 
        embed = discord.Embed(title="**Invite {0} to your server**".format(app.name), color = PRIMARY_COLOR)
        embed.set_thumbnail(url=icon)
        embed.add_field(name = "[Invite link for {0}!]({1}).".format(app.name, BOT_INVITE), value="\u200b")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Heist(bot))
    