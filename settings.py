import discord
from discord.ext import commands
import typing

PRIMARY_COLOR = discord.Color.red()
SECONDARY_COLOR = discord.Color.darker_grey()
PRIMARY_COLOR = discord.Color.blue()

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Settings module successfully imported")

    @commands.command(aliases=['reload'], description="Reload an extension or all extensions")
    async def _reload(self, ctx, *, extension: typing.Optional[str] = None):
        if (extension is None): # Reload all extensions
            for ext in self.config["extensions"]:
                self.bot.reload_extension(ext)
            await ctx.send("All extensions reloaded.")
        else: # Reload single extension
            extension = str.lower(extension)
            self.bot.reload_extension(extension)
            await ctx.send("{0} extension reloaded.".format(extension))

    @commands.command(aliases=['load'], description="Load a new extension")
    async def _load(self, ctx, *, extension: str):
        extension = str.lower(extension)
        self.bot.load_extension(extension)
        await ctx.send("{0} extension loaded.".format(extension))

def setup(bot):
    bot.add_cog(Settings(bot))