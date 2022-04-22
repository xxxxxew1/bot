from array import array
from ast import Constant
from collections import defaultdict
from email import message
from glob import glob
from msilib.schema import PublishComponent
from multiprocessing.dummy import Array
from threading import local
import telebot
import time
import re;

from telebot import types


#5135606281:AAEq-AbXUNNdhoQ85IVt9OgQ-AsVuuq5rs0 //3 bot
bot = telebot.TeleBot('5135606281:AAEq-AbXUNNdhoQ85IVt9OgQ-AsVuuq5rs0')


markup = types.InlineKeyboardMarkup(row_width=3)
markupmain = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup1 = types.InlineKeyboardMarkup(row_width=2)
markup2 = types.InlineKeyboardMarkup(row_width=2)
markups1 = types.InlineKeyboardMarkup(row_width=2)
markups2 = types.InlineKeyboardMarkup(row_width=2)
markups3 = types.InlineKeyboardMarkup(row_width=2)
markups4 = types.InlineKeyboardMarkup(row_width=2)
markups5 = types.InlineKeyboardMarkup(row_width=2)
markups6 = types.InlineKeyboardMarkup(row_width=2)
markups7 = types.InlineKeyboardMarkup(row_width=2)
markups8 = types.InlineKeyboardMarkup(row_width=2)
markups9 = types.InlineKeyboardMarkup(row_width=2)
markups10 = types.InlineKeyboardMarkup(row_width=2)
markups11 = types.InlineKeyboardMarkup(row_width=2)
markups12 = types.InlineKeyboardMarkup(row_width=2)
markups13 = types.InlineKeyboardMarkup(row_width=2)
markups14 = types.InlineKeyboardMarkup(row_width=2)
markups15 = types.InlineKeyboardMarkup(row_width=2)
markups16 = types.InlineKeyboardMarkup(row_width=2)
markups17 = types.InlineKeyboardMarkup(row_width=2)
markups18 = types.InlineKeyboardMarkup(row_width=2)
markups19 = types.InlineKeyboardMarkup(row_width=2)
markups20 = types.InlineKeyboardMarkup(row_width=2)


item12 = types.InlineKeyboardButton("1", callback_data='yes1')
item13 = types.InlineKeyboardButton("2", callback_data='no1')
markups1.add(item12, item13)

item14 = types.InlineKeyboardButton("1", callback_data='yes2')
item15 = types.InlineKeyboardButton("2", callback_data='no2')
markups2.add(item14, item15)

item16 = types.InlineKeyboardButton("1", callback_data='yes3')
item17 = types.InlineKeyboardButton("2", callback_data='no3')
markups3.add(item16, item17)

item18 = types.InlineKeyboardButton("1", callback_data='yes4')
item19 = types.InlineKeyboardButton("2", callback_data='no4')
markups4.add(item18, item19)

item20 = types.InlineKeyboardButton("1", callback_data='yes5')
item21 = types.InlineKeyboardButton("2", callback_data='no5')
markups5.add(item20, item21)

item22 = types.InlineKeyboardButton("1", callback_data='yes6')
item23 = types.InlineKeyboardButton("2", callback_data='no6')
markups6.add(item22, item23)


item24 = types.InlineKeyboardButton("1", callback_data='yes7')
item25 = types.InlineKeyboardButton("2", callback_data='no7')
markups7.add(item24, item25)

item26 = types.InlineKeyboardButton("1", callback_data='yes8')
item27 = types.InlineKeyboardButton("2", callback_data='no8')
markups8.add(item26, item27)

item28 = types.InlineKeyboardButton("1", callback_data='yes9')
item29 = types.InlineKeyboardButton("2", callback_data='no9')
markups9.add(item28, item29)

item30 = types.InlineKeyboardButton("1", callback_data='yes10')
item31 = types.InlineKeyboardButton("2", callback_data='no10')
markups10.add(item30, item31)

item32 = types.InlineKeyboardButton("1", callback_data='yes11')
item33 = types.InlineKeyboardButton("2", callback_data='no11')
markups11.add(item32, item33)

item34 = types.InlineKeyboardButton("1", callback_data='yes12')
item35 = types.InlineKeyboardButton("2", callback_data='no12')
markups12.add(item34, item35)

