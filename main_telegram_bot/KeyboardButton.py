from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


# ================= КНОПКИ АДМИНА =================
btn_add_admin = KeyboardButton("Добавить админа")
btn_del_admin = KeyboardButton("Удалить админа")
btn_all_admin = KeyboardButton("Все админы")

btn_add_bot_main = KeyboardButton("Добавить Бота")

btn_add_city = KeyboardButton("Добавить Город")
btn_del_city = KeyboardButton("Удалить Город")

btn_add_district = KeyboardButton("Добавить Район")
btn_del_district = KeyboardButton("Удалить Район")

btn_add_dop_district = KeyboardButton("Добавить доп Район")
btn_del_dop_district = KeyboardButton("Удалить доп Район")

btn_add_product = KeyboardButton("Добавить Продукт")
btn_del_product = KeyboardButton("Удалить Продукт")

btn_malling_add = KeyboardButton("Сделать рассылку")
btn_malling_del = KeyboardButton("Удалить рассылку")
btn_malling_all = KeyboardButton("Все рассылки")
btn_all_info = KeyboardButton("Все пользователи")

btn_add_card = KeyboardButton("Добавить карту")
btn_del_card = KeyboardButton("Удалить карту")

btn_add_btc = KeyboardButton("Добавить BTC")
btn_del_btc = KeyboardButton("Удалить BTC")

btn_add_sim = KeyboardButton("Добавить ETH")
btn_del_sim = KeyboardButton("Удалить ETH")

btn_add_ltc = KeyboardButton("Добавить LTC")
btn_del_ltc = KeyboardButton("Удалить LTC")

btn_all_wallets = KeyboardButton("Все кошельки")

btn_edit_min = KeyboardButton("Изменить MIN пополнение")

btn_captha = KeyboardButton("Капча")
btn_num_edit = KeyboardButton("Номер_")

btn_all = KeyboardButton("Все")
btn_cancel = KeyboardButton("Отмена")

btn_t = "➖➖➖➖➖➖➖➖➖➖➖➖➖➖"

BUTTON_TYPES = {
    "BTN_HOME_ADMIN": ReplyKeyboardMarkup(resize_keyboard=True).add(btn_add_admin, btn_del_admin, btn_all_admin).add(btn_add_bot_main).add(btn_t).
    add(btn_add_city, btn_add_product, btn_add_district, btn_add_dop_district).add(btn_t).add(btn_del_city, btn_del_product, btn_del_district, btn_del_dop_district).add(btn_t).add(btn_malling_add, btn_malling_del, btn_malling_all).add(btn_all_info).add(btn_t).
    add(btn_add_card, btn_add_btc).add(btn_add_ltc, btn_add_sim).add(btn_t).add(btn_del_card, btn_del_btc).add(btn_del_ltc, btn_del_sim).add(btn_t).add(btn_all_wallets).add(btn_edit_min).add(btn_captha).add(btn_num_edit),


    "BTN_CANCEL": ReplyKeyboardMarkup(resize_keyboard=True).add(btn_cancel),
    "BTN_CANCEL_ALL": ReplyKeyboardMarkup(resize_keyboard=True).add(btn_all).add(btn_cancel),
}
