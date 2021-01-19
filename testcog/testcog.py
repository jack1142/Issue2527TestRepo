import asyncio
import logging

from redbot.core import commands

log = logging.getLogger("red.testcog")


class TestCog(commands.Cog):
    """Some dummy cog for Downloader testing."""

    def __init__(self, bot):
        self.bot = bot

    def z(self):
        raise RuntimeError("Something went horribly wrong.")

    def y(self):
        self.z()

    async def x(self):
        self.y()

    def create_task_x(self, *args):
        asyncio.create_task(self.x())

    async def initialize(self):
        self.create_task_x()

    @commands.is_owner()
    @commands.command()
    async def testcommand(self, ctx, x: int, y: int):
        """Settings for voice tools"""
        raise RuntimeError("Something went horribly wrong.")
        await ctx.send(f"Result of {x} + {y} is {result}")

    @commands.is_owner()
    @commands.command()
    async def anothercommand(self, ctx, x: int, y: int):
        """Settings for voice tools"""
        raise RuntimeError("Something went horribly wrong.")
        await ctx.send(f"Result of {x} * {y} is {result}")
