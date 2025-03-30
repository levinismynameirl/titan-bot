import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message commands

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Load extensions (cogs) before the bot starts
async def load_extensions():
    """Loads all extensions (cogs) before running the bot."""
    await bot.load_extension("moderation")  # Adjust with your extension names

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Main entry point to run the bot
async def main():
    # Load extensions before starting the bot
    await load_extensions()

    # Start the bot using its token (using environment variable for safety)
    await bot.start(TOKEN)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
