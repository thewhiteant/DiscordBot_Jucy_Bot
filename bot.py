import asyncio
from asyncio.tasks import sleep
from datetime import date
from math import inf
import discord
from discord import message
from discord.ext import commands ,tasks
import datetime
from discord.utils import async_all, get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import requests
import os
import urllib.parse
import re
import sys



x = datetime.datetime.now()


client = commands.Bot(command_prefix="$", help_command=None,intents=discord.Intents.all())

# TODO: cmt1 Bot Rady + Custom Status





f_date = date(2020, 12, 30)
l_date = date.today()
delta = f_date - l_date








va = []
@client.event
async def on_voice_state_update(member, before, after):
        guild = member.guild
        if str(after.channel) == 'Jucy Click To VC':
            if str(after) != str(before):
                if member.name != str(before.channel):
                    channel = discord.utils.get(guild.voice_channels, name=member.name)
                    if channel == None:
                        va.append(f"{member.name}")
                        await after.channel.clone(name=member.name)
                        channel = discord.utils.get(guild.voice_channels, name=member.name)
                        await member.move_to(channel)
                    else:
                        channel = discord.utils.get(guild.voice_channels, name=member.name)
                        await member.move_to(channel)
        elif (after.channel is None) or (before.channel == "Jucy Click To"):
            if len(va) != 0:
                for i in va:
                    channel = discord.utils.get(guild.voice_channels, name=i)
                    if len(channel.members) == 0:
                        va.remove(i)
                        await channel.delete()

#join leave

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("> **Command Not Found Type: ** '$help'")



@client.event
async def on_member_join(member):
       await member.send("Welcome")
       role = discord.utils.get(member.guild.roles, name="Member")
       await member.add_roles(role)

@client.event
async def on_member_remove(member):
    await member.send(f"Bye Bye {member.name}  :cry: We will miss u {member.name}")
    inv = "https://discord.gg/8A5HuCaFku"
    await member.send(inv)


@client.event
async def on_ready():
    print("Bot Running------------>")
    activity = discord.Activity(name=" Jucy man 69 💦", type=1)  #
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)




#help likhle ja ja command ase
    
@client.command()
async def help(ctx):

    color = []
    for clr in range(0x00000, 0xfffff):
        color.append(clr)
    inv = await ctx.channel.create_invite(max_age='10', max_uses=1)
    embed = discord.Embed(title=ctx.author.name, description="You Got This!", url= inv , color=color[0])
    embed.set_author(name="  All Commands",url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail( url="https://cdn.discordapp.com/avatars/919574001355984906/02a2ee3d429a04c77feeb178e805187e.webp?size=1024")
    embed.add_field(name="$ping", value="Test Ping", inline=False)
    embed.add_field(name="$invite", value="Jucy [Invite your friend]", inline=False)
    embed.add_field(name="$dp @mention", value="Show Profile Picture", inline=False)
    embed.add_field(name="$dm", value="Personal dm with mention [Jucy Role Require]" , inline=False)
    embed.add_field(name="$pvt ", value="Message Without Trace  [Jucy Role Require]", inline=False)
    embed.add_field(name="Music Bot", value="---------", inline=False)
    embed.add_field(name="$p song_name", value="Search Any Song And Play with bot", inline=True)
    embed.add_field(name="$pos", value="Pause Song", inline=True)
    embed.add_field(name="$res ", value="Resume Song", inline=True)
    embed.add_field(name="$stop ", value="Stop Song", inline=True)
    embed.set_footer(text="Copyright © White-Ant")
    await ctx.send(embed=embed)


#jucy Ping


@client.command()  # Ping(Latency)
async def ping(ctx):
    ping = round(client.latency*1000)
    if ping > 100:
        embed = discord.Embed(
            title=f" {ping} ms", description="Ooops!! Little Bit High!", color=0xe40101)
        embed.set_author(name=ctx.author.name,url="https://discord.gg/3zMrW2uKuy", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn1.vectorstock.com/i/thumb-large/01/85/triangular-red-warning-hazard-symbol-vector-25180185.jpg")
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"{ping} ms", description="Nice Ping Man!!!", color=0xffb123)
        embed.set_author(name=ctx.author.name,url="https://discord.gg/3zMrW2uKuy", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://image.freepik.com/free-vector/smiling-face-emoji_1319-431.jpg")
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.send(embed=embed)
        



def quoteCOl():
    data = requests.get("https://zenquotes.io/api/random")
    if data.status_code == 200:
        final = data.json()
        return final[0]['q'] + " --" + final[0]['a']


@client.command()
async def quote(ctx):
   await ctx.send(f"> **{quoteCOl()}**")










@commands.has_role("Jucy")
@client.command(pass_context=True)
async def pvt(ctx, *, msg):
    print(f"{ctx.author.name} sent {msg}  Time: {x}")
    await ctx.channel.purge(limit=1)
    await ctx.send(msg)
#ping check command


@client.command()  # Invite to your dm
async def invite(ctx):
    inv = await ctx.channel.create_invite(max_age='200',max_uses = 2)
    await ctx.author.send(f"``` \t{inv} \n```\n> {inv} ")
    embed = discord.Embed(title=ctx.author.name, description="Invite Already Sent To Your DM 😉 \n `If Dm are not available, Click Team Jucy on top of this`", color=0x01d9f1)
    embed.set_author(name="Team JUCY", url=inv,icon_url="https://cdn.discordapp.com/splashes/557864258617081858/053c45339b4d85c9cca13ffdc151d720.jpg?size=2048")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text="Copyright \u00a9 White-Ant")
    await ctx.send(embed=embed)

@commands.has_role("Whiteant")
@client.command()
async def sendin(ctx, user:discord.User):
    inv = await ctx.channel.create_invite(max_age='200',max_uses = 2)
    await ctx.author.send(inv)
    embed = discord.Embed(title=ctx.author.name, description="Invite Sent By Whiteant 😉 \n `If Dm are not available, Click Team Jucy on top of this`", color=0x01d9f1)
    embed.set_author(name="Team JUCY", url=inv,icon_url="https://cdn.discordapp.com/splashes/557864258617081858/053c45339b4d85c9cca13ffdc151d720.jpg?size=2048")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text="Copyright \u00a9 White-Ant")
    await user.send(embed=embed)


