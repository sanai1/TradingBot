import telebot  # pip install pyTelegramBotAPI / alt + enter для скачивания библиотек
from bs4 import BeautifulSoup
from db import DBHeper

# НЕ ЗАБУДЬТЕ ВСТАВИТЬ СВОЙ ТОКЕН!!!!
token = '6291399833:AAEFvkL-1IxVMeoyxP7Rryrn0NLeQMge5rE'
bot = telebot.TeleBot(token)

keyboard_name = "сектор" # переменная для определение в каком меню находишься TODO: желательно заменить на что-то получше (сделать вместе с реализацией кнопки назад)

# TODO: ориентировочно парсим тут, желательно сводя все к массиву в каком-либо виде, далее вызываем метод класса DBHeper для добавления всего этого добра в БД


# /start  /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "HELLO!"
    bot.send_message(message.chat.id, welcome_text)
    send_Bwelcome(message)


def send_Bwelcome(message):
    # Создаём клавиатуру
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    welcome_text = "Выберите сектор"

    # получаем названия секторов
    database = DBHeper("указать путь к БД")
    mas_name_sector = DBHeper.get_name_sector(database)

    #Создаём и добавляем кнопки
    for i in range(0, len(mas_name_sector), 3):
        bnt_one = telebot.types.KeyboardButton(mas_name_sector[i][0])
        if i + 2 < len(mas_name_sector):
            bnt_two = telebot.types.KeyboardButton(mas_name_sector[i+1][0])
            bnt_three = telebot.types.KeyboardButton(mas_name_sector[i+2][0])
            keyboard.add(bnt_one, bnt_two, bnt_three)
        elif i + 1 < len(mas_name_sector):
            bnt_two = telebot.types.KeyboardButton(mas_name_sector[i+1][0])
            keyboard.add(bnt_one, bnt_two)
        else:
            keyboard.add(bnt_one)

    # Отправляем клавиатуру
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.chat.type == "private":
        if message.text == "назад":
            # TODO: реализовать действие кнопки назад (возврат к предыдущему состаянию клавиатуры/ крайний случай - в главное меню, первое состояние кнопок)
            print("назад")
        else:
            if keyboard_name == "сектор":
                sector_text = "Выберите интересующую бумагу"
                database = DBHeper("db_telebot.db")
                mas_name_stocks = database.get_name_stocks(message.text)
                bot.send_message(message.chat.id, sector_text, reply_markup=sector(mas_name_stocks))
            elif keyboard_name == "акции":
                # TODO: подтягивание из БД мультипликаторов, вызов функции stocks с последующим выводом аналитики на экран в виде сообщения
                print("аналитика")


def sector(name_sector): # передаем массив с названиями акций в выбранном секторе, получаем клавиатуру из названий компаний
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=3)
    for i in range(0, len(name_sector), 3):
        btn_one = telebot.types.KeyboardButton(name_sector[i][0])
        if i + 2 < len(name_sector):
            btn_two = telebot.types.KeyboardButton(name_sector[i+1][0])
            btn_three = telebot.types.KeyboardButton(name_sector[i+2][0])
            keyboard.add(btn_one, btn_two, btn_three)
            if i + 3 == len(name_sector):
                keyboard.add(telebot.types.KeyboardButton("назад"))
        elif i + 1 < len(name_sector):
            btn_two = telebot.types.KeyboardButton(name_sector[i+1][0])
            keyboard.add(btn_one, btn_two, telebot.types.KeyboardButton("назад"))
        else:
            keyboard.add(btn_one, telebot.types.KeyboardButton("назад"))
    global keyboard_name
    keyboard_name = "акции"
    return keyboard


def stocks(name_stocks):
    print("аналитика")


bot.polling()