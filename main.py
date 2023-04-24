import telebot
from telebot import types
import sqlite3
import pandas as pd


bot = telebot.TeleBot('6107680735:AAH9rrQINqK0IDzmxnlBVgVRtn5w5MsSFNw')


# Обработка кнопки /start
@bot.message_handler(commands=['start'])
def start(message):
    """
    Вывод начального сообщения по нажатию кнопки /start
    :param message: Переменная для управления чатом и пользователем
    :return: None
    """
    bot.send_message(message.chat.id, 'Привет, я Russian Trip Bot! Я умею искать интересные места в городах России, которые ты мне напишешь 🗺')
    bot.send_message(message.chat.id, 'Чтобы начать, напиши мне название города России, который хочешь посетить.')


# Получение данных из базы данных
def get_db(city):
    """
    Получение информации о городе из базы данных
    :param city: название введённого города
    :return: data: Информация о городе из базы данных
    """
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT * FROM trip WHERE city = ?'
    cursor.execute(query, (city,))
    data = cursor.fetchall()
    connect.close()
    return data


# Разделение и вывод данных
def split_db(message, data):
    """
    Форматированный вывод данных
    :param message: Переменная для управления чатом и пользователем
    :param data: Информация о городе из базы данных
    :return: None
    """
    for i in data:
        text = f'<b>{i[2]}</b>\n\n{i[3]}\n\n<i>{i[4]}</i>'
        photo = i[1].split('; ')
        media = [telebot.types.InputMediaPhoto(open(f'{photo[0]}', 'rb'), caption=text, parse_mode='html'), telebot.types.InputMediaPhoto(open(f'{photo[1]}', 'rb')), telebot.types.InputMediaPhoto(open(f'{photo[2]}', 'rb'))]
        bot.send_media_group(message.chat.id, media)
        link = i[5].split('; ')
        markup = types.InlineKeyboardMarkup()
        if len(link) == 2:
            if 'reviews' in link[0] and 'reviews' in link[1]:
                markup.add(types.InlineKeyboardButton('Отзывы в Яндекс', url=f'{link[0]}'))
                markup.add(types.InlineKeyboardButton('Отзывы в Яндекс', url=f'{link[1]}'))
                bot.send_message(message.chat.id, 'Вот несколько полезных ссылок', reply_markup=markup)
            elif 'reviews' in link[0] and not 'reviews' in link[1]:
                markup.add(types.InlineKeyboardButton('Официальный сайт', url=f'{link[1]}'))
                markup.add(types.InlineKeyboardButton('Отзывы в Яндекс', url=f'{link[0]}'))
                bot.send_message(message.chat.id, 'Вот несколько полезных ссылок', reply_markup=markup)
        elif len(link) == 1:
            if '---' in link[0]:
                continue
            elif 'reviews' in link[0]:
                markup.add(types.InlineKeyboardButton('Отзывы в Яндекс', url=f'{link[0]}'))
                bot.send_message(message.chat.id, 'Вот несколько полезных ссылок', reply_markup=markup)
            elif not 'reviews' in link[0]:
                markup.add(types.InlineKeyboardButton('Официальный сайт', url=f'{link[0]}'))
                bot.send_message(message.chat.id, 'Вот несколько полезных ссылок', reply_markup=markup)


# Обработка ввода города
# Выводит 5 мест (3 картинки, описание, адрес и кнопку с отзывами в Яндексе + сайт (если есть))
@bot.message_handler()
def info(message):
    """
    Управление выводом информации
    :param message: Переменная для управления чатом и пользователем
    :return: None
    """
    city = message.text
    data = get_db(city)  # вся инфа из бд
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
    df = pd.read_html(url)[0]
    if city in df.values:
        if not data:
            bot.send_message(message.chat.id, 'Такого города пока нет в моем списке 😔 Но в скором времени мы это исправим 😉')
        else:
            bot.send_message(message.chat.id, f'Вот список интересных мест города <u>{city}</u>:', parse_mode='html')
            split_db(message, data)
    else:
        bot.send_message(message.chat.id, 'Введите корректное название города 🫣')


bot.polling(none_stop=True)
