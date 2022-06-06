import discord
from discord.ext import commands
import datetime

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Member module successfully imported")

    @commands.command(aliases=['avatar'], description="Get a bigger image of a users avatar")
    async def _avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
            
            embed = discord.Embed(color = member.colour)
            embed.set_image(url='{}'.format(member.avatar))
            msg = await ctx.send(embed = embed)
            await msg.add_reaction('👍')
        else:
            embed = discord.Embed(color = member.colour)
            embed.set_image(url='{}'.format(member.avatar))
            msg = await ctx.send(embed = embed)
            await msg.add_reaction('👍')

    @commands.command(aliases=['userinfo'], description="Shows various information about you or the specified user")
    async def _userinfo(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author

            embed = discord.Embed(title = "User Information", color = member.colour) 
            embed.set_thumbnail(url='{}'.format(member.avatar))
            embed.add_field(name="ID", value=member.id, inline=False)
            embed.add_field(name="Name", value=str(member), inline=True)
            embed.add_field(name="Role", value=member.top_role.mention, inline=True)
            embed.add_field(name="Status", value=str(member.status).title(), inline=True)
            embed.add_field(name="Created at", value=member.created_at.strftime("%m/%d/%Y %H:%M %p"), inline=True)
            embed.add_field(name="Joined at", value=member.joined_at.strftime("%m/%d/%y %H:%M %p"), inline=True)
            embed.add_field(name = ":video_game: Activity", value = None if ctx.guild is None or member.activity is None else member.activity.name, inline=False)
            
            if bool(member.premium_since) == True:
                embed.add_field(name=":gem:  Premium", value="Since {}".format(member.premium_since), inline=True)
            else:
                embed.add_field(name=":gem:  Premium", value=bool(member.premium_since), inline=True)
            
            await ctx.send(embed=embed)

        else:
            #timestamp = datetime.utcnow()
            embed = discord.Embed(title = "User Information", color = member.colour) 
            embed.set_thumbnail(url='{}'.format(member.avatar))
            embed.add_field(name="ID", value=member.id, inline=False)
            embed.add_field(name="Name", value=str(member), inline=True)
            embed.add_field(name="Role", value=member.top_role.mention, inline=True)
            embed.add_field(name="Status", value=str(member.status).title(), inline=True)
            embed.add_field(name="Created at", value=member.created_at.strftime("%m/%d/%Y %H:%M %p"), inline=True)
            embed.add_field(name="Joined at", value=member.joined_at.strftime("%m/%d/%y %H:%M %p"), inline=True)
            embed.add_field(name = ":video_game: Activity", value = None if ctx.guild is None or member.activity is None else member.activity.name)

            if bool(member.premium_since) == True:
                embed.add_field(name=":gem:  Premium", value="Since {}".format(member.premium_since), inline=True)
            else:
                embed.add_field(name=":gem:  Premium", value=bool(member.premium_since), inline=True)
            
            await ctx.send(embed=embed)
    
    @commands.command (aliases=['newmembers'])
    @commands.bot_has_permissions (embed_links=True)
    async def newusers (self, ctx, *, count=5):
            
        count = min(max(count, 5), 25)
        now = datetime.now(timezone.utc)
        e = discord.Embed()
        
        for idx, member in enumerate(sorted (ctx.guild.members, key=lambda m: m.joined_at, reverse=True)):
                if idx >= count:
                        break
                value = 'Joined (0} ago\nCreated {1} ago'.format (pretty_timedelta(now - member.joined_at), pretty_timedelta(now - member.created_at ))
                e. add_field(name=po(member), value=value, inline=False)

        await ctx.send (embed=e)

def setup(bot):
    bot.add_cog(Members(bot))