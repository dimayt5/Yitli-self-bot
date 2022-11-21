import os
import requests
import json
import discord
from discord.ext import commands
from config import *


token=Login.token
prefix=Login.prefix
id=Login.id
bot=commands.Bot(command_prefix=prefix,self_bot=True)
bot.remove_command('help')

#Настройка хелпа не трогайте
link="https://github.com/dimayt5/Yitli-self-bot"
tos_link="https://discord.com/terms"

@bot.event
async def on_ready():
    print(f"""Активно!
Имя аккаунта {bot.user}
ID аккаунта {bot.user.id}
Пинг {int(bot.latency * 1000)}
Ваш префикс {prefix} узнать команды введите {prefix}help""")

#Базовые функции
@bot.command()
async def help(ctx):
    await ctx.send(f"""
```cpp
Внимание! При использовании нашего селф бота Вы соглашаетесь с тем что мы не несём ответственость за вашу учётную запись и правил ToS {tos_link}!
Обьяснение работы команд:
    - команды с аргументами находятся в квадратных скобках после значения команды ---> [Аргумент: --------] 
    - команды без аргументов обозначаются как None после значения команды ---> [Аргумент: None]
Скачать: {link}
```""")
    await ctx.send(f"""```Базовые функции```
`{prefix}clear` - Удалить свои сообщения в чате. [Аргумент: amount число сообщений]

`{prefix}massreact` - Расставить 20 эмодзи в чате под все сообщения. [Аргумент: введите эмодзи и напишите его с командой. Например: `{prefix}massreact :x:`]

`{prefix}spam` - Спам сообщениями. [Аргумент: Введите количество спама сообщений в числе (например: 5 смс будет спамить) и (например: фразу `Привет!`)]

`{prefix}copy` - Скопировать эмодзи сервера [Аргумент: (этот аргумент рекомендован к прочитыванию файла config.py категории SendDM ---> id)]

`{prefix}cpgld` - Скопировать сервер [Аргумент: None]""")
    await ctx.send(f"""```Веселье```
`Животные`
`{prefix}cat` - Рандомное фото с котами [Аргумент: None]

`{prefix}dog` - Рандомное фото с собаками [Аргумент: None]

`{prefix}panda` - Рандомное фото с пандами [Аргумент: None]""")
    await ctx.send(f"""```Активность```
`{prefix}streaming` - Активность стрим [Аргумент: Ввести название активности Стримит (Например: `{prefix}streaming Моя трансляция в DU Recorder`)]

`{prefix}playing` - Активность стрим [Аргумент: Ввести название активности Играет (Например: `{prefix}playing Portal 2`)]

`{prefix}listening` - Активность стрим [Аргумент: Ввести название активности Слушает (Например: `{prefix}listening Звук моря`)]

`{prefix}watching` - Активность стрим [Аргумент: Ввести название активности Смотрит (Например: `{prefix}watching Маинкрафт`)]

`{prefix}stopactivity` - Удалить активность [Аргумент: None]""")


@bot.command()
async def clear(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

@bot.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@bot.command()
async def spam(ctx, amount:int=None, *, message: str=None):
    await ctx.message.delete()
    for each in range (0, amount):
        await ctx.send(f"{message}")


@bot.command()
async def copy(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    dima = await bot.fetch_user(id)
    for em in ctx.message.guild.emojis:
        await dima.send(em.url)
    await dima.send('вывел все')


@bot.command()
async def cpgld(ctx):
    if not ctx.message.guild: return
    guild = ctx.message.guild
    print(f'Начинаю клонирование сервера {guild.name}...')
    try:
        await ctx.message.channel.purge(limit=1)
    except:
        pass
    print(f'Сервер создан - ❌ Созданы роли - ❌ Созданы каналы - ❌ Настроены права каналов - ❌ Созданы эмодзи - ❌')

    new_guild = await bot.create_guild(name=guild.name)
    for channel in new_guild.channels:
        try:
            await channel.delete()
        except:
            pass

    print(f'Сервер создан - ✅ Идёт создание ролей, пожалуйста, подождите... - ⏳ Созданы каналы - ❌ Настроены права каналов - ❌ Созданы эмодзи - ❌')

    print(f'Создан сервер с именем {guild.name} с нужной иконкой, начинаю создание ролей')
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)

    print(f'Сервер создан - ✅ Созданы роли - ✅ Идёт создание каналов, пожалуйста, подождите... - ⏳ Настроены права каналов - ❌ Созданы эмодзи - ❌')

    print(f'Создание ролей завершено, начинаю создание каналов')
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    print(f'Создание каналов завершено, начинаю настройку оверврайтов')
    print(f'Сервер создан - ✅ Созданы роли - ✅ Созданы каналы - ✅ Идёт настройка прав каналов, пожалуйста, подождите... - ⏳ Созданы эмодзи - ❌')
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
            else:
                print(f'(OVERWRITES) Пропускаю {target.name}, так как это юзер')
        await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)
    print(f'Настройка оверврайтов завершена, начинаю создание эмодзи...')
    print(f'Сервер создан - ✅ Созданы роли - ✅ Созданы каналы - ✅ Настроены права каналов - ✅ Идёт создание эмодзи, пожалуйста, подождите... - ⏳')
    print(f'Сервер создан - ✅ Созданы роли - ✅ Созданы каналы - ✅ Настроены права каналов - ✅ Созданы эмодзи - ✅ ')



#Веселье
#Животные
@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/cat").json()
    await ctx.send(r['link'])

@bot.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/dog").json()
    await ctx.send(r['link'])

@bot.command()
async def panda(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/panda").json()
    await ctx.send(r['link'])  

#Активность
@bot.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name = message,
        url = "https://www.youtube.com/watch?v=SHFTHDncw0g", 
    )
    await bot.change_presence(activity=stream)    


@bot.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)


@bot.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

        
@bot.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))


@bot.command()
async def stopactivity(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=None, status=None)

try:
    bot.run(token, bot=False)
except:
    print("Неверный токен или нет токена!\nНапишите в config.py категории Login --> token")