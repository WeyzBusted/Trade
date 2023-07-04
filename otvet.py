# -*- coding: utf8 -*-
import telebot
from telebot import types
import json
from config import maxbalancestatus0,maxbalancestatus2


pravila = "Политика и условия пользования данным ботом.\n\
1. Перед принятием инвестиционного решения Инвестору необходимо самостоятельно оценить экономические риски и выгоды, налоговые, юридические, бухгалтерские последствия заключения сделки, свою готовность и возможность принять такие риски. Клиент также несет расходы на оплату брокерских и депозитарных услуг\n\
2. Принимая правила, Вы подтверждаете своё согласие со всеми вышеперечисленными и нижеперечисленными правилами!\n\
3. Ваш аккаунт может быть заблокирован в подозрении на мошенничество/обман нашей системы!\n\
4. Мультиаккаунты запрещены!\n\
5. Скрипты, схемы, тактики использовать запрещено!\n\
6. Если будут выявлены вышеперчисленные случаи, Ваш аккаунт будет заморожен до выяснения обстоятельств!\n\
7. В случае необходимости администрация имеет право запросить у Вас документы, подтверждающие Вашу личность и Ваше совершеннолетие.\n\
Вы играете на виртуальные монеты, покупая их за настоящие деньги. Любое пополнение бота является пожертвованием!По всем вопросам игры обращайтесь в поддержку, указанную в описании к боту.\n\
Пишите сразу по делу, а не «Здравствуйте! Тут?»\n\
Старайтесь изложить свои мысли четко и ясно.\n\n\
Спасибо за понимание, Ваш «Igrovoi bot»"



workerinfo = f"Фейковый номер для вывода +77777777777                                                         Статус 1 - всегда проигрыш\n\nСтатус 0 - реферал будет выигрывать пока у него баланс меньше {maxbalancestatus0},после того как баланс увелечится статус автоматичкесий изменится на 0 - всегда проигрыш\nНа этом статусе ставка на ровно будет проигрыш.\n\nСтатус 2:Любая cтавка будет выигрыш пока у него баланс меньше {maxbalancestatus2},после того как баланс увелечится статус автоматичкесий изменится на 0 - всегда проигрыш\n\n\nДефолтом стоит статус - 0"
prinyat = "Принять правила✅"

start = "Приветствую!"
start2 = "Приветствую снова!"
select = "Выберите актив."
qiwiorpromo = "Выберите вариант пополнения баланса"
textotzyv = "Оставить свой отзыв, и прочитать отзывы других пользователей можете тут.\n\nОставьте свой отзыв и получите +5% на следующее пополнение."

userbtn1 = "ECN счёт📍"
userbtn2 = "💼 Профиль"
userbtn3 = "Пополнить💰"
userbtn4 = "💸Вывести"
userbtn6 = "Отзывы 💬"
userbtn5 = "🛠 Тех Поддержка 🛠"


activ1 = "Amazon"
activ2 = "Apple"
activ3 = "Bitcoin"
activ4 = "Ethereum"
activ5 = "Tesla"
activ6 = "Intel"

otmena = "Отмена"

verx = "Вверх"
vniz = "Вниз"
rovno = "Не изменится"


balanceqiwi= "💳 QIWI"
balancecard = "💳 Банковская карта (RU)"
balancepromo = "💳 Промокод"

oplata = "Оплатить"
proverit = "Проверить"

def igrabtn():
	gamebtn = types.ReplyKeyboardMarkup(True)
	gb1 = types.KeyboardButton(verx)
	gb2 = types.KeyboardButton(vniz)
	gb3 = types.KeyboardButton(rovno)

	gamebtn.add(gb1,gb2)
	gamebtn.add(gb3)

	return gamebtn



def user():
	k1 = types.ReplyKeyboardMarkup(True)
	k1_btn1 = types.KeyboardButton(userbtn1)
	k1_btn2 = types.KeyboardButton(userbtn2)
	k1_btn3 = types.KeyboardButton(userbtn3)
	k1_btn4 = types.KeyboardButton(userbtn4)
	k1_btn6 = types.KeyboardButton(userbtn6)
	k1_btn5 = types.KeyboardButton(userbtn5)

	k1.add(k1_btn1)	
	k1.add(k1_btn3,k1_btn2,k1_btn4)	
	k1.add(k1_btn6,k1_btn5)
	
	

	return k1

