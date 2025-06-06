from telebot import types


# Клавиатура основная
def main_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('💸 Чеки / Баланс')
    btn2 = types.KeyboardButton('📪 Накладные / поссылки')

    btn3 = types.KeyboardButton('📩 Письма')
    btn4 = types.KeyboardButton('🎲 Ставки')

    btn5 = types.KeyboardButton('🖼 Готовые скриншоты')
    btn6 = types.KeyboardButton('💬 Диалоги')

    btn7 = types.KeyboardButton('👨‍💼 Информация')

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7)
    return markup
  
# Клавиатура диалогов
def dialog_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
    btn1 = types.KeyboardButton('👋 Приветствие')
    btn2 = types.KeyboardButton('🧐 Вопросы о товаре')
    btn3 = types.KeyboardButton('🚚 Доставка')
    btn4 = types.KeyboardButton('🙄 Другие вопросы')
    btn5 = types.KeyboardButton('Назад ↩️')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.add(btn5)
    return markup 

# Клавиатура скриншотов
def screenshot_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
    btn1 = types.KeyboardButton('Авито')
    btn2 = types.KeyboardButton('Юла')
    btn3 = types.KeyboardButton('Другие сервисы')
    btn5 = types.KeyboardButton('Назад ↩️')
    markup.row(btn1, btn2, btn3)
    markup.add(btn5)
    return markup 

# Клавиатура скриншотов
def avito_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('1.0 Запрос почты')
    btn2 = types.KeyboardButton('1.0 Оплата по ссылке')

    btn3 = types.KeyboardButton('2.0 Подозрительный')
    btn4 = types.KeyboardButton('2.0 Запрос почты')

    btn5 = types.KeyboardButton('3.0 Запрос кода')

    btn6 = types.KeyboardButton('Списывание / баланс')
    btn7 = types.KeyboardButton('CVC код')

    btn8 = types.KeyboardButton('Нет уведомлений')
    btn9 = types.KeyboardButton('Авито - 900')

    btn10 = types.KeyboardButton('Как работает доставка (ссылка)')

    btn11 = types.KeyboardButton('Как работает доставка (SMS)')

    btn12 = types.KeyboardButton('Как работает доставка (Email)')

    btn13 = types.KeyboardButton('Заказ оформлен, продавец получит средства через sms/ссылку')

    btn14 = types.KeyboardButton('Возврат')
    btn15 = types.KeyboardButton('Получить по ссылке')

    btn16 = types.KeyboardButton('Деньги возвращаются на карту после резервирования (sms)')

    btn17 = types.KeyboardButton('Назад ↩️')


    markup.row(btn1, btn2)
    markup.row(btn2, btn3)
    markup.add(btn5)
    markup.row(btn6, btn7)
    markup.row(btn8, btn9)
    markup.add(btn10)
    markup.add(btn11)
    markup.add(btn12)
    markup.add(btn13)
    markup.row(btn14, btn15)
    markup.add(btn16)
    markup.add(btn17)
    return markup          

# Клавиатура скриншотов
def youla_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('- 1.0 Запрос почты')
    btn2 = types.KeyboardButton('- 1.0 Оплата по ссылке')

    btn3 = types.KeyboardButton('- 1.0 900')
    btn4 = types.KeyboardButton('- 2.0 900')

    btn5 = types.KeyboardButton('- 2.0 Подозрительный')

    btn6 = types.KeyboardButton('- 3.0 Запрос кода')

    btn7 = types.KeyboardButton('- Запрос почты')
    btn8 = types.KeyboardButton('- CVC код')

    btn9 = types.KeyboardButton('- Нет уведомлений')

    btn10 = types.KeyboardButton('- Получить по ссылке')
    btn11 = types.KeyboardButton('- Возврат')

    btn12 = types.KeyboardButton('- Как работает доставка (ссылка)')

    btn17 = types.KeyboardButton('Назад ↩️')


    markup.row(btn1, btn2)
    markup.row(btn3)
    markup.add(btn5, btn6)
    markup.row(btn7, btn8)
    markup.add(btn9)
    markup.row(btn10, btn11)
    markup.add(btn12)
    markup.add(btn17)
    return markup              

# Клавиатура другие сервисы
def other_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('🚕 Яндекс.Доставка 2.0 — как работает доставка')

    btn2 = types.KeyboardButton('🚐 Dostavista 2.0 — как работает доставка')

    btn3 = types.KeyboardButton('🚎 Почта РФ 2.0 — как работает доставка')

    btn4 = types.KeyboardButton('🚗 Boxberry 2.0 — как работает доставка')

    btn5 = types.KeyboardButton('🚛 СДЭК — оплата по ссылке')

    btn6 = types.KeyboardButton('🛺 СДЭК 2.0 — как работает доставка')

    btn7 = types.KeyboardButton('🚚 Boxberry — оплата по ссылке')

    btn17 = types.KeyboardButton('Назад ↩️')


    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn7)
    markup.add(btn5)
    markup.add(btn6)

    markup.add(btn17)
    return markup                   

# Клавиатура отрисовка
def wallet_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True) 

    btn1 = types.KeyboardButton('QIWI')
    btn2 = types.KeyboardButton('Яндекс.Деньги')

    btn3 = types.KeyboardButton('Sberbank')
    btn4 = types.KeyboardButton('Tinkoff')

    btn5 = types.KeyboardButton('OLX KZ')
    btn6 = types.KeyboardButton('OLX PL')

    btn8 = types.KeyboardButton('MonoBank')

    btn9 = types.KeyboardButton('Kufar')
    btn10 = types.KeyboardButton('Kaspi')

    btn11 = types.KeyboardButton('SportBank')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)
    markup.row(btn9, btn10)
    markup.row(btn8, btn11)
    markup.add(btn17)
    return markup

# Клавиатура Qiwi
def qiwi_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Баланс Киви')
    btn2 = types.KeyboardButton('Перевод Киви')
    btn3 = types.KeyboardButton('Получение Киви (ПК)')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2, btn3)
    markup.add(btn17)
    return markup

# Клавиатура Yandex
def yandex_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Баланс ЮMoney')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1)
    markup.add(btn17)
    return markup

# Клавиатура Sberbank
def sberbank_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Баланс Сбербанк')
    btn2 = types.KeyboardButton('Перевод Сбербанк')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)

    markup.add(btn17)
    return markup

# Клавиатура Tinkoff
def tinkoff_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Перевод Тинькофф')
    btn2 = types.KeyboardButton('Чек Тинькофф')

    btn3 = types.KeyboardButton('Тинькофф перевод Авито')
    btn4 = types.KeyboardButton('Тинькофф перевод Юла')

    btn5 = types.KeyboardButton('Тинькофф возврат')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    markup.add(btn5)

    markup.add(btn17)
    return markup                                       

# Клавиатура OLX KZ
def olxkz_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Перевод OLX (KZ)')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1)

    markup.add(btn17)
    return markup

# Клавиатура OLX PL
def olxpl_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Перевод OLX (PL)')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1)

    markup.add(btn17)
    return markup                                                
                                                   
# Клавиатура MonoBank
def monobank_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Баланс Monobank')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1)

    markup.add(btn17)
    return markup                                                    

# Клавиатура Kufar
def kufar_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Перевод Куфар')
    btn2 = types.KeyboardButton('Куфар Card2Card')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)

    markup.add(btn17)
    return markup 

# Клавиатура kaspi
def kaspi_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Баланс Каспи')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1)

    markup.add(btn17)
    return markup 

# Клавиатура отрисовка
def delivery_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Нова Пошта')
    btn2 = types.KeyboardButton('Boxberry')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)

    markup.add(btn17)
    return markup 

# Клавиатура отрисовка
def bet_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('PariMatch')
    btn2 = types.KeyboardButton('BetWinner')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)

    markup.add(btn17)
    return markup 
    
# Клавиатура отрисовка
def mailto_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)

    btn1 = types.KeyboardButton('Письмо Юла')
    btn2 = types.KeyboardButton('Юла возврат')
    btn3 = types.KeyboardButton('Письмо Авито')

    btn17 = types.KeyboardButton('Назад ↩️')

    markup.row(btn1, btn2)
    markup.row(btn3, btn17)
    return markup 





















