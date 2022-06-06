import discord
from discord.ext import commands
import time
from config import *
import logging

bot = commands.Bot(command_prefix = PREFIX, intents =  discord.Intents().all())
bot.remove_command('help')
#slash = SlashCommand(bot, sync_commands=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("🆃🆄🅺🅼🅾🅻 ​ 🅸🆂 ​ 🅽🅾🆆 ​ 🅾🅽🅻🅸🅽🅴")
    
    #Playing
    #await bot.change_presence(activity=discord.Game(name=f" always mga kili-kile!")) #{len(bot.guilds)}
    #Streaming
    #await bot.change_presence(activity=discord.Streaming(name=f"My Stream", url=twitch_url))
    #Listening
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    #Watching
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you kili-kile!"))   
    # await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)


bot.load_extension("tukmol")
bot.load_extension("help")
bot.load_extension("ball8")
#bot.load_extension("crypto")
bot.load_extension("fun")
bot.load_extension("member")
bot.load_extension("moderation")
bot.load_extension("music")
bot.load_extension("server")
bot.load_extension("settings")
bot.load_extension("utility")
bot.load_extension("welcome")

#bot.load_extension("tictactoe")
#bot.load_extension("ephemeral")
bot.load_extension("higherlower")
bot.run(TOKEN)