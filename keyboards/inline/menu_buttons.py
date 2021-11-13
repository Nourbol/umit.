from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Точки по близости", callback_data="points_nearby")
        ],
        [
            InlineKeyboardButton(text="Мои комментарии", callback_data="my_comments")
        ],
        [
            InlineKeyboardButton(text="Профиль", callback_data="profile")
        ]
    ])