import discord
from discord.ext import commands
from enum import Enum


class ActualIs(Enum):
    HIGHER = 1
    MATCH = 0
    LOWER = -1


def higher_lower(min_value, max_value, callback):
    assert isinstance(max_value, int)
    assert isinstance(min_value, int)
    assert max_value > min_value
    candidate = midpoint(min_value, max_value)
    while True:
        result = callback(candidate)
        if result is ActualIs.MATCH:
            return candidate
        elif result is ActualIs.LOWER:
            # lower
            max_value = candidate
            candidate = midpoint(min_value, candidate)
        elif result is ActualIs.HIGHER:
            # higher
            min_value = candidate
            candidate = midpoint(candidate, max_value)
        else:
            assert False, "Should be a ActualIs enum constant"


def midpoint(x, y):
    return x + ((y - x) // 2)

class HighLow(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin: Higher Lower module successfully imported")

    @commands.command()
    async def higherlower(self, ctx: commands.Context):
        """Starts a game with yourself."""
        higher_lower(1, 10, ctx)

def setup(bot):
    bot.add_cog(HighLow(bot))