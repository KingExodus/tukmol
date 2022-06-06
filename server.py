import discord
from discord.ext import commands

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Server module successfully imported")

    @commands.command(aliases=['invite'], description="Generate an invite link to this server")
    async def _invite(self, ctx):

        
        invites = await ctx.guild.invites()
        channel = ctx.channel

        botInvites = list(x for x in invites if x.inviter.id == self.bot.user.id and x.channel.id == channel.id)

        invite = None
        if (len(botInvites) == 0): # Create new invite in this channel
            #await ctx.send("Creating a new invite link.")
            #invite = await channel.create_invite(reason = "Tukmol created invite link")
            invite = await ctx.channel.create_invite(max_age = 90, max_uses=1, unique=True)
            msg = await ctx.send(invite)
            await msg.edit(content=invite)
        else:
            msg = await ctx.send("Previous invite link found, retrieving that one.")
            invite = botInvites[0]
            await msg.edit(content=invite)
        
        #invitelink = await ctx.channel.create_invite(max_age = 90, max_uses=1, unique=True)
        #await ctx.send(invitelink)


    @commands.command(aliases=['serverinfo'], description="Shows various information about the current guild")
    async def _serverinfo(self, ctx):
        icon = str(ctx.guild.icon_url)
        region = str(ctx.guild.region)
        timestamp = ctx.guild.created_at
        date_time = timestamp.strftime("%m/%d/%Y, %H:%M %p")

        embed = discord.Embed(title= "** Server Information **", description="", color=PRIMARY_COLOR)
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner ", value=f"{ctx.guild.owner} ", inline=False)
        embed.add_field(name=":regional_indicator_a:  Server ID ", value=f"{ctx.guild.id}", inline=False)
        embed.add_field(name=":birthday:  Created at ", value="{0}".format(date_time), inline=False)
        embed.add_field(name=":earth_americas:  Server Region ", value="{0}".format(region.upper()), inline=True)
        embed.add_field(name=":busts_in_silhouette:  Members", value=f"{ctx.guild.member_count} members", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Server(bot))