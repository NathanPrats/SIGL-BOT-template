import os
from discord.ext import commands
from discord.utils import get
import discord

intents = discord.Intents(messages=True, guilds=True, members=True)

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)

bot.author_id =   # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def count(ctx):
    online = []
    offline = []
    idle = []
    dnd = []
    invisible = []
    members = await ctx.guild.fetch_members().flatten()
    print(members)
    for member in members:
        print(member.name)
        print(member.status)
        if member.status == 'online':
            online.append(member.name)
        if member.status == 'offline':
            offline.append(member.name)
        if member.status == 'idle':
            idle.append(member.name)
        if member.status == 'dnd' or member.status == 'do_not_disturb':
            dnd.append(member.name)
        if member.status == 'invisible':
            invisible.append(member.name)
    print(online)
    print(offline)
    print(idle)
    print(dnd)
    print(invisible)

@bot.command()
async def admin(ctx, member: discord.Member):

    if not get(ctx.guild.roles, name='Admin'):
        perms = discord.Permissions(kick_members=True, ban_members=True, manage_channels=True)
        await ctx.guild.create_role(name='Admin', permissions=perms)
    
    role = get(ctx.guild.roles, name='Admin')
    await member.add_roles(role)

@bot.command()
async def mute(ctx, member: discord.Member):
    if not get(ctx.guild.roles, name='Unmuted'):
        perms = discord.Permissions(send_messages=True)
        await ctx.guild.create_role(name='Unmuted', permissions=perms)
    
    role = get(ctx.guild.roles, name='Unmuted')
    if role in member.roles:
        await member.remove_roles(role)

@bot.command()
async def unmute(ctx, member: discord.Member):
    if not get(ctx.guild.roles, name='Unmuted'):
        perms = discord.Permissions(send_messages=True)
        await ctx.guild.create_role(name='Unmuted', permissions=perms)
    
    role = get(ctx.guild.roles, name='Unmuted')
    if not role in member.roles:
        await member.add_roles(role)

@bot.command()
async def ban(ctx, member: discord.Member):
    await member.ban()


token = ""
bot.run(token)  # Starts the bot