item36= types.InlineKeyboardButton("1", callback_data='yes13')
item37 = types.InlineKeyboardButton("2", callback_data='no13')
markups13.add(item36, item37)

item38 = types.InlineKeyboardButton("1", callback_data='yes14')
item39 = types.InlineKeyboardButton("2", callback_data='no14')
markups14.add(item38, item39)

item40 = types.InlineKeyboardButton("1", callback_data='yes15')
item41 = types.InlineKeyboardButton("2", callback_data='no15')
markups15.add(item40, item41)

item42 = types.InlineKeyboardButton("1", callback_data='yes16')
item43 = types.InlineKeyboardButton("2", callback_data='no16')
markups16.add(item42, item43)

item44 = types.InlineKeyboardButton("1", callback_data='yes17')
item45 = types.InlineKeyboardButton("2", callback_data='no17')
markups17.add(item44, item45)

item46 = types.InlineKeyboardButton("1", callback_data='yes18')
item47 = types.InlineKeyboardButton("2", callback_data='no18')
markups18.add(item46, item47)

item48 = types.InlineKeyboardButton("1", callback_data='yes19')
item49 = types.InlineKeyboardButton("2", callback_data='no19')
markups19.add(item48, item49)

item50 = types.InlineKeyboardButton("1", callback_data='yes20')
item51 = types.InlineKeyboardButton("2", callback_data='no20')
markups20.add(item50, item51)

#item12 = types.InlineKeyboardButton("Да", callback_data='yes1')
#item13 = types.InlineKeyboardButton("Нет", callback_data='no1')
#markups1.add(item12, item13)

		


#chatid = message.from_user.id
#user_id = chatid

global user_id
user_id = []
global pr
pr = []
global tech
tech = []
global peopl
peopl = []
global syste
syste = []
global hud
hud = []

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id not in user_id:
        user_id.append(message.from_user.id)
        pr.append(0)
        tech.append(0)
        peopl.append(0)
        syste.append(0)
        hud.append(0)
    else:
        for i in range (len(user_id)):
            if message.from_user.id == user_id[i]:
                pr[i] = 0
                tech[i] = 0
                peopl[i] = 0
                syste[i] = 0
                hud[i] = 0
    
    bot.send_message(message.chat.id, "Здравствуй, {0.first_name}!\nПредлагаем вам 20 пар утверждений. Внимательно прочитав оба утверждения, выберите то, которое больше соответствует вашему желанию. Выбор нужно сделать в каждой паре утверждений".format(message.from_user, bot.get_me()),parse_mode='html')
    bot.send_message(message.chat.id, "Ответьте на вопрос: «Мне нравится…»")
    #bot.send_message(message.chat.id, user_id[i])
    print(user_id)
    bot.send_message(message.chat.id, "Мне нравится: \n1.Ухаживать за животными\n2.Обслуживать машины, приборы (следить, регулировать)", reply_markup=markups1)
    

@bot.message_handler(content_types=['text'])
def tgbot(message):
	bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

