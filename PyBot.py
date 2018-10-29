import chatterbot
from chatterbot.trainers import ListTrainer as lt
import os

bot = ChatBot('Bot')
bot.set_Trainer(lt)

for files in os.listdir('C:/Users/RAJASEKAR/Downloads/New Project/chatterbot-corpus-master/chatterbot_corpus/data/english'):
	data = open('C:/Users/RAJASEKAR/Downloads/New Project/chatterbot-corpus-master/chatterbot_corpus/data/english'+ files, 'r').readlines()
	bot.train(data)

while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Bot: ', reply)
	if message.strip() == 'Bye':
		print('Bot: Bye')
		break