@commands.has_role("Jucy")
@client.command()
async def dm(ctx, user: discord.User, *, msg):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Private DM Sent To {user.name}....")
    await user.send(msg)


@client.command()
async def dp(ctx, user: discord.User):
    if user == None:
        user = ctx.author
    await ctx.send(user.avatar_url)


@commands.has_role("Jucy")
@client.command()
async def delt(ctx, dat):
        await ctx.channel.purge(limit=int(dat))




url = []

@client.command()
async def p(ctx, *,link):

    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if link not in url:
        url.append(link)
    for i in url:
        await ctx.send(f"Song: {i}")


    if not voice.is_playing():

        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(client.voice_clients, guild=ctx.guild)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if url[0][0:4] == "https":
                info = ydl.extract_info(url, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{url[0]}", download=False)['entries'][0]
            URL = info['url']
            lenth = info["duration"]
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))  #await voice.disconnect()
                    # voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="test.mp3"))
            voice.is_playing()

            await asyncio.sleep(lenth)
            if len(url) != 0:
                url.pop(0)
                print("play next")
                await ctx.invoke(client.get_command('p'), link=url[0])
                print("work")
            if not voice.is_playing():
                await voice.disconnect() 


    # except:
    #      await ctx.send("Song Is not playable")


@client.command()
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if  voice.is_playing():
       voice.pause()
       url.pop(0)
       await ctx.invoke(client.get_command('p'), link=url[0])




@client.command()
async def res(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice.is_playing():
       voice.resume()

        # command to pause voice if it is 

@client.command()
async def pos(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send('Ay Ay Captain')
        await asyncio.sleep(60)
        if not voice.is_playing():
            await voice.disconnect()



     


@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')
        await asyncio.sleep(20)
        if not voice.is_playing():
            await voice.disconnect()

    


@commands.has_role("Jucy")
@client.command()
async def cl(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    if not voice.is_playing():
        voice.play(discord.FFmpegPCMAudio(source="test.mp3"))
        voice.is_playing()
        await asyncio.sleep(5)
        if not voice.is_playing():
            await voice.disconnect()


#time is in 24hr format
 #channel ID o send images tot



@tasks.loop(hours=24)
async def time_check():
    await client.wait_until_ready()
    message_channel = client.get_channel(id=928508066192850986)
    await message_channel.purge(limit=1)
    await message_channel.send(f"> **{quoteCOl()}**")
time_check.start()
BOTT = "OTE5NTc0MDAxMzU1OTg0OTA2.YbXyBg.JndmTJA_TnUixbJFJDWO6cd6DWA"
client.run(BOTT)
