from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import json, os, string, sys, threading, logging, time, re, random
import discord
import openai

##########
#Settings#
##########
#OpenAI API key
openai.api_key = "OPENAI API KEY"

#Discord key
dkey = 'DISCORD KEY'

# Lots of console output
debug = True
# User Session timeout
timstart = 300


#Defaults
user = 'Human'
botname = 'AI'
cache = None
qcache = None
chat_log = None
running = False
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

completion = openai.Completion()

##################
#Command handlers#
##################
def start():
    """Send a message when the command /start is issued."""
    global user
    global chat_log
    global cache
    global qcache
    global running
    global botname
    user = 'Human'
    botname = 'AI'
    chat_log = None
    cache = None
    qcache = None
    running = True
    return

def stop():
    """Send a message when the command /stop is issued."""
    global user
    global chat_log
    global cache
    global qcache
    global running
    global botname
    user = 'Human'
    botname = 'AI'
    chat_log = None
    cache = None
    qcache = None
    running = False
    return

def reset():
    """Send a message when the command /reset is issued."""
    global username
    global botname
    global chat_log
    global cache
    global qcache
    global botname
    username = 'Human'
    botname = 'AI'
    chat_log = None
    cache = None
    qcache = None
    return

def retry(message):
    """Send a message when the command /retry is issued."""
    global chat_log
    global cache
    global qcache
    global running
    global username
    global botname
    new = True
    rep = interact(message, new)
    return rep

################
#Main functions#
################

def run(message):
    global chat_log
    global cache
    global qcache
    global running
    global username
    global botname
    new = False
    rep = interact(message, new)
    return rep

def ask(username, botname, question, chat_log=None):
    if chat_log is None:
        chat_log = username + ': Hello, how are you?\n ' + botname + ': I am doing great. How can I help you today?\n'

    prompt = f'{chat_log}{username}: {question}\n{botname}:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\n'], temperature=0.9,
        top_p=1, frequency_penalty=7, presence_penalty=0.1, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(username, botname, question, answer, chat_log=None):
    if chat_log is None:
        chat_log = username + ': Hello, how are you?\n ' + botname + ': I am doing great. How can I help you today?\n'
    return f'{chat_log}{username}: {question}\n{botname}: {answer}\n'
	
def interact(update, new):
    global chat_log
    global cache
    global qcache
    global botname
    global username
    print("==========START==========")
    tex = update
    text = str(tex)
    analyzer = SentimentIntensityAnalyzer()
    if new != True:
        vs = analyzer.polarity_scores(text)
        if debug == True:
            print("Sentiment of input:\n")
            print(vs)
        if vs['neg'] > 0:
            rep = 'Input text is not positive. Input text must be of positive sentiment/emotion.'
            return rep
    if new == True:
        if debug == True:
            print("Chat_LOG Cache is...")
            print(cache)
            print("Question Cache is...")
            print(qcache)
        chat_log = cache
        question = qcache
    if new != True:
        question = text
        qcache = question
        cache = chat_log
    try:
        print('TEST')
        aka = str(username)
        answer = ask(aka, botname, question, chat_log)
        print('TEST')
        if debug == True:
            print("Input:\n" + question)
            print("Output:\n" + answer)
            print("====================")
        stripes = answer.encode(encoding=sys.stdout.encoding,errors='ignore')
        decoded	= stripes.decode("utf-8")
        out = str(decoded)
        vs = analyzer.polarity_scores(out)
        if debug == True:
            print("Sentiment of output:\n")
            print(vs)
        if vs['neg'] > 0:
            rep = 'Output text is not positive. Censoring. Use /retry to get positive output.'
            return rep
        chat_log = append_interaction_to_chat_log(aka, botname, question, answer, chat_log)
        return out

    except Exception as e:
        print(e)
        errstr = str(e)
        return errstr

#####################
# End main functions#
#####################

def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        global running
        global botname
        global username
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!start'):
            start()
            await message.reply('You have started the bot. Commands are !start, !stop, !character (name of your desired rp partner), and !rp (text)', mention_author=False)
        if message.content.startswith('!stop'):
            stop()
            await message.reply('You have stopped the bot.', mention_author=False)
        if message.content.startswith('!reset'):
            reset()
            await message.reply('You have reset the bot.', mention_author=False)
        if message.content.startswith('!character'):
            botname = re.search(r'(?<=!character ).*[^.]*', message.content)
            name = botname.group(0)
            botname = str(name)
            reply = 'Bot Character Name Is: ' + botname
            await message.reply(reply, mention_author=False)
        if message.content and running == True:
            if message.content.startswith('!retry'):
                conts = 'null'
                rep = retry(conts)
                await message.reply(rep, mention_author=False)
            if message.content.startswith('!rp'):
                content = re.search(r'(?<=!rp ).*[^.]*', message.content)
                cont = content.group(0)
                conts = str(cont)
                username = str(message.author)
                rep = run(conts)
                await message.reply(rep, mention_author=False)

if __name__ == '__main__':
    client = MyClient()
    client.run(dkey)
# https://discord.com/api/oauth2/authorize?client_id=890033105325400075&permissions=68608&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D890033105325400075&scope=bot