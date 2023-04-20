
import disnake
from disnake.ext import commands
import random
import asyncio
import requests
import yt_dlp
from discord.utils import get
from disnake import FFmpegOpusAudio
intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
user_ranks = {}

## похуй похуй мне, работает, значит нормально
ranks = ["```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```","```bash\n#Podpivas [Common]\n```",
         '```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```','```bash\n#Strigalo [Common]\n```',
         '```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```','```bash\n#Mc Borov [Common]\n```',
         '```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```','```bash\n#Crook 1 lvl [Common]\n```',
         '```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```','```bash\n#Chucha [Common]\n```',
         '```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```','```bash\n#Chmo [Common]\n```',
         '```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```','```bash\nF rank [Common]\n```',
         '```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```','```bash\n#E rank [Common]\n```',
         '```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```','```Tribuna [Uncommon]```',
         '```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```','```Sosochka [Uncommon]```',
         '```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```','```Killer 25lvl [Uncommon]```',
         '```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```','```D rank [Unommon]```',
         '```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```','```C rank [Unmmon]```',
         '```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```','```B rank [Unmmon]```',
         '```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```','```yaml\nRama [Rare]\n```',
         '```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```','```yaml\nZXC [Rare]\n```',
         '```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```','```yaml\nQQE [Rare]\n```',
         '```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```','```yaml\n`OG [Rare]`\n```',
         '```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```','```yaml\nA rank [Rare]\n```',
         '```prolog\nS rank [Legendary]\n```','```prolog\nS rank [Legendary]\n```','```prolog\nS rank [Legendary]\n```',
         '```prolog\nSS Rank [Legendary]\n```','```prolog\nSS Rank [Legendary]\n```','```prolog\nSS Rank [Legendary]\n```',
         '```ml\nSSS Rank [Mythic]\n```',
         '```ml\nMafia Boss [Mythic]\n`'
         ]

ranks_file = 'ranks.txt'



queue = []

#вот эта хуйня кривая

@bot.slash_command(name="play", description="Включи музыку с ютуба")
async def play(ctx, url: str):
    try:
        # Получение потока аудио с помощью youtube_dl
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info['url']
        source = FFmpegOpusAudio (stream_url)
        
        voice = get(bot.voice_clients, guild=ctx.guild)
        if ctx.author.voice is None:
            await ctx.send('Зайди в голосовой канал, я не могу подключиться.')
        elif voice and voice.is_connected():
            await voice.move_to(ctx.author.voice.channel)
        else:
            voice = await ctx.author.voice.channel.connect()

        # Проигрывание музыки
        if not voice.is_playing():
            voice.play(source)

    except Exception as e:
        await print(e)

# ваще не работает
@bot.slash_command(name="stop", description="Останови воспроизведение")
async def stop(ctx):
    voice = disnake.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await ctx.send('Стоп.')
# Работают, но нужно переделать их в / команды
# --------------
@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.pause()
    await ctx.send("Окей, мы на паузе")

@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client
    if voice_client and voice_client.is_paused():
        voice_client.resume()
    await ctx.send("ЕЕЕЕЙ, продолжаем!!")
#--------------

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    global user_ranks
    user_ranks = load_user_ranks_from_file(ranks_file)
    print(f'Ranks saves loaded')

## Rank GET -----------------------------
@bot.slash_command(name="ранг", description="Узнай свой ранг!")
async def rank(ctx):
    user_id = ctx.author.id
    button4 = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Delete")
    view = disnake.ui.View()
    view.add_item(button4)
    
    if user_id in user_ranks:
        rank = user_ranks[user_id]
    else:
        rank = random.choice(ranks)
        user_ranks[user_id] = rank
        save_user_rank_to_file(ranks_file, user_id, rank)
        
    await ctx.send(f'{ctx.author.mention}, Такс... ты у нас: {rank}',view=view)

# работает, но при перезапуске бота забивает хуй на txt файл и записывает все по новой
def load_user_ranks_from_file(ranks_file):
    user_ranks = {}
    try:
        with open(ranks_file, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    try:
                        user_id = int(parts[0])
                        rank = parts[1]
                        user_ranks[user_id] = rank
                    except ValueError:
                        print(f"Error: Invalid data format in line: {line}")
                else:
                    print(f"Error: Invalid data format in line: {line}")
    except FileNotFoundError:
        print(f"Error: File not found: {ranks_file}")
    return user_ranks

def save_user_rank_to_file(ranks_file, user_id, rank):
    with open(ranks_file, 'a') as f:
        f.write(f'{user_id}:{rank}\n')
## REROL -----------------------------------
@bot.slash_command(name="рерол", description="Попробуй получить другой ранг!")
async def рерол(ctx):
    user_id = ctx.author.id
    button4 = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Delete")
    view = disnake.ui.View()
    view.add_item(button4)
    if user_id in user_ranks:
        del user_ranks[user_id]
        remove_user_rank_from_file(ranks_file, user_id)
        rank = random.choice(ranks)
        user_ranks[user_id] = rank
        save_user_rank_to_file(ranks_file, user_id, rank)
        await ctx.send(f'{ctx.author.mention}, Теперь ты: {rank}',view=view)
    else:
        await ctx.send(f'{ctx.author.mention}, у тебя нет ранга используй /ранг')

def remove_user_rank_from_file(ranks_file, user_id):
    with open(ranks_file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2 and int(parts[0]) != user_id:
                f.write(line)
## -----------------------------------------------

@bot.slash_command(name="сколько", description="Попробуй угадать сколько")
async def сколько(ctx):
    # Create 3 buttons
    button1 = disnake.ui.Button(style=disnake.ButtonStyle.green, label="40")
    button2 = disnake.ui.Button(style=disnake.ButtonStyle.red, label="22")
    button3 = disnake.ui.Button(style=disnake.ButtonStyle.primary, label="Дохуя...")

    # Create a nested message with buttons
    view = disnake.ui.View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)

    await ctx.send("Сколько?", view=view)

@bot.command()
async def зайди(ctx):

    if ctx.author.voice is None:
        await ctx.send('Зайди в голосовой канал, гнида, я не могу подключиться.')
    else:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()

@bot.command
async def выйди(ctx):

    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()

    else:
        await ctx.send('Я не в войсе, еблан')

@bot.command()
async def лох(ctx): ## Не работает, ну оно и видно кста. Зато бот сам себя подъебывает
    await ctx.message.delete()
    server = ctx.guild
    all_members = ctx.guild.members
    random_member = random.choice(all_members)
    await ctx.send(f'Лох - {random_member.mention}')

@bot.slash_command(name="привет", description="Поздоровайся с ботом")
async def привет(ctx):
    user = ctx.author
    await ctx.send(f'O, {user.mention}, рад тебя видеть, пошел нахуй :nerd:')

@bot.slash_command(name="пока", description="Попрощайся с ботом")
async def пока(ctx):
    user = ctx.author
    await ctx.send(f'{user.mention}, похуй похуй мне, вали')

@bot.slash_command(name="как_дела", description="Узнай как у бота дела")
async def какдела(ctx):
    await ctx.message.delete()
    words_list = ["Хуево", "Классно", "Нормально", "Похуй", "ХуКлаНоПо (не records.)"]
    random_word = random.choice(words_list)
    await ctx.send(f'{random_word}')

@bot.slash_command(name="ролл", description="Получи случайное число")
async def ролл(ctx, userroll: int = 100):
    user = ctx.author
    max_value = userroll
    random_num = random.randint(1, max_value)
    await ctx.send(f'{user.mention} Выпало: {random_num}')

@bot.slash_command(name="посчитай", description="Посчитай то, что тебе нужно")
async def посчитай(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'Ну типо: {result}')
    except Exception as e:
        await ctx.send(f'Бля, ты тупой: {e}')


@bot.command()
async def команды(ctx, amount=1):
    button4 = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Delete")
    view = disnake.ui.View()
    view.add_item(button4)
    await ctx.message.delete()
    await ctx.send('```''Список команд''\n-----------\nаниме - хуевая картинка, но похуй\nанимецитата\nмем\nшафлгейм\nранк - работает криво\nрерол\nролл (По дефолту 1 - 100)\nпривет\nпока\nкакдела\nпосчитай Пример:(Мистер, посчитай 10+10)\nсколько\nлох\nвыйди\nзайди\nгуль(Бля, не смей)\n-----------\nНЕ РАБОТАЕТ И НЕ БУДЕТ :(\n!play\n!skip\n!volume\n!pause\n!resume\n!clear\n-----------```',view=view)

@bot.slash_command(name="гуль", description="Иди нахуй")
async def гуль(ctx):
        await ctx.send("Бля, ты точно уверен, чел..., ну это пиздец типо\nладно, если тебе это пиздец нужно напиши Мистер, яеблан")

def get_random_anime_image():
    response = requests.get('https://kitsu.io/api/edge/anime')
    if response.status_code == 200:
        data = response.json()
        anime = random.choice(data['data'])
        image_url = anime['attributes']['posterImage']['original']
        return image_url
    else:
        return None

def get_random_anime_quote(): ## мб подрублю перевод
    response = requests.get('https://animechan.vercel.app/api/random')
    if response.status_code == 200:
        data = response.json()
        quote = data['quote']
        character = data['character']
        anime = data['anime']
        return f'"{quote}" - {character} from "{anime}"'
    else:
        return None

@bot.slash_command(name="аниме_цитата", description="Получи рандомную цитату")
async def анимецитата(ctx):
    quote = get_random_anime_quote()
    if quote:
        await ctx.send(quote)
    else:
        await ctx.send('error.')

@bot.slash_command(name="аниме", description="Получи рандомную картинку (плохо работает)")
async def аниме(ctx):
    image_url = get_random_anime_image()
    if image_url:
        embed = disnake.Embed()
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send('error.')

@bot.slash_command(name="мем", description="Мем с редита...")
async def мем(ctx):
    response = requests.get('https://www.reddit.com/r/memes/random.json', headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['data']['children'][0]['data']['url']
        title = data[0]['data']['children'][0]['data']['title']
        embed = disnake.Embed(title=title)
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send('error')

import disnake
from disnake.ext import commands
from disnake import Option, OptionType

messages = [
    "Ты лох, вкурсе?",
    "Ты сегодня выглядишь ужасно",
    "Мне кажется, ты никогда не сможешь чего-то достичь",
    "Твой последний проект был полным провалом, не стоит даже пытаться следующий.",
    "Как ты вообще думал, что это может сработать? Ты такой неумелый в этом деле.",
    "Твой голос звучит ужасно, может лучше не петь вообще?",
    "Ты постоянно совершаешь ошибки, как ты думаешь, когда тебя наконец уволят?",
    "Ты такой неуверенный и несамостоятельный, как ты думаешь, кто захочет с тобой работать?",
    "Ты такой ленивый, что никогда не добьешься успеха в жизни.",
    "Твои идеи постоянно неудачны, может стоит перестать их выдвигать?",
    "Твои друзья никогда не научатся у тебя ничему полезному.",
    "Ты такой непривлекательный, что никто не захочет с тобой встречаться.",
    "Ты никогда не будешь настоящим лидером, тебе не хватает уверенности и харизмы.",
    "Твой уровень умения сравним с умением собаки держать палку во рту.",
    "Ты такой малоприятный, что даже мухи улетают, когда ты появляешься.",
    "Ты такой медлительный, что к твоему дню рождения поздравления придут только на следующий год.",
    "Ты такой мудрый, что я бы даже спросил у тебя, как жить, но я боюсь, что мои мозги не смогут вместить все твои знания.",
    "Ты такой талантливый, что тебе не нужно учиться, чтобы достичь успеха - просто удача будет следовать за тобой.",
    "Ты такой красивый, что твои фотографии настолько великолепны, что все модели и актеры выглядят рядом с тобой, как пачка старых газет.",
    "Ты такой обаятельный, что если бы я был рыбой, я бы просил тебя на свидание.",
    "Ты такой крутой, что даже я хочу стать тобой - но, к сожалению, я уже слишком крутой, чтобы меняться.",
    "Ты такой умный, что мне кажется, что если бы ты стал зубным врачом, то многие бы начали ходить к зубному не по медицинским показаниям, а просто чтобы послушать твои умные рассуждения.",
    "Ты такой остроумный, что мне кажется, что твой мозг работает на частоте, которую не поддерживают современные компьютеры.",

]

@bot.slash_command(name="обидь", description="Попусти лоха")
async def insult(ctx, user: disnake.Member):
    message = random.choice(messages)
    await ctx.send(f"{user.mention}, {message}")



@bot.slash_command(name="я_еблан", description="Покажи всем кто ты на самом деле")
async def яеблан(ctx):
    user = ctx.author
    await ctx.send(".")
    await asyncio.sleep(1)
    await ctx.send("..")
    await asyncio.sleep(1)
    await ctx.send("...")
    await asyncio.sleep(1)
    await ctx.send(":orangutan:")
    await ctx.send(f'{user.mention}, а все, лавочка прикрыта')
    ##for i in range(1000, -1, -7):
        ##await ctx.send(i)
        ##await asyncio.sleep(0.1)

word_list = ['3bu1a','Ебула','Снежок','Кендоку рамен','Солнце','Птица','Подпивас','Аболтус','Тварь дрожащая','Анекдот',
             'Учитель','Сигарета','Чапман','Клоун','Траншея','Тяги','Найк','Адидас','Приора','Ворона',
             'Кошка','Собака','Человек','Подсолнух','Мистер Ботик',
]
@bot.slash_command(name="шафлгейм", description="Я загадаю тебе слово в котором все буквы переставленны местами\n твоя задача угадать что это за слово")
async def шафлгейм(ctx):
    word = random.choice(word_list)
    shuffled_word = ''.join(random.sample(word, len(word)))
    await ctx.send(f'Слово - {shuffled_word}\nУ тебя есть 30 секунд что бы отгадать')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    try:
        message = await bot.wait_for('message', check=check, timeout=30.0)
        if message.content.lower() == word.lower():
            await ctx.send('Правильно! Я думал у тебя 10 IQ, а ты вон какой умный')
        else:
            await ctx.send(f'Не, хуйня, слово было: {word}')
    except asyncio.TimeoutError:
        await ctx.send('Время вышло :nerd:.')





##Events
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('Чо ты спизданул?')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Не понял, конкретнее.')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    await member.send(f'Йоу, {member.name}! Чо с ебалом?')

@bot.event
async def on_member_remove(member):
    await member.send(f'Пока, {member.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    for voice_client in bot.voice_clients:
        if voice_client.guild == member.guild:
            break  
    else:
        return 

    if len(voice_client.channel.members) == 1 and not voice_client.is_paused():
        await asyncio.sleep(5)
        await voice_client.disconnect()


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.event
async def on_button_click(interaction: disnake.MessageInteraction):
    if interaction.component.label == "40":
        await interaction.response.send_message("Too much...")
        await interaction.message.delete()
     
    if interaction.component.label == "22":
        await interaction.response.send_message("Мало")
        await interaction.message.delete()
     
    if interaction.component.label == "Дохуя...":
        await interaction.response.send_message("Нормаааально :)")
        await interaction.message.delete()

    if interaction.component.label == "Delete":
        await interaction.message.delete()
               
bot.run('Токен')


