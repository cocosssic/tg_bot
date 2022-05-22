import telebot
from telebot import types

bot= telebot.TeleBot('#TOKEN')

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("расписание",url="https://www.tutu.ru"))
    bot.send_message(message.chat.id, "Просто нажми на кнопку", parse_mode='html', reply_markup=markup)




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('test1')
    btn2 = types.KeyboardButton('test2')
    btn3 = types.KeyboardButton('test3')
    btn4 = types.KeyboardButton('test4')
    btn5 = types.KeyboardButton('test5')
    btn6 = types.KeyboardButton('test6')
    btn7 = types.KeyboardButton('test7')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!"
    bot.send_message( message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

bot.polling(non_stop=True)
