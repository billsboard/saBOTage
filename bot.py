import asyncio
import discord
import random
import requests
from discord.ext import commands
from nltk.corpus import wordnet

bot = commands.Bot(command_prefix='//')  # bot prefix for all bot commands
TOKEN = "NTA0NDkzNjQ3MzE2NjQ3OTM2.DsE8aw.aJAjSamxZmSiRMZpcLvR_tYIr9E"  # bot token
bot.remove_command("help")  # replaces old help command with custom help


"""EVENTS"""


@bot.event  # checks if bot is ready
async def on_ready():
    await bot.change_presence(game=discord.Game(name="//help"))
    print("Bot is ready!")


@bot.event  # responds to messages
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "<@504493647316647936>":
        await message.channel.send("Bot prefix is **//**")
    await bot.process_commands(message)

    f = open(r"C:\Users\lyndo\Programming\Python\banned_words.txt", 'r')
    chat_filter = tuple(f.read().splitlines())
    f.close()
    contents = message.content.split(" ")
    for word in contents:
        if word.lower() in chat_filter and not isinstance(message.channel, discord.DMChannel):
            await discord.Message.delete(message)
            await bot.get_channel(message.channel.id).send("{}, **You are not allowed to use that word here! Next time it will be a loss of permissions.**".format(message.author.mention))


@bot.event
async def on_command_error(ctx, error):
    pass

"""GRAPHICS"""


@bot.command(name="nuke-pic")  # sends picture of a nuke
async def nuke_pic(ctx):
    await bot.get_channel(ctx.channel.id).send(file=discord.File(r"C:\Users\lyndo\OneDrive\Pictures\Saved Pictures\Discord\nuke\nuke{}.jpg"
                        .format(random.randint(1, 15))))


@bot.command(name="dog-pic")  # sends picture of a dog
async def dog_pic(ctx):
    dog_data = requests.get("https://dog.ceo/api/breeds/image/random").json()
    await ctx.send(dog_data["message"])


@bot.command(name="cat-pic")  # sends picture of a cat
async def cat_pic(ctx):
    api_key = "ca183891-47a4-4ae7-ae2a-c62af21cea04"
    cat_data = requests.get("https://api.thecatapi.com/v1/images/search?format=json&x-api-key=" + api_key).json()
    await ctx.send(cat_data[0]["url"])


@bot.command()
async def meme(ctx):
    meme_data = requests.get("http://alpha-meme-maker.herokuapp.com/{}".format(random.randint(1, 11))).json()
    await ctx.send(meme_data["data"][random.randint(0, len(meme_data["data"]) - 1)]["image"])


@bot.command(name="st-pic")  # sends picture of a square twitter
async def st_pic(ctx, type = None):
    st_text = ("[;]>", "(;)>", "{;}>", "|;|>")

    if type is None:
        await ctx.send("**You must enter a** `type` **parameter.**")
    elif type.lower() == "text":
        await ctx.send(random.choice(st_text))
    elif type.lower() == "paint":
        await bot.get_channel(ctx.channel.id).send(file=discord.File(r"C:\Users\lyndo\OneDrive\Pictures\Saved Pictures\Discord\st\paint.png"))
    elif type.lower() == "ink":
        await bot.get_channel(ctx.channel.id).send(file=discord.File(r"C:\Users\lyndo\OneDrive\Pictures\Saved Pictures\Discord\st\ink.png"))
    elif type.lower() == "draw":
        await bot.get_channel(ctx.channel.id).send(file=discord.File(r"C:\Users\lyndo\OneDrive\Pictures\Saved Pictures\Discord\st\draw{}.jpg".format(random.randint(1, 3))))
    else:
        await ctx.send("**That is not a valid option. Please enter** `text`**,** `paint`**,** `ink` **or** `draw`**.**")

"""RANDOM"""


@bot.command()  # roll a dice
async def roll(ctx, sides = 6):
    try:
        await ctx.send("You rolled a {}.".format(random.randint(1, sides)))
    except ValueError:
        await ctx.send("`sides` must be a natural number.")

@bot.command()  # flip a coin
async def flip(ctx):
    sides = ["heads"] * 10 + ["tails"] * 10 + ["the coin on its side!"]
    await ctx.send("You flipped **{}**.".format(random.choice(sides)))


