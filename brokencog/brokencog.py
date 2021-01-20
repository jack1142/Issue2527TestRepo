from redbot.core import commands


class Brokencog(commands.Cog):
    @commands.group()
    async def aaa(self, ctx):
        pass

    @aaa.commands()
    async def asbd(self, ctx):
        pass
