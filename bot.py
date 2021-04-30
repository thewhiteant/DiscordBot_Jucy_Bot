from datetime import date
import discord
from discord.ext import commands
import random
import datetime
import time
import json


x = datetime.datetime.now()


client = commands.Bot(command_prefix="$", help_command=None,intents=discord.Intents.all())

# TODO: cmt1 Bot Rady + Custom Status


f_date = date(2020, 12, 30)
l_date = date.today()
delta = f_date - l_date


# @client.event
# async def on_message(message):
#     if message.content.startswith("!p"):
#         time.sleep(5)
#         await message.channel.purge(limit=4)
#     elif message.content.startswith(">p"):
#         time.sleep(5)
#         await message.channel.purge(limit=4)
#     elif message.content.startswith("*p"):
#         time.sleep(5)
#         await message.channel.purge(limit=4)
#     elif message.content.startswith("-p"):
#         time.sleep(5)
#t         await message.channel.purge(limit=2)
#     elif message.content.startswith("_p"):
#         time.sleep(5)
#         await message.channel.purge(limit=3)

@client.event
async def on_ready():
    print("Bot Running------------>")
    activity = discord.Activity(name=" Jucy man 69 💦", type=1)  #
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)


@client.event
async def on_member_join(member):
    await member.send("> **Wait** `6.333333333330123 `**s to :unlock: UnloCke All VC to unlock everything**")



@client.event
async def on_member_remove(member):
    await member.send(f"> ** {member.name} Khatam bye bye .. Tata GoodBye Gya **")




#for temp vc
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
    elif after.channel is None:
          if len(va) != 0:
               for i in va:
                    channel = discord.utils.get(guild.voice_channels, name=i)
                    if len(channel.members) == 0:
                       va.remove(i)
                       await channel.delete()
    
    if str(after.channel) == '🔓UnloCke All':
        
        time.sleep(4)
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)


@client.event
async def on_raw_reaction_add(payload):

    if payload.channel_id == 837456234894196776:
        with open("rtr.json") as react_file:

            data = json.load(react_file)
            for x in data:
                if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
                        await payload.member.send("https://discord.gg/TRGzSqvuek")
                        channel = client.get_channel(payload.channel_id)
                        message = await channel.fetch_message(x["message_id"])
                        await message.remove_reaction(x["emoji"], payload.member)

                elif x["emoji"] != payload.emoji.name and x["message_id"] != payload.message_id:
                        channel = client.get_channel(payload.channel_id)
                        message = await channel.fetch_message(payload.message_id)
                        await message.remove_reaction(payload.emoji, payload.member)


@client.command()
async def srx(ctx, emoji):

    embed = discord.Embed(title="Invitation Link ", description="React For Invitation Link  :calling:", color=0x80ff00)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782847710201774120/782847804459450398/bg.png")
    embed.set_footer(text="Copyright © White-Ant")
    await ctx.channel.purge(limit=1)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji)
    with open("rtr.json") as json_file:
        data = json.load(json_file)
        new_react = {
            "emoji": emoji,
            "message_id": msg.id
        }
        data.append(new_react)

    with open("rtr.json", "w") as j:
        json.dump(data, j, indent=4)



#help likhle ja ja command ase

@client.command()
async def help(ctx):
    embed = discord.Embed(title=ctx.author.name, description="You Got This!",url="https://discord.gg/TRGzSqvuek", color=0x0abacd)
    embed.set_author(name="  All Commands", url="https://discord.gg/TRGzSqvuek",icon_url="https://media.tenor.com/images/2d04da00ecf31f6065b436094f0b9c95/tenor.gif")
    embed.set_image(url="https://cdn.discordapp.com/attachments/782847710201774120/785742282833264640/Ant.gif")
    embed.add_field(name="$ping", value="Test Ping", inline=False)
    embed.add_field(name="$invite", value="Jucy [Invite your friend]", inline=False)
    # embed.add_field(name="$an [name]", value="or Random", inline=False)
    embed.add_field(name="$p ", value="ex: $p MandO", inline=False)
    embed.add_field(name="$dp", value="Someone DP(Display Picture)", inline=True)
    embed.add_field(name="$dm", value="Personal dm with mention", inline=False)
    embed.add_field(name="$pvt ", value="Message Without Trace", inline=False)
    embed.set_footer(text="Copyright © White-Ant")
    await ctx.send(embed=embed)

