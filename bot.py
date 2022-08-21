import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Send: join', url='https://www.twitch.tv/yosiket'))
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if "join" in message.content:
        role = discord.utils.get(message.guild.roles, name="Member")
        await message.author.add_roles(role)
    await bot.process_commands(message)
    emoji = '👌'
    await message.add_reaction(emoji)

bot.run('')