@bot.command()  # picks a random card from a deck of cards
async def card(ctx):
    value = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
    suit = ("Diamonds", "Clubs", "Hearts", "Spades")
    await ctx.send("Your card is the **{} of {}**.".format(random.choice(value), random.choice(suit)))


@bot.command(name="8ball")  # a magic 8-ball
async def eight_ball(ctx, *args):
    if len(args) == 0:
        return await ctx.send("**Must ask a question.**")

    question = ""
    for word in args:
        question += word
        question += " "

    responses = ("Signs point to yes.", "Yes.", "Reply hazy.", "Try again.", "Without a doubt.", "My sources say no.",
                 "As I see it, yes.", "You may rely on it.", "Concentrate and ask again.",  "Outlook not so good.",
                 "It is decidedly so.", "Better not tell you now.", "Very doubtful.", "Yes - definitely.",
                 "It is certain.", "Cannot predict now.", "Most likely.", "Ask again later.", "My reply is no.",
                 "Outlook good.", "Don\'t count on it.", "Who cares?", "Never, ever, ever.", "Possibly.",
                 "There is a small chance.")

    await ctx.send(responses[len(str(question)) % 25])


@bot.command(name="f-cookie")
async def fortune_cookie(ctx):
    fortunes = ("Your future will come with riches.", "You open your heart to people you care for.", "Something you have longed for will no longer be a dream.",
                "The fortune you seek is in another cookie.", "A cynic is only a frustrated optimist.", "A foolish man listens to his heart. A wise man listens to cookies",
                "The greatest danger may very well be your stupidity.", "Avoid taking unnecessary gambles. Lucky numbers: 13, 27, 35, 65, 78",
                "This cookie contains 117 calories.", "If a turtle doesn't have a shell, is it naked or homeless?",
                "Don't eat the paper.", "It is a good day to have a good day.", "He who laughs at himself never runs out of things to laugh at.")
    await ctx.send(random.choice(fortunes))


"""INFO"""


@bot.command()  # help command for new users
async def help(ctx):
    await bot.get_user(ctx.message.author.id).send(":blue_book: __**saBOTage Help Commands**__")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Graphics =\n"
       "nuke-pic                    :: Picks a random picture of a nuke.\n"
       "dog-pic                     :: Picks a random picture of a dog.\n"
       "cat-pic                     :: Picks a random picture of a cat.\n"
       "st-pic                      :: Picks a random picture of a square twitter (type = text, paint, ink, draw).\n"
       "meme                        :: Shows a meme.\n"
       "```")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Random =\n"
       "roll <sides = 6>            :: Rolls a dice with a specified amount of sides.\n"
       "flip                        :: Flips a coin (Heads = 10/21, Tails = 10/21, Side = 1/21).\n"
       "card                        :: Names a random card from a 52-card deck.\n"
       "8ball <question>            :: Answers a question using the Magic 8-Ball (25 Choices).\n"
       "guess-num                   :: Asks user to guess the bot's number, which is between 1 and 100.\n"
       "f-cookie                    :: Opens a fortune cookie.\n"
       "```")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Information =\n"
       "help                        :: Gives the commands of the saBOTage bot.\n"
       "user-avatar <@user = you>   :: Shows a link and a picture of <@user> avatar.\n"
       "user-id <@user = you>       :: Shows the ID of <@user>.\n"
       "user-name <@user = you>     :: Shows name of <@user>.\n"
       "user-status <@user = you>   :: Shows the status of <@user>.\n"
       "user-joined <@user = you>   :: Shows date when <@user> joined the server.\n"
       "user-roles <@user = you>    :: Lists all of the roles of <@user>.\n"
       "user-toprole <@user = you>  :: Shows the top tole of <@user>.\n"
       "user-info <@user = you>     :: Lists <@user> name, id, status, date joined, top role, and avatar URL.\n"
       "user-list                   :: Lists all of the users from the channel's server, and their top role.\n"
       "```")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Configuration =\n"
       "clear <amount>        :: Deletes <amount> number of messages from channel (<amount> within [1, 500]).\n"
       "```")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Fun =\n"
       "joke <type = you>           :: Bot will give a <type> joke (<type> = [Yo Momma = ym, Knock Knock = kk]).\n"
       "rps                         :: Plays rock, paper, scissors, with the bot.\n"
       "roast                       :: Bot sends a roast text to you.\n"
       "emoji <type>                :: Sends emoji art based on <type> (<type> = frozen, up, dirty (NSFW), chess).\n"
       "```")
    await bot.get_user(ctx.message.author.id).send("```asciidoc\n"
       "= Utilities =\n"
       "PvsT                        :: Compares Pewdiepie and T-Series's subscriber counts.\n"
       "sub-count <username>        :: Gets subscriber count of youtuber. (remove symbols/spaces in <username>).\n"
       "view-count <username>       :: Gets view count of youtuber. (remove symbols/spaces in <username>).\n"
       "video-count <username>      :: Gets video count of youtuber. (remove symbols/spaces in <username>).\n"
       "bitcoin <currency = CAD>    :: Gets bitcoin value in <currency>, which should be in abbreviated form.\n"
       "forecast <city> <data>      :: Gets <data> forecast of <city>, (<data> = temp, weather, air).\n"
       "urban <word> <define = 1>   :: Gets a definition of a <word>, example, and link from the urban dictionary (NSFW).\n"
       "dict <word> <define = 1>    :: Gets a definition and an example of a <word> from wordnet.\n"
       "similar <w1> <w2>           :: Gets the similarity of <w1> and <w2> in a percentage, which must both be nouns.\n"
       "wiki <name>                 :: Provides a link to a Wikipedia article about <name>.\n"
       "yt <search>                 :: Shows and plays results from a youtube search about <search>.\n"
       "```")