def find_user_id(message):
	return message.chat.id

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

	try:
		if call.message:
			#user_id = call.message.chat.id
			
			#bot.send_message(call.message.chat.id, sum[i])
			
			if call.data == 'yes1':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Помогать больным людям, лечить их\n2.Составлять таблицы, схемы, программы вычислительных машин", delete(call.message), reply_markup=markups2)
				#pr[i] = pr[i] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						pr[i] = pr[i] + 1
					else:
						print(call.message.from_user.id," ",user_id[i])
				#delete(call.message)
			
			if call.data == 'no1':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Помогать больным людям, лечить их\n2.Составлять таблицы, схемы, программы вычислительных машин", delete(call.message), reply_markup=markups2)
				#tech[i] = tech[i] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)

			if call.data == 'yes2':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок\n2.Следить за состоянием, развитием растений", delete(call.message), reply_markup=markups3)
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("yes2")
						peopl[i] = peopl[i] + 1
				#delete(call.message)
			
			if call.data == 'no2':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок\n2.Следить за состоянием, развитием растений", delete(call.message),reply_markup=markups3)
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no2")
						syste[i] = syste[i] + 1
				#delete(call.message)

			if call.data == 'yes3':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обрабатывать материалы (дерево, ткань, пластмассу и т.д.)\n2.Доводить товары до потребителя (рекламировать, продавать).", delete(call.message), reply_markup=markups4)
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("yes3")
						hud[i] = hud[i] + 1

				#delete(call.message)
			
			if call.data == 'no3':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обрабатывать материалы (дерево, ткань, пластмассу и т.д.)\n2.Доводить товары до потребителя (рекламировать, продавать).", delete(call.message), reply_markup=markups4)
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no3")
						pr[i] = pr[i] + 1
				#delete(call.message)
			#print(pr[i],tech[i],syste[i],peopl[i],hud[i])

			if call.data == 'yes4':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обсуждать научно-популярные книги, статьи \n2.Обсуждать художественные книги", delete(call.message), reply_markup=markups5)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)
			
			if call.data == 'no4':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обсуждать научно-популярные книги, статьи \n2.Обсуждать художественные книги", delete(call.message), reply_markup=markups5)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)

			if call.data == 'yes5':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Выращивать молодняк животных какой-либо породы \n2.Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных", delete(call.message), reply_markup=markups6)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)
			
			if call.data == 'no5':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Выращивать молодняк животных какой-либо породы \n2.Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных", delete(call.message), reply_markup=markups6)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)

			if call.data == 'yes6':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Копировать рисунки, изображения, настраивать музыкальные инструменты \n2.Управлять каким-либо грузовым, подъёмным, транс портным средством (подъёмным краном, машиной и т.п.)", delete(call.message), reply_markup=markups7)
				#pr[user_id] = pr[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						pr[i] = pr[i] + 1
				#delete(call.message)
			
			if call.data == 'no6':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Копировать рисунки, изображения, настраивать музыкальные инструменты \n2.Управлять каким-либо грузовым, подъёмным, транс портным средством (подъёмным краном, машиной и т.п.)", delete(call.message), reply_markup=markups7)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)
			
			if call.data == 'yes7':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Сообщать, разъяснять людям нужные для них сведения в справочном бюро, во время экскурсии и т.д. \n2.Художественно оформлять выставки, витрины, участвовать в подготовке концертов, пьес и т.п.", delete(call.message), reply_markup=markups8)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)
			
			if call.data == 'no7':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Сообщать, разъяснять людям нужные для них сведения в справочном бюро, во время экскурсии и т.д. \n2.Художественно оформлять выставки, витрины, участвовать в подготовке концертов, пьес и т.п.", delete(call.message), reply_markup=markups8)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)
			
			if call.data == 'yes8':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Ремонтировать изделия, вещи (одежду, технику), жилище\n2.Искать и исправлять ошибки в текстах, таблицах, рисунках", delete(call.message), reply_markup=markups9)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)
			
			if call.data == 'no8':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Ремонтировать изделия, вещи (одежду, технику), жилище\n2.Искать и исправлять ошибки в текстах, таблицах, рисунках", delete(call.message), reply_markup=markups9)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)

			if call.data == 'yes9':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Лечить животных\n2.Выполнять расчёты, вычисления", delete(call.message), reply_markup=markups10)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)
			
			if call.data == 'no9':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Лечить животных\n2.Выполнять расчёты, вычисления", delete(call.message), reply_markup=markups10)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)

			if call.data == 'yes10':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Выводить новые сорта растений \n2.Конструировать новые виды промышленных изделий (машины, одежду, дома и т.д.) ", delete(call.message), reply_markup=markups11)
				#pr[user_id] = pr[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						pr[i] = pr[i] + 1
				#delete(call.message)
			
			if call.data == 'no10':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Выводить новые сорта растений \n2.Конструировать новые виды промышленных изделий (машины, одежду, дома и т.д.) ", delete(call.message), reply_markup=markups11)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)

			if call.data == 'yes11':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать \n2.Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок) ", delete(call.message), reply_markup=markups12)
				#pr[user_id] = pr[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						pr[i] = pr[i] + 1
				#delete(call.message)
			
			if call.data == 'no11':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать \n2.Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок) ", delete(call.message), reply_markup=markups12)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)

			if call.data == 'yes12':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Наблюдать, изучать работу кружков художественной самодеятельности \n2.Наблюдать, изучать жизнь микробов ", delete(call.message), reply_markup=markups13)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)
			
			if call.data == 'no12':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Наблюдать, изучать работу кружков художественной самодеятельности \n2.Наблюдать, изучать жизнь микробов ", delete(call.message), reply_markup=markups13)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)

			if call.data == 'yes13':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обслуживать, налаживать медицинские приборы и аппараты \n2.Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п ", delete(call.message), reply_markup=markups14)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)
			
			if call.data == 'no13':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Обслуживать, налаживать медицинские приборы и аппараты \n2.Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п ", delete(call.message), reply_markup=markups14)
				#pr[user_id] = pr[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						pr[i] = pr[i] + 1
				#delete(call.message)

			if call.data == 'yes14':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др \n2.Художественно описывать, изображать события наблюдаемые или представляемые ", delete(call.message), reply_markup=markups15)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)
			
			if call.data == 'no14':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др \n2.Художественно описывать, изображать события наблюдаемые или представляемые ", delete(call.message), reply_markup=markups15)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)

			if call.data == 'yes15':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Делать лабораторные анализы в больнице \n2.Принимать, осматривать больных, беседовать с ними, назначать лечение ", delete(call.message), reply_markup=markups16)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)
			
			if call.data == 'no15':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Делать лабораторные анализы в больнице \n2.Принимать, осматривать больных, беседовать с ними, назначать лечение ", delete(call.message), reply_markup=markups16)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)

			if call.data == 'yes16':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Красить или расписывать стены помещений, поверхность изделий \n2.Осуществлять монтаж здания или сборку машин, приборов ", delete(call.message), reply_markup=markups17)
				#pr[user_id] = pr[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						pr[i] = pr[i] + 1
				#delete(call.message)
			
			if call.data == 'no16':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Красить или расписывать стены помещений, поверхность изделий \n2.Осуществлять монтаж здания или сборку машин, приборов ", delete(call.message), reply_markup=markups17)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)

			if call.data == 'yes17':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Организовывать культ походы людей в театры, музеи, на экскурсии, в туристические путешествия и т.п \n2.Играть на сцене, принимать участие в концертах ", delete(call.message), reply_markup=markups18)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)
			
			if call.data == 'no17':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Организовывать культ походы людей в театры, музеи, на экскурсии, в туристические путешествия и т.п \n2.Играть на сцене, принимать участие в концертах ", delete(call.message), reply_markup=markups18)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)

			if call.data == 'yes18':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Изготовлять по чертежам детали, изделия (машины, одежду), строить здания \n2.Заниматься черчением, копировать карты, чертежи ", delete(call.message), reply_markup=markups19)
				#peopl[user_id] = peopl[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						peopl[i] = peopl[i] + 1
				#delete(call.message)
			
			if call.data == 'no18':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Изготовлять по чертежам детали, изделия (машины, одежду), строить здания \n2.Заниматься черчением, копировать карты, чертежи ", delete(call.message), reply_markup=markups19)
				#hud[user_id] = hud[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						hud[i] = hud[i] + 1
				#delete(call.message)

			if call.data == 'yes19':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Вести борьбу с болезнями растений, с вредителями леса, сада \n2.Работать на машинах (пишущая машина, компьютер, телетайп, телефакс) ", delete(call.message), reply_markup=markups20)
				#tech[user_id] = tech[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						tech[i] = tech[i] + 1
				#delete(call.message)
			
			if call.data == 'no19':
				bot.send_message(call.message.chat.id, "Мне нравится: \n1.Вести борьбу с болезнями растений, с вредителями леса, сада \n2.Работать на машинах (пишущая машина, компьютер, телетайп, телефакс) ", delete(call.message), reply_markup=markups20)
				#syste[user_id] = syste[user_id] + 1
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						#print("no1")
						syste[i] = syste[i] + 1
				#delete(call.message)

			if call.data == 'yes20':
				#print("no11")
				for i in range (len(user_id)):
					#print("no12")
					if(find_user_id(call.message) == user_id[i]):
						#print("no13")
						pr[i] = pr[i] + 1
						#bot.send_message(call.message.chat.id,user_id[i])
						#bot.send_message(call.message.chat.id,pr[i])
						#bot.send_message(call.message.chat.id,tech[i])
						#bot.send_message(call.message.chat.id,peopl[i])
						#bot.send_message(call.message.chat.id,syste[i])
				delete(call.message)
				
				img1 = "https://ibb.co/Jqyg1JN" #Priroda/technika
				img2 = "https://ibb.co/vL1MgSs" #technika
				img3 = "https://ibb.co/wJTnGx3" #technika
				img4 = "https://ibb.co/rp6fWNL" #Priroda/technika
				img5 = "https://ibb.co/3r4FxLz" #system
				img6 = "https://ibb.co/PFMvKkb" #hyd
				img7 = "https://ibb.co/sqD2sbk" #people
				img8 = "https://ibb.co/V3ByxmM" #people/hud
				img9 = "https://ibb.co/L839Gnn" #people
				img10 = "https://ibb.co/t8BgkzR" #technika
				bot.send_message(call.message.chat.id,user_id[i])
				bot.send_message(call.message.chat.id,pr[i])
				bot.send_message(call.message.chat.id,tech[i])
				bot.send_message(call.message.chat.id,peopl[i])
				bot.send_message(call.message.chat.id,syste[i])
				bot.send_message(call.message.chat.id,"Специальности которые вам подойдут")
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == pr[i] and max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == tech[i]):
							bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img2, caption='Техническая эксплуатация и обслуживание электрического и электромеханического оборудования \n\nВыпускники этой специальности квалифицированные специалисты, которые совершают ремонт устройств электроснабжения. Они предотвращают или устраняют неполадки в электрических приборах, проводят профилактические осмотры электрических аппаратов, производят измерения и несложные электрические расчеты, изготавливают электротехнические схемы монтажа и сборки.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img3, caption=' Монтаж, техническое обслуживание и ремонт промышленного оборудования \n\nСпециалисты этого профиля выполняют монтаж, техническое обслуживание и ремонт промышленного оборудования. Для выполнения своих должностных обязанностей выпускники должны владеть знаниями основных законов электротехники, изучить физические, технические и промышленные основы электроники. Учащиеся в процессе обучения знакомятся с устройством электронной техники, получают навык работы с инструментами и контрольно-измерительными приборами, которые необходимы для проведения технического обслуживания и ремонта оборудования. Студенты изучают основы метрологии, сертификации и стандартизации, а также знакомятся с методами диагностирования промышленного оборудования и дефектации его элементов. Для будущих специалистов необходим опыт проведения работ по восстановлению работоспособности оборудования с соблюдением техники безопасности и норм бережливого производства.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img10, caption='Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей \n\nСпециальность, выпускник которой владеет навыками не только грамотной эксплуатации автомобилей, но и может организовывать технологические процессы обслуживания и ремонта. В процессе обучения студент овладевает компетенциями, которые в дальнейшей трудовой деятельности позволят ему иметь конкурентное преимущество на рынке труда.')
							time.sleep(5)
						else:
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == pr[i]):
								bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == tech[i]):
								bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img2, caption='Техническая эксплуатация и обслуживание электрического и электромеханического оборудования \n\nВыпускники этой специальности квалифицированные специалисты, которые совершают ремонт устройств электроснабжения. Они предотвращают или устраняют неполадки в электрических приборах, проводят профилактические осмотры электрических аппаратов, производят измерения и несложные электрические расчеты, изготавливают электротехнические схемы монтажа и сборки.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img3, caption='Монтаж, техническое обслуживание и ремонт промышленного оборудования \n\nСпециалисты этого профиля выполняют монтаж, техническое обслуживание и ремонт промышленного оборудования. Для выполнения своих должностных обязанностей выпускники должны владеть знаниями основных законов электротехники, изучить физические, технические и промышленные основы электроники. Учащиеся в процессе обучения знакомятся с устройством электронной техники, получают навык работы с инструментами и контрольно-измерительными приборами, которые необходимы для проведения технического обслуживания и ремонта оборудования. Студенты изучают основы метрологии, сертификации и стандартизации, а также знакомятся с методами диагностирования промышленного оборудования и дефектации его элементов. Для будущих специалистов необходим опыт проведения работ по восстановлению работоспособности оборудования с соблюдением техники безопасности и норм бережливого производства.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img10, caption='Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей \n\nСпециальность, выпускник которой владеет навыками не только грамотной эксплуатации автомобилей, но и может организовывать технологические процессы обслуживания и ремонта. В процессе обучения студент овладевает компетенциями, которые в дальнейшей трудовой деятельности позволят ему иметь конкурентное преимущество на рынке труда.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
								time.sleep(5)
								bot.send_message(call.message.chat.id, 'Электрические машины и аппараты \n\nВ процессе обучения студенты знакомятся с принципами работы, конструкцией, технологией изготовления и правилами эксплуатации электрических машин и аппаратов, порядком проектирования, производства и ремонта электромеханических устройств и систем, принципами автоматического управления электроприводом, работой электрических станций и т. д. Для специалистов данной специальности всегда достаточно высокий и устойчивый спрос на рынке труда.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == peopl[i]):
								bot.send_photo(call.message.chat.id, img7, caption='Дошкольное образование \n\nПедагог дошкольного образования – это специалист, осуществляющий всестороннее развитие психических и физических качеств детей в соответствии с возрастными и индивидуальными особенностями, а также подготавливающий их к последующей учебной деятельности.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img8, caption='Технология парикмахерского искусства \n\nПарикмахер-модельер – специалист, который осуществляет разнообразные процедуры, связанные с моделированием причесок, уходом за волосами и кожей головы, в круг обязанностей которого входит мытье и массаж головы, стрижка волос (простая и модельная), укладка волос, завивка волос.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img9, caption='Преподавание в начальных классах \n\nУчитель начальных классов – педагог, занимающийся обучением и воспитанием детей младшего школьного возраста (1-4 классы). Он осуществляет целостный педагогический процесс в соответствии с образовательными программами начальной школы. Ключевой целью деятельности учителя начальных классов является формирования главной способности у учащихся: научиться учиться')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == syste[i]):
								bot.send_photo(call.message.chat.id, img5, caption='Информационные системы и программирование \n\nСпециальность информационные системы и программирование изучает вопросы, связанные разработкой операционных систем, интерфейсов к распределенным базам данных; вопросы проектирования и сопровождения, программное и информационное обеспечение компьютерных систем с использованием современных средств вычислительной техники, телекоммуникаций и технологий автоматизированного проектирования. Вас научат подготавливать необходимые данные и составлять технические задания на проектирование автоматизированных систем управления, проводить анализ рынков информационных технологий, поиску и оптимальному выбору программных и аппаратных средств управления, осуществлять анализ, проектирование и разработку сайтов.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == hud[i]):
								bot.send_photo(call.message.chat.id, img8, caption='Технология парикмахерского искусства \n\nПарикмахер-модельер – специалист, который осуществляет разнообразные процедуры, связанные с моделированием причесок, уходом за волосами и кожей головы, в круг обязанностей которого входит мытье и массаж головы, стрижка волос (простая и модельная), укладка волос, завивка волос.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img6, caption='Поварское и кондитерское дело \n\nСпециалист по поварскому и кондитерскому делу относится к категории специалистов среднего звена, который занимается организацией и ведением процессов приготовления, оформлением и подготовкой к реализации горячих блюд, кулинарных изделий, закусок сложного ассортимента с учетом потребностей различных категорий потребителей, видов и форм обслуживания.')
			
			if call.data == 'no20':
				#print("no11")
				for i in range (len(user_id)):
					#print("no12")
					if(find_user_id(call.message) == user_id[i]):
						#print("no13")
						syste[i] = syste[i] + 1
						#bot.send_message(call.message.chat.id,user_id[i])
						#bot.send_message(call.message.chat.id,pr[i])
						#bot.send_message(call.message.chat.id,tech[i])
						#bot.send_message(call.message.chat.id,peopl[i])
						#bot.send_message(call.message.chat.id,syste[i])
				delete(call.message)
				
				img1 = "https://ibb.co/Jqyg1JN" #Priroda/technika
				img2 = "https://ibb.co/vL1MgSs" #technika
				img3 = "https://ibb.co/wJTnGx3" #technika
				img4 = "https://ibb.co/rp6fWNL" #Priroda/technika
				img5 = "https://ibb.co/3r4FxLz" #system
				img6 = "https://ibb.co/PFMvKkb" #hyd
				img7 = "https://ibb.co/sqD2sbk" #people
				img8 = "https://ibb.co/V3ByxmM" #people/hud
				img9 = "https://ibb.co/L839Gnn" #people
				img10 = "https://ibb.co/t8BgkzR" #technika
				bot.send_message(call.message.chat.id,user_id[i])
				bot.send_message(call.message.chat.id,pr[i])
				bot.send_message(call.message.chat.id,tech[i])
				bot.send_message(call.message.chat.id,peopl[i])
				bot.send_message(call.message.chat.id,syste[i])
				bot.send_message(call.message.chat.id,"Специальности которые вам подойдут")
				for i in range (len(user_id)):
					if(find_user_id(call.message) == user_id[i]):
						if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == pr[i] and max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == tech[i]):
							bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img2, caption='Техническая эксплуатация и обслуживание электрического и электромеханического оборудования \n\nВыпускники этой специальности квалифицированные специалисты, которые совершают ремонт устройств электроснабжения. Они предотвращают или устраняют неполадки в электрических приборах, проводят профилактические осмотры электрических аппаратов, производят измерения и несложные электрические расчеты, изготавливают электротехнические схемы монтажа и сборки.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img3, caption='Монтаж, техническое обслуживание и ремонт промышленного оборудования \n\nСпециалисты этого профиля выполняют монтаж, техническое обслуживание и ремонт промышленного оборудования. Для выполнения своих должностных обязанностей выпускники должны владеть знаниями основных законов электротехники, изучить физические, технические и промышленные основы электроники. Учащиеся в процессе обучения знакомятся с устройством электронной техники, получают навык работы с инструментами и контрольно-измерительными приборами, которые необходимы для проведения технического обслуживания и ремонта оборудования. Студенты изучают основы метрологии, сертификации и стандартизации, а также знакомятся с методами диагностирования промышленного оборудования и дефектации его элементов. Для будущих специалистов необходим опыт проведения работ по восстановлению работоспособности оборудования с соблюдением техники безопасности и норм бережливого производства.')
							time.sleep(5)
							bot.send_photo(call.message.chat.id, img10, caption='Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей \n\nСпециальность, выпускник которой владеет навыками не только грамотной эксплуатации автомобилей, но и может организовывать технологические процессы обслуживания и ремонта. В процессе обучения студент овладевает компетенциями, которые в дальнейшей трудовой деятельности позволят ему иметь конкурентное преимущество на рынке труда.')
							time.sleep(5)
						else:
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == pr[i]):
								bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == tech[i]):
								bot.send_photo(call.message.chat.id, img1, caption='Производство тугоплавких неметаллических и силикатных материалов и изделий \n\nСтуденты изучают физическую и коллоидную химию, химию кремния, приготовление и хранение сырьевых смесей производства, основы производства тугоплавких неметаллических и силикатных материалов и изделий. Они узнают все о свойствах кремния и его соединениях. Их научат проводить расчеты, подбирать огнеупорные материалы для кладки печей, выбирать способы и режимы охлаждения.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img2, caption='Техническая эксплуатация и обслуживание электрического и электромеханического оборудования \n\nВыпускники этой специальности квалифицированные специалисты, которые совершают ремонт устройств электроснабжения. Они предотвращают или устраняют неполадки в электрических приборах, проводят профилактические осмотры электрических аппаратов, производят измерения и несложные электрические расчеты, изготавливают электротехнические схемы монтажа и сборки.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img3, caption='Монтаж, техническое обслуживание и ремонт промышленного оборудования \n\nСпециалисты этого профиля выполняют монтаж, техническое обслуживание и ремонт промышленного оборудования. Для выполнения своих должностных обязанностей выпускники должны владеть знаниями основных законов электротехники, изучить физические, технические и промышленные основы электроники. Учащиеся в процессе обучения знакомятся с устройством электронной техники, получают навык работы с инструментами и контрольно-измерительными приборами, которые необходимы для проведения технического обслуживания и ремонта оборудования. Студенты изучают основы метрологии, сертификации и стандартизации, а также знакомятся с методами диагностирования промышленного оборудования и дефектации его элементов. Для будущих специалистов необходим опыт проведения работ по восстановлению работоспособности оборудования с соблюдением техники безопасности и норм бережливого производства.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img10, caption='Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей \n\nСпециальность, выпускник которой владеет навыками не только грамотной эксплуатации автомобилей, но и может организовывать технологические процессы обслуживания и ремонта. В процессе обучения студент овладевает компетенциями, которые в дальнейшей трудовой деятельности позволят ему иметь конкурентное преимущество на рынке труда.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img4, caption='Подземная разработка месторождений полезных ископаемых \n\nСтуденты получают знания по классификации минералов, представления о составе, строении, параметрах Земли и земной коры. Они узнают многое о геологических процессах, происходящих в Земле, геологическом возрасте горных пород, их классификации и свойствах. Познакомятся с техногенными изменениями геологической среды. На практике студенты будут отрабатывать способы вскрытия и подготовки скважинной разработки месторождений. Научатся работать на горных машинах, проводить подземные выработки.')
								time.sleep(5)
								bot.send_message(call.message.chat.id, 'Электрические машины и аппараты \n\nВ процессе обучения студенты знакомятся с принципами работы, конструкцией, технологией изготовления и правилами эксплуатации электрических машин и аппаратов, порядком проектирования, производства и ремонта электромеханических устройств и систем, принципами автоматического управления электроприводом, работой электрических станций и т. д. Для специалистов данной специальности всегда достаточно высокий и устойчивый спрос на рынке труда.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == peopl[i]):
								bot.send_photo(call.message.chat.id, img7, caption='Дошкольное образование \n\nПедагог дошкольного образования – это специалист, осуществляющий всестороннее развитие психических и физических качеств детей в соответствии с возрастными и индивидуальными особенностями, а также подготавливающий их к последующей учебной деятельности.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img8, caption='Технология парикмахерского искусства \n\nПарикмахер-модельер – специалист, который осуществляет разнообразные процедуры, связанные с моделированием причесок, уходом за волосами и кожей головы, в круг обязанностей которого входит мытье и массаж головы, стрижка волос (простая и модельная), укладка волос, завивка волос.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img9, caption='Преподавание в начальных классах \n\nУчитель начальных классов – педагог, занимающийся обучением и воспитанием детей младшего школьного возраста (1-4 классы). Он осуществляет целостный педагогический процесс в соответствии с образовательными программами начальной школы. Ключевой целью деятельности учителя начальных классов является формирования главной способности у учащихся: научиться учиться')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == syste[i]):
								bot.send_photo(call.message.chat.id, img5, caption='Информационные системы и программирование \n\nСпециальность информационные системы и программирование изучает вопросы, связанные разработкой операционных систем, интерфейсов к распределенным базам данных; вопросы проектирования и сопровождения, программное и информационное обеспечение компьютерных систем с использованием современных средств вычислительной техники, телекоммуникаций и технологий автоматизированного проектирования. Вас научат подготавливать необходимые данные и составлять технические задания на проектирование автоматизированных систем управления, проводить анализ рынков информационных технологий, поиску и оптимальному выбору программных и аппаратных средств управления, осуществлять анализ, проектирование и разработку сайтов.')
							if (max(pr[i],tech[i],peopl[i],syste[i],hud[i]) == hud[i]):
								bot.send_photo(call.message.chat.id, img8, caption='Технология парикмахерского искусства \n\nПарикмахер-модельер – специалист, который осуществляет разнообразные процедуры, связанные с моделированием причесок, уходом за волосами и кожей головы, в круг обязанностей которого входит мытье и массаж головы, стрижка волос (простая и модельная), укладка волос, завивка волос.')
								time.sleep(5)
								bot.send_photo(call.message.chat.id, img6, caption='Поварское и кондитерское дело \n\nСпециалист по поварскому и кондитерскому делу относится к категории специалистов среднего звена, который занимается организацией и ведением процессов приготовления, оформлением и подготовкой к реализации горячих блюд, кулинарных изделий, закусок сложного ассортимента с учетом потребностей различных категорий потребителей, видов и форм обслуживания.')




	except Exception as e:
		print(repr(e))
		#welcome("hi")



def delete(message):
      bot.delete_message(message.chat.id, message.message_id)


# RUN
bot.polling(none_stop=True)