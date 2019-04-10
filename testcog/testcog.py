from redbot.core import commands
from cog_shared import testlib  # type: ignore


class TestCog(commands.Cog):
    """Some dummy cog for Downloader testing."""

    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        pass

    @commands.is_owner()
    @commands.command()
    async def testcommand(self, ctx, x: int, y: int):
        """Settings for voice tools"""
        result = testlib.add_numbers(x, y)
        await ctx.send(f"Result of {x} + {y} is {result}")
