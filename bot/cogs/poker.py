from discord.ext import commands

class Poker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='start')
    async def start_game(self, ctx):
        await ctx.send("Texas Hold'em game starting soon...")

def setup(bot):
    bot.add_cog(Poker(bot))
