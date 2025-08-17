import telebot
from telebot import types
from get_cost import check_rate
from tg_token import api_key


bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['menu', 'start'])
def menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Рассчитать стоимость💰')
    markup.row(btn1)

    btn2 = types.KeyboardButton('Отзывы✍️')
    btn3 = types.KeyboardButton('Написать менеджеру👨‍💻')
    markup.row(btn2, btn3)

    btn5 = types.KeyboardButton('Ответы на вопросы❓')
    btn6 = types.KeyboardButton('Меню⚙️')
    markup.row(btn5, btn6)


    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name} \n\n"
    f"Этот бот поможет тебе рассчитать стоимость заказа \nСвязаться с менеджером \n@p0iman \n" 
    f"А также получить ответы на интересующие вопросы", reply_markup=markup)


@bot.message_handler(commands=['get_cost'])
def cost(message):
    bot.send_message(message.chat.id, f"Введите стоимость выбранного товара в Юанях")
    bot.register_next_step_handler(message, exchange)


def exchange(message):

    exchange_rate = check_rate()

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Менеджер👨‍💻', url='https://t.me/p0iman')
    markup.row(btn1)

    try:
        float(message.text) * exchange_rate
    except ValueError:
        bot.reply_to(message, f"Некорректный ввод")
    except TypeError:
        bot.reply_to(message, f"Некорректный ввод")
    else:
        res = int(float(message.text) * exchange_rate) + 2500
        bot.send_message(message.chat.id, f"Итоговая стоимость {res}₽ \nСтоимость включает: \nДоставку из Китая в Москву - 1500₽"
                                          f"\nКоммисию нашего сервиса - 1000₽\n<b>Курс ¥ - {exchange_rate}₽</b>", reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['reviews'])
def reviews(message):
    bot.send_message(message.chat.id, f"<b>Отзывы:</b> https://t.me/chinatown_otzyv", parse_mode='html')


@bot.message_handler(commands=['manager'])
def manager(message):
    bot.send_message(message.chat.id, f"<b>Наш менеджер:</b> @p0iman", parse_mode='html')


@bot.message_handler(commands=['questions'])
def questions(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('📌Как все работает?', callback_data='how to use')
    btn2 = types.InlineKeyboardButton('📌Как выбрать товар?', callback_data='how to choose product')

    markup.row(btn1)
    markup.row(btn2)

    btn3 = types.InlineKeyboardButton('📌Как выбрать размер', callback_data='how to choose size')
    btn4 = types.InlineKeyboardButton('📌Как скопировать ссылку?', callback_data='how to copy link')

    markup.row(btn3)
    markup.row(btn4)

    bot.send_message(message.chat.id, f'Если вы <b>не нашли</b> интересующий вас вопрос, обратитесь к менеджеру @p0iman', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def processing(message):
    if message.text == 'Рассчитать стоимость💰':
        cost(message)
    elif message.text == 'Отзывы✍️':
        reviews(message)
    elif message.text == 'Написать менеджеру👨‍💻':
        manager(message)
    elif message.text == 'Ответы на вопросы❓':
        questions(message)
    elif message.text == 'Меню⚙️':
        menu(message)


@bot.message_handler(content_types=['photo'])
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):

    if callback.data == 'how to use':
        bot.send_message(callback.message.chat.id, f"<b>Как все работает?</b>\n\n"
                                                   f"<b>1. Напиши @p0iman и расскажи, что ты хочешь заказать, прикрепи ссылку на товар и скриншот.</b>\n\n"
                                                   f"<b>2. Мы производим расчёт и предоставим финальную стоимость.</b>\n\n"
                                                   f"<b>3. Производишь оплату товара.</b>\n\n"
                                                   f"<b>4. Мы оплачиваем и оформляем твой заказ, предоставляем чеки.</b>\n\n"
                                                   f"<b>5. Остаётся только ждать пока твой товар приедет. В любой момент ты можешь обратиться по любому вопросу.</b>", parse_mode='html')

    elif callback.data == 'how to choose product':
        bot.send_message(callback.message.chat.id, f"<b>Как выбрать товар?\n\n"
                                                   f"1. Заходите в приложение dewu (POIZON)\n"
                                                   f"<i>https://apps.apple.com/app/id1012871328</i>\n\n"
                                                   f"2. Регистрируетесь по своему номеру телефона.\n\n"
                                                   f"3. Находите товар который вас интересует.\n\n"
                                                   f"4. Выбираете нужный размер.\n\n"
                                                   f"5. И скидываете ссылку и скриншот @p0iman</b>", parse_mode='html', disable_web_page_preview=True)

    elif callback.data == 'how to choose size':
        '''bot.send_media_group(callback.message.chat.id, [types.InputMediaPhoto(open('photo_5188322199126265612_y.jpg', 'rb')),
                                               types.InputMediaPhoto(open('photo_5188322199126265613_y.jpg', 'rb'))])'''
        pic1 = open('photo_5188322199126265612_y.jpg', 'rb')
        pic2 = open('photo_5188322199126265613_y.jpg', 'rb')
        media = [types.InputMediaPhoto(pic1, caption="<b>Как выбрать размер</b>", parse_mode='html'), types.InputMediaPhoto(pic2)]
        bot.send_media_group(callback.message.chat.id, media)

    elif callback.data == 'how to copy link':
        '''bot.send_media_group(callback.message.chat.id,
                             [types.InputMediaPhoto(open('photo_5188322199126265616_y.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo_5188322199126265617_y.jpg', 'rb'))])'''
        pic1 = open('photo_5188322199126265616_y.jpg', 'rb')
        pic2 = open('photo_5188322199126265617_y.jpg', 'rb')
        media = [types.InputMediaPhoto(pic1, caption="<b>Как скопировать ссылку</b>", parse_mode='html'), types.InputMediaPhoto(pic2)]
        bot.send_media_group(callback.message.chat.id, media)


bot.polling(none_stop=True)
