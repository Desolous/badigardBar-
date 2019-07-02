import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

bot = discord.Client()
bot_prefix="*"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print ("Çalıştırılıyor")
    activity = discord.Game(name="Hayallerimle")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print ("Aktif")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="boşlar")
    await channel.send(member.mention + " Hoşgeldin Paşam !")


@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="boşlar")
    await channel.send(member.mention + " Hop Hemşerim Nereye ?")


bot.run("NTk1NjQ1NTE3NDQ3NTYxMjQ1.XRuBIw.BqoUn3B6ASXSGqqExnWuQ1Uea1Q") 