def akcii():
	act = types.ReplyKeyboardMarkup(True)
	activ_btn1 = types.KeyboardButton(activ1)
	activ_btn2 = types.KeyboardButton(activ2)
	activ_btn3 = types.KeyboardButton(activ3)
	activ_btn4 = types.KeyboardButton(activ4)
	activ_btn5 = types.KeyboardButton(activ5)
	activ_btn6 = types.KeyboardButton(activ6)
	activ_btn7 = types.KeyboardButton(otmena)

	act.add(activ_btn1,activ_btn2)	
	act.add(activ_btn3,activ_btn4)	
	act.add(activ_btn5,activ_btn6)
	act.add(activ_btn7)
	return act


def cancel():
	markup = types.ReplyKeyboardMarkup(True)
	key1 = types.KeyboardButton("Отмена")
	markup.add(key1)
	return markup

def popolnenie():
	pop = types.ReplyKeyboardMarkup(True)
	pop1 = types.KeyboardButton(balanceqiwi)
	pop4 = types.KeyboardButton(balancecard)
	pop2 = types.KeyboardButton(balancepromo)
	pop3 = types.KeyboardButton(otmena)

	pop.add(pop1)
	pop.add(pop4)
	pop.add(pop2)
	pop.add(pop3)
	return pop


def soglashenie():
	prinyatpravila = types.InlineKeyboardMarkup()
	prinyatpravila_btn1 = types.InlineKeyboardButton(text=prinyat, callback_data="prinyal")
	prinyatpravila.add(prinyatpravila_btn1)
	return prinyatpravila


def adminpanel():
	adm = types.InlineKeyboardMarkup()
	adm1 = types.InlineKeyboardButton(text="Изменить Qiwi", callback_data="qiwi")	
	adm6 = types.InlineKeyboardButton(text="Изменить Карту", callback_data="cardcard")	
	adm2 = types.InlineKeyboardButton(text="Статистика", callback_data="stat")
	
	adm3 = types.InlineKeyboardButton(text="Рассылка", callback_data="send")	
	adm4 = types.InlineKeyboardButton(text="Закрыть", callback_data="cancel")
	adm5 = types.InlineKeyboardButton(text="Изменить процент", callback_data="procent")
	adm.add(adm1)	
	adm.add(adm6)	
	adm.add(adm5)	
		
	adm.add(adm2)
	adm.add(adm3)	
	adm.add(adm4)

	return adm

def workerpanel():
	wrk = types.InlineKeyboardMarkup()
	wrk1 = types.InlineKeyboardButton(text="Реф ссылка", callback_data="ref")
	wrk9 = types.InlineKeyboardButton(text="Информация", callback_data="infworker")
	wrk5 = types.InlineKeyboardButton(text="💌 Сообщение рефералу", callback_data="smsm")
	wrk6 = types.InlineKeyboardButton(text="💌 Рассылка рефералам", callback_data="rassw")
	wrk2 = types.InlineKeyboardButton(text="Создать промо", callback_data="prom")
	wrk4 = types.InlineKeyboardButton(text="Статистика", callback_data="statw")
	wrk7 =  types.InlineKeyboardButton(text="Список рефералов", callback_data="spisok")
	wrk8 =  types.InlineKeyboardButton(text="Изменить статус", callback_data="statusreplace")
	wrk10 = types.InlineKeyboardButton(text="Изменит баланс", callback_data="admbalance")
	wrk3 = types.InlineKeyboardButton(text="Закрыть", callback_data="cancel")

	wrk.add(wrk1,wrk9)
	wrk.add(wrk5,wrk6)	
	wrk.add(wrk7,wrk8)	
	wrk.add(wrk2,wrk4)	
	wrk.add(wrk10)
	wrk.add(wrk3)
	

	return wrk





rem = types.ReplyKeyboardRemove()	