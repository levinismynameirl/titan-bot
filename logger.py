import discord
from discord.ext import commands
import datetime

class CommandLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel_id = 1310173771633791037  # Replace with your log channel ID

    @commands.Cog.listener()
    async def on_command(self, ctx):
        """Logs every command used in the server."""
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel:
            embed = discord.Embed(
                title="📝 Command Used",
                description=f"**Command:** `{ctx.command}`\n**User:** {ctx.author.mention}\n**Channel:** {ctx.channel.mention}",
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CommandLogger(bot))