@bot.command(name="user-avatar")  # generates picture of user's avatar
async def user_avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send("{0.mention}\nhttps://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member))


@bot.command(name="user-id")  # shows user's id
async def user_id(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send("{0.mention}: {0.id}".format(member))


@bot.command(name="user-name")  # shows user's name
async def user_name(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send("{0.mention}: {0.name}".format(member))


@bot.command(name="user-status")   # shows user's status
async def user_status(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    if member.status == discord.Status.online:
        await ctx.send("{}: Online".format(member.mention))
    elif member.status == discord.Status.offline:
        await ctx.send("{}: Offline".format(member.mention))
    elif member.status == discord.Status.dnd:
        await ctx.send("{}: Do Not Disturb".format(member.mention))
    else:
        await ctx.send("{}: Idle".format(member.mention))


@bot.command(name="user-joined")  # shows when user joined
async def user_joined(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send("{0.mention}: {0.joined_at}".format(member))


@bot.command(name="user-roles")  # shows user's roles
async def user_roles(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    roles = member.roles
    del roles[0]

    await ctx.send(member.mention + ':')
    for role in roles:
        await ctx.send(role)


@bot.command(name="user-toprole")  # shows user's top role
async def user_toprole(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await ctx.send("{0.mention}: {0.top_role}".format(member))


@bot.command(name="user-info")  # shows all user's info
async def user_info(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Color.blue())
    embed.add_field(name="Name: ", value=member.name, inline=False)
    embed.add_field(name="ID: ", value=member.id, inline=False)
    embed.add_field(name="Status: ", value=member.status, inline=False)
    embed.add_field(name="Joined: ", value=member.joined_at, inline=False)
    embed.add_field(name="Top Role: ", value=member.top_role, inline=False)
    embed.add_field(name="Avatar URL: ", value=member.avatar_url, inline=False)

    await ctx.send(embed=embed)


@bot.command(name="user-list")  # shows server's members
async def user_list(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    for member in ctx.message.guild.members:
        embed.add_field(name=member, value=member.top_role, inline=False)

    await ctx.send(embed=embed)


"""CONFIG"""


@bot.command()  # clears inputted channel
async def clear(ctx, amount):
        #return await ctx.send("**You must have manage channels permissions.**")
    if amount in tuple(range(1, 501)):
        await ctx.channel.purge(limit=amount)
    else:
        return await ctx.send("`amount` **must be an integer from 1 to 500.**")


@clear.error
async def on_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("`amount` **must be an integer from 1 to 500.**")


"""FUN"""


@bot.command()  # bot says a joke
async def joke(ctx, type):
    if type.lower() == "ym":
        yo_momma = ("fat, I took a picture of her last Christmas and it's still printing.",
                    "fat when she got on the scale it said, 'I need your weight not your phone number.'",
                    "fat and old when God said, 'Let there be light', he asked your mother to move out of the way.",
                    "fat she doesn't need the internet, because she's already world wide.",
                    "fat, when she sat on an iPod, she made the iPad!",
                    "fat she walked past the TV and I missed 3 episodes.",
                    "ugly when she tried to join an ugly contest they said, 'Sorry, no professionals.'",
                    "ugly she made One Direction go another direction.",
                    "ugly Fix-It Felix said, 'I can\'t fix it.'"
                    "stupid when an intruder broke into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldn't find the 'CALL' button.",
                    "stupid she stuck a battery up her ass and said, 'I GOT THE POWER!'",
                    "stupid that she sat on the TV to watch the couch.")
        await ctx.send("**Hey {}**, Yo momma so {}".format(ctx.message.author.name, random.choice(yo_momma)))
    elif type.lower() == "kk":
        await ctx.send("Knock Knock.")

        if ctx.message.author == bot.user:
            return

        wt_response = await bot.wait_for("message", timeout=10)
        if wt_response is None:
            await ctx.send("**Sorry, you took too long.**")
        elif wt_response.content.lower() in ("who's there", "who's there?"):
            kk = [["A little old lady", "All this time, I did not know you could yodel."],
                  ["Cow says", "Cow says mooooo!"],
                  ["Etch", "Bless you, friend."],
                  ["Robin", "Now hand over the cash."],
                  ["Cash", "No thanks, I'll have some peanuts."],
                  ["Mustache", "I mustache you a question, but I'll shave it for later."],
                  ["Tank", "You're welcome."],
                  ["Candice", "Candice door open, or what?"],
                  ["Boo", "No need to cry, it's only a joke."],
                  ["Howl", "Howl you know unless you open this door?"],
                  ["Iran", "Iran all the way here. Let me in already!"]]

            joke_num = random.randint(0, 9)
            chosen_joke = [kk[joke_num][0], kk[joke_num][1]]
            await ctx.send(chosen_joke[0])

            xwho_response = await bot.wait_for("message", timeout=20)
            if xwho_response is None:
                await ctx.send("**Sorry, you took too long.**")
            elif xwho_response.content in ("{} who".format(chosen_joke[0]), "{} who?".format(chosen_joke[0])):
                await ctx.send(chosen_joke[1])
            else:
                await ctx.send("**Must reply with '{0} who or '{0} who?'.**".format(chosen_joke[0]))
        else:
            await ctx.send("**You must answer with** `who\'s there` **or** `who\'s there?`**.**")
    else:
        await ctx.send("**Not a joke type.** `type` **must be** `ym` **or** `kk`**.**")


@bot.command()
async def rps(ctx):
    await ctx.send("Welcome to Rock, Paper, Scissors. **Please select a weapon: (`rock`, `paper`, `scissors`).**")

    choices = ("rock", "paper", "scissors")

    computer = random.choice(choices)
    player = await bot.wait_for("message", timeout=10)
    if player.content.lower() not in choices:
        return await ctx.send("**That is not a valid choice.**")

    beats = {
        "rock": ["paper"],
        "paper": ["scissors"],
        "scissors": ["rock"]
    }

    if player.content.lower() == computer:
        await ctx.send("**Tie!** You both chose {}.".format(computer))
    elif player.content.lower() in beats[computer]:
        await ctx.send("**You win!** You chose {}, Computer chose {}.".format(player.content, computer))
    else:
        await ctx.send("**You lose!** You chose {}, Computer chose {}.".format(player.content, computer))


@bot.command(name="guess-num")
async def guess_num(ctx):
    try:
        await ctx.send("Pick an integer between 1 and 100.")
        if ctx.message.author == bot.user:
            return

        try:
            guess = await bot.wait_for("message", timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("**Sorry, {}, you took too long.**".format(ctx.message.author.mention))

        answer = random.randint(1, 100)
        counter = 0
        while True:
            if ctx.message.author == bot.user:
                return

            counter += 1
            if int(guess.content) not in tuple(range(1, 101)):
                await ctx.send("**Must pick an integer between 1 and 100.**")
                counter -= 1
            elif int(guess.content) > answer:
                await ctx.send("**Your guess is too high. Guess again.**")

                try:
                    guess = await bot.wait_for("message", timeout=10.0)
                except asyncio.TimeoutError:
                    return await ctx.send("**Sorry, {}, you took too long.**".format(ctx.message.author.mention))
            elif int(guess.content) < answer:
                await ctx.send("**Your guess is too low. Guess again.**")

                try:
                    guess = await bot.wait_for("message", timeout=10.0)
                except asyncio.TimeoutError:
                    return await ctx.send("**Sorry, {}, you took too long.**".format(ctx.message.author.mention))
            else:
                if counter <= 1:
                    return await ctx.send("**Congratulations!** You got it on your first attempt.")
                else:
                    return await ctx.send("**You are correct!** It took you {} attempts to get it.".format(counter))
    except ValueError:
        await ctx.send("**Not an integer between 1 and 100.**")


@bot.command()
async def roast(ctx, member: discord.Member):
    roasts = ("I'd give you a nasty look, but you've already got one.",
              "I love what you’ve done with your hair. How do you get it to come out of the nostrils like that?",
              "It looks like your face caught fire and someone tried to put it out with a hammer.",
              "Just because you have one doesn’t mean you need to act like one.",
              "I’m sorry, was I meant to be offended? The only thing offending me is your face.",
              "You are proof that evolution can go in reverse.",
              "I thought of you today. It reminded me to take the garbage out",
              "I’d slap you but I don’t want to make your face look any better.",
              "Were you born on the highway? That is where most accidents happen.",
              "Shut up, you'll never be the man your mother is.")
    await ctx.send("Hey {}, {}\n🔥🔥🔥😝😝".format(member.mention, random.choice(roasts)))


@bot.command()
async def emoji(ctx, type):
    if type == "frozen":
        await ctx.send("The ❄️ 🌟 🔦 ⚪ on the mountain 🌙 🌠. 🙅🏻 a👣 to 🐝 👀. A 🏰 of 😢, and it 👀\n"
                       "like☝️️ the 👑. The 💨 is 🐺 like this 🌀 ❄️ ☔️ 🏠. 🙅🏻 keep it in, ☁️ 💡 ☝️️ tried. 🙅🏻 let\n"
                       "👬👫 in,🙅🏻 let 👬👫 👀. 🐝 the 👍 👧 👇 always have to 🐝. 🙅🏻, don't 👐, 🚫 let 👬\n"
                       "👫💡. Well now 👬👫 💡. 👐 it 🚗,, 👐 it 🚗,,🙅🏻 ✊ it back anymore. 👐 it 🚗,, 👐 it\n"
                       "🚗, turn ✈️ and 🔨 the 🚪. ☝️️ 🚫 care, what 👬👫 going to 👄, let the ☔️ ⚡ ❄️ 😡\n"
                       "on, the ❄️ ⛄️ 🙅🏻 bothered ☝️️ anyway. It's 😜😂 how some ✈️ 🚆 makes everything\n"
                       "😳 🐜. And the 😱 that once 👮 me, 🙅🏻 get to☝️️ at all. It's 🕓 to 👀 what☝️️ can do. To\n"
                       "📝 the 📊 and 🔨 through. 🚫 👍 , 🚫 👎, 🚫 👮 for ☝️️. ☝️️ 🏃. 👐 it 🚗,, 👐 it 🚗., ☝️\n"
                       "am ☝️ with the 🌀 and 🌌. 👐 it 🚗,, 👐 it 🚗..👇 🙅🏻 👀 ☝️️ 😭 . 👉 ☝️️ 🚶, and 👉 ☝️\n"
                       "stay. Let the⚡ ❄️ 😡 on. ☝️️ 💪 ❄️ through the 🌀 into the 🌎.☝️️ 👤 is 🌀 in ❄️ ⛄️\n"
                       "fractals all 🔁. And 1️⃣💡 💎 like an ❄️ 📢. ☝️️ 🙅🏻 🏃 back, the past is in the past. 👐 it\n"
                       "🚗,,👐 it 🚗,. And ☝️️ 🚀 like the 💔 of 🌌. 👐 it 🚗,, 👐 it 🚗.. That 💁 is 🚫. Here\n"
                       "☝️️ 🚶, in the 🔦 of ☀️. Let the ⚡ ❄️ 😡 on, the ❄️ ⛄️ 🙅🏻 bothered ☝️️ anyway.")
    elif type == "up":
        await ctx.send("⁣          🎈🎈  ☁️\n"
                       "         🎈🎈🎈\n"
                       " ☁️   🎈🎈🎈🎈\n"
                       "       🎈🎈🎈🎈\n"
                       "   ☁️   ⁣🎈🎈🎈\n"
                       "             | | |\n"
                       "             🏠   ☁️\n"
                       "   ☁️         ☁️\n"
                       "🌳🌹🏫🌳🏢🏢_🏢🏢🌳🌳")
    elif type == "dirty":
        if not ctx.channel.is_nsfw():
            return await ctx.send("**You can't use this command here.**")

        await ctx.send("☝️️       👨\n"
                       "🐛💤👔 🐛\n"
                       "             ⛽️     👢\n"
                       "              ⚡️ 8=👊 =D💦\n"
                       "       🎺      🍗                💦\n"
                       "       👢        👢                 🙆🏻")
    elif type == "chess":
        await ctx.send("🏰🏇⛪👸👱⛪🏇🏰\n"
                       "😶😶😶😶😶😶😶😶\n"
                       "🔳🔲🔳🔲🔳🔲🔳🔲\n"
                       "🔳🔲🔳🔲🔳🔲🔳🔲\n"
                       "🔳🔲🔳🔲🔳🔲🔳🔲\n"
                       "🔳🔲🔳🔲🔳🔲🔳🔲\n"
                       "👶👶👶👶👶👶👶👶\n"
                       "🏃🐴👼👰🙇👼🐴🏃")



"""UTILITIES"""


yt_api_key = "AIzaSyBR68aLaWlBarv_g-ND8afn_JnSSjqdU4w"  # youtube api-key

@bot.command(name="PvsT")  # Calculates sub count of pewdiepie and T-Series
async def pewdiepie_vs_tseries(ctx):
    pew_name = "pewdiepie"
    t_name = "tseries"

    pew_data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + pew_name + "&key=" + yt_api_key).json()
    t_data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + t_name + "&key=" + yt_api_key).json()

    pew_subs = pew_data["items"][0]["statistics"]["subscriberCount"]
    t_subs = t_data["items"][0]["statistics"]["subscriberCount"]

    await ctx.send("**Pewdiepie:** {} Subscribers\n**T-Series:**    {} Subscribers".format(pew_subs, t_subs))


@bot.command(name="sub-count")  # gets sub count of any youtuber
async def sub_count(ctx, username):
    try:
        user_data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username.lower() + "&key=" + yt_api_key).json()
        user_subs = user_data["items"][0]["statistics"]["subscriberCount"]

        await ctx.send("**{}**: {}".format(username, user_subs))
    except IndexError:
        await ctx.send("**Not a valid username.**")


@bot.command(name="view-count")  # gets view count of any youtuber
async def view_count(ctx, username):
    try:
        user_data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username.lower() + "&key=" + yt_api_key).json()
        user_views = user_data["items"][0]["statistics"]["viewCount"]

        await ctx.send("**{}**: {}".format(username, user_views))
    except IndexError:
        await ctx.send("**Not a valid username.**")


@bot.command(name="video-count")  # gets video count of any youtuber
async def video_count(ctx, username):
    try:
        user_data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username.lower() + "&key=" + yt_api_key).json()
        user_videos = user_data["items"][0]["statistics"]["videoCount"]

        await ctx.send("**{}**: {}".format(username, user_videos))
    except IndexError:
        await ctx.send("**Not a valid username.**")


@bot.command()  # gets bitcoin value in a currency type
async def bitcoin(ctx, currency="CAD"):
    try:
        bitcoin_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        currency_data = requests.get("https://api.exchangeratesapi.io/latest").json()
        fullname_data = requests.get("https://gist.githubusercontent.com/Fluidbyte/2973986/raw/b0d1722b04b0a737aade2ce6e055263625a0b435/Common-Currency.json").json()
        base_currency = bitcoin_data["bpi"]["EUR"]["rate"].replace(',', '')

        if currency.upper() == "EUR":
            value = float(base_currency)
        else:
            value = float(base_currency) * float(currency_data["rates"][currency.upper()])
        await ctx.send("**{}:** ${}".format(fullname_data[currency.upper()]["name"], round(value, 2)))
    except KeyError:
        await ctx.send("`{}` **is not a valid currency type.**".format(currency))


@bot.command()  # gets the forecast of a specific city
async def forecast(ctx, city, data):
    try:
        forecast_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=8284a846ac560add042f60ab4c7ce7e0".format(city.capitalize())).json()

        if data.lower() == "temp":
            await ctx.send("**Temperature:** {}°C".format(round(float(forecast_data["main"]["temp"]) - 273.15, 1)))
            await ctx.send("**Low:** {}°C".format(round(float(forecast_data["main"]["temp_min"]) - 273.15, 1)))
            await ctx.send("**High:** {}°C".format(round(float(forecast_data["main"]["temp_max"]) - 273.15, 1)))
        elif data.lower() == "weather":
            await ctx.send("**Weather:** {} ({})".format(forecast_data["weather"][0]["main"], forecast_data["weather"][0]["description"]))
        elif data.lower() == "air":
            await ctx.send("**Humidity:** {}%".format(round(float(forecast_data["main"]["humidity"]), 1)))
            await ctx.send("**Wind Speed:** {} km/h".format(round(float(forecast_data["wind"]["speed"]), 1)))
        else:
            await ctx.send("`{}` **is not a valid data. (**`data` **=** `temp`**,** `weather`**,** `air` **|** `city` = **name of city**)".format(data))
    except KeyError:
        await ctx.send("`{}` **is not a city name.**".format(city))


@forecast.error  # error handling for forecast command
async def on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Must enter** `city` **and** `data` **parameters.**")


@bot.command()  # gets a definition of a word from the urban dictionary
async def urban(ctx, word, define = 1):
    try:
        if not ctx.channel.is_nsfw():
            return await ctx.send("**You can't use this command here.**")

        urban_data = requests.get("http://urbanscraper.herokuapp.com/search/{}".format(word.lower())).json()

        await ctx.send("**Definition:** {}".format(urban_data[define - 1]["definition"]))
        await ctx.send("**Example:** {}".format(urban_data[define - 1]["example"]))
        await ctx.send("**Link:** {}".format(urban_data[define - 1]["url"]))
    except KeyError:
        await ctx.send("`{}` **is not a word.**".format(word))
    except IndexError:
        await ctx.send("**Definition number is not valid.**")


@urban.error  # error handling for urban command
async def on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Must enter** `word` **parameter.**")


@bot.command()  # gets a definition from the google dictionary
async def dict(ctx, word = None, define = 1):
    try:
        if word is None:
            return await ctx.send("**Must enter a word.**")

        syns = wordnet.synsets(word.lower())

        await ctx.send("**Definition:** {}".format(syns[define - 1].definition()))
        await ctx.send("**Example:** {}".format(syns[define - 1].examples()[0]))
    except IndexError:
        await ctx.send("**Not a valid word |** `define` **is out of range.**")


@bot.command()  # gets the theoretical similaarity of two words
async def similar(ctx, w1 = None, w2 = None):
    if w1 is None or w2 is None:
        return await ctx.send("**Must enter two parameters.**")

    wn1 = wordnet.synset("{}.n.01".format(w1))
    wn2 = wordnet.synset("{}.n.01".format(w2))

    await ctx.send("{0:.0%} similar.".format(wn1.wup_similarity(wn2)))


@similar.error
async def on_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("**The word(s) is not valid.**")


@bot.command()  # sends the link to a Wikipedia article
async def wiki(ctx, *args):
    name = ""
    for word in args:
        name += word + " "
    name = name[:-1].replace(" ", "_")

    if len(args) == 0:
        await ctx.send("**Must enter a Wikipedia article.**")
        return
    elif requests.get("https://en.wikipedia.org/wiki/{}".format(name)).status_code != 200:
        await ctx.send("**Wikipedia article does not exist.**")
        return

    wiki_data = "https://en.wikipedia.org/wiki/{}".format(name.lower())
    await ctx.send(wiki_data)


@bot.command()
async def yt(ctx, *args):
    search = ""
    for word in args:
        search += word + " "
    search = search.replace(" ", "+")

    yt_url = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&key={}".format(search, yt_api_key)).json()
    if len(yt_url["items"]) == 0:
        await ctx.send("**No results found.**")

    for vid in range(0, 5):
        await ctx.send("**[{}]:** {}".format(vid + 1, yt_url["items"][vid]["snippet"]["title"]))

    await ctx.send("\n*Input the number of the video you wish to choose.*")
    num = await bot.wait_for("message", timeout=10)

    if num is None:
        await ctx.send("**Sorry, you took too long.**")
    elif int(num.content) in (tuple(range(1, 6))):
        await ctx.send("https://www.youtube.com/watch?v={}".format(yt_url["items"][int(num.content) - 1]["id"]["videoId"]))
    else:
        await ctx.send("**You must enter a number between 1 and 5.**")



bot.run(str(os.environ.get("BOT_TOKEN")))  # run the bot
