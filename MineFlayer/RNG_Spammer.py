# RANDOM USER / RANDOM STRING SPAM SCRIPT

import time
from javascript import require, On
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

import random, string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

BOT_USERNAME = randomword(5)
ADRESS = 'ekipa.pro'
   
bot = mineflayer.createBot({
    'username': BOT_USERNAME,
    'host': ADRESS,
})
@On(bot, 'spawn')
def handle(*args):
	print("SPAM TIME")
	bot.chat('/register lel666 lel666')

@On(bot, 'chat')
def handle(*args):
	time.sleep(6)
	bot.chat(randomword(20));
	time.sleep(3)