#private msg
@client.command(pass_context=True)
async def pvt(ctx, *, msg):
    print(f"{ctx.author.name} sent {msg}  Time: {x}")
    await ctx.channel.purge(limit=1)
    await ctx.send(msg)
#ping check command

@client.command()  # Ping(Latency)
async def ping(ctx):
    ping = round(client.latency*1000)
    if ping > 100:
        embed = discord.Embed(
            title=f" {ping} ms", description="Ooops!! Little Bit High!", color=0xe40101)
        embed.set_author(name=ctx.author.name,
                         url="https://discord.gg/TRGzSqvuek", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://cdn1.vectorstock.com/i/thumb-large/01/85/triangular-red-warning-hazard-symbol-vector-25180185.jpg")
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"{ping} ms", description="Nice Ping Man!!!", color=0xffb123)
        embed.set_author(name=ctx.author.name,url="https://discord.gg/TRGzSqvuek", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://image.freepik.com/free-vector/smiling-face-emoji_1319-431.jpg")
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)


@client.command()  # Invite to your dm
async def invite(ctx):
   await ctx.author.send("https://discord.gg/TRGzSqvuek")
   embed = discord.Embed(title=ctx.author.name, description="Invite Already Sent To Your DM 😉 \n `If Dm are not available, Click Team Jucy on top of this`", color=0x01d9f1)
   embed.set_author(name="Team JUCY", url="https://discord.gg/TRGzSqvuek",icon_url="https://cdn.discordapp.com/splashes/557864258617081858/053c45339b4d85c9cca13ffdc151d720.jpg?size=2048")
   embed.set_thumbnail(url=ctx.author.avatar_url)
   embed.set_footer(text="Copyright \u00a9 White-Ant")
   await ctx.send(embed=embed)



#dm command
@client.command()
async def dm(ctx, user: discord.User, *, msg):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Private DM Sent To {user.name}....")
    await user.send(msg)

#dp
@client.command()
async def dp(ctx, user: discord.User):
    await ctx.send(user.avatar_url)


@client.command()
async def delt(ctx, rang):
    rang = int(rang)
    await ctx.channel.purge(limit=rang)






# @client.command()
# async def an(ctx, *, x=None):
#     dic = {
#         #rent a girlfriend
#         "Mizuhara":  ["Rent a Girlfriend", 0xFDAFB7, "https://www.anime-planet.com/images/characters/chizuru-mizuhara-157856.jpg"],
#         #tonikawa
#         "Nasa kun": ["Tonikawa", 0xC4E2DD, "https://www.anime-planet.com/images/characters/nasa-yuzaki-170364.jpg?t=1601703158"],
#         "Tsukasa Tsukuyom": ["Tonikawa", 0xFFB9BA, "https://static.wikia.nocookie.net/tonikaku-kawaii/images/b/b4/TsukasaAnime.png/revision/latest?cb=20201023142348"],
#         #naruto
#         "Narutu":  ["Nauto", 0xD6D649, "https://qph.fs.quoracdn.net/main-qimg-dbe7a01f55cd5895da8802ae53aa5cf4"],
#         "Hinata": ["Nauto", 0xD4CBD9, "https://www.anime-planet.com/images/characters/hinata-hyuuga-626.jpg"],
#         #fairy tails
#         "Natsu": ["Fairy Tale ", 0xB8879F, "https://static.wikia.nocookie.net/fairytail/images/c/ca/Natsu_X792.png/revision/latest?cb=20181111122101"],
#         #One Piece
#         "Luffy": ["One Piece", 0xCC8E67, "https://i1.sndcdn.com/avatars-000587714706-vjdrog-t500x500.jpg"],
#         "Nami": ["One Piece", 0xF2EFF2, "https://static.wikia.nocookie.net/onepiece/images/6/68/Nami_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20190720162446"],
#         "Zoro ":  ["One Piece", 0x7DD29A, "https://static.wikia.nocookie.net/onepiece/images/6/64/Roronoa_Zoro_Anime_Pre_Timeskip_Infobox.png/revision/latest?cb=20200918221448"],
#         "Sanji": ["One Piece", 0x000019, "https://static.wikia.nocookie.net/loveinterest/images/7/73/Sanji_im_Alter_von_21_Jahren_auf_dem_Sabaody-Archipel.jpg/revision/latest/top-crop/width/360/height/450?cb=20180902235218"],
#         "Usoop": ["One Piece", 0xE8C597, "https://i.pinimg.com/originals/7c/43/7f/7c437f5d2eea737af7c99cab42546750.png"],
#         "Chopper": ["One Piece", 0x35BADD, "https://static.wikia.nocookie.net/onepiece/images/a/af/Tony_Tony_Chopper_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20130428202154"],
#         "Robin": ["One Piece", 0xE8C2FB, "https://i.pinimg.com/originals/30/27/87/3027877470647351f797c2268fab663b.jpg"],
#         "Franky": ["One Piece", 0x7E0E1B, "https://static.wikia.nocookie.net/onepiece/images/8/8c/Franky_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20130225034035"],
#         "Brook": ["One Piece", 0xDD8229, "https://i.stack.imgur.com/ouNRB.jpg"],
#         #deamon slayer
#         "Tanjiro": ["Deamon Slayer", 0x6D364D, "https://s1.econotimes.com/assets/uploads/20200403efc8ee9b921c01245_th_1024x0.jpg"],
#         #steins:gate
#         "Rintarou Okabe": ["Steins Gate", 0xA3B0A7, "https://i.pinimg.com/564x/6d/fc/7e/6dfc7e860e2796936c1f39f0b0e7c91e.jpg"],
#         "Kurisu Makise": ["Steins Gate", 0xA3B0A7, "https://i.pinimg.com/564x/19/40/65/19406579e0f2198f93295f311cbae6b0--image-anime.jpg"],
#     }
#     if not x:
#         y = dic.keys()
#         y = list(y)
#         x = random.choice(y)
#     embed = discord.Embed(
#         title=f"Name : **{x}** ", description=f"Source : **{dic[x][0]}**", color=dic[x][1])
#     embed.set_image(url=dic[x][2])
#     await ctx.channel.purge(limit=1)
#     await ctx.send(embed=embed)


# #player spawnert
# @client.command(pass_context=True)
# async def p(ctx, x):
#     person = {
#         "Taofiq":  ["Hotty And Naughty Boy", 0xF5E4DF, " Fortnite, Valorant , CSGO ", "XII", "https://cdn.discordapp.com/attachments/782847710201774120/785554806604824646/ers.png"],
#         "Mando":  ["Ahsan Al Rafi || Khai r Game Kheli", 0xD9C0A1, " Fortnite, Valorant , CSGO , Genshin Impact ", "XI", "https://cdn.discordapp.com/attachments/782847710201774120/785786055474544640/Gandu.png"],
#         "Demo":  ["A. R. Rafi || Rich Kid (Potol)", 0xB08A6C, " Main[Valorant , COD MW, RDR] Others Depends on Mood", "X", "https://cdn.discordapp.com/attachments/782847710201774120/785784329527230484/tempu.PNG"],
#         "Mahib":  ["Skill 13, " Valorant , RDR ", "XI", "https://cdn.discordapp.com/attachments/782847710201774120/785788140249939978/1880726.png"],
#     }
#     embed = discord.Embed(e: **{x}**  Class: **{person[x][3]}** ", description=f"Games: ** {person[x][2]} **", color=person[x][1])
#     embed.setame="Player introduction",
#                      url="https://discord.gg/GfkjDChWbE")
#     embed.set_image(url=person[x][4])
#     embed.seton[x][0]}")
#     await ctx.channel.purge(limit=1)
#     await ctx.send(embed=embed)

# @client.command()
# async def music(ctx):
#     # channel = ctx.author.voice.channel
#     # await channel.connect()
#     vc = discord.utils.get(ctx.guild.channels, id=808900116824064010)
#     vc = await vc.connect()

#     def repeat():
#         vc.play(discord.FFmpegPCMAudio(source=f"mx/m5.mp3"), after=lambda e:repeat())
#         vc.is_playing()

#     vc.play(discord.FFmpegPCMAudio(source=f"mx/m5.mp3"), after=lambda e:repeat())


BOTT = "Nzc1NDQxMTc3NzY3NDQ0NTUx.X6mX3w.ucn9BDqn3vDdR2Yr7dd6YRo5BgY"
client.run(BOTT)
