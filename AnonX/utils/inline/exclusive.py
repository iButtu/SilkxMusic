from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_exclusive",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Aᴅᴍɪɴ",
                    callback_data="exclusive_callback ex1",
                ),
                InlineKeyboardButton(
                    text="Aᴜᴛʜ",
                    callback_data="exclusive_callback ex2",
                ),
                InlineKeyboardButton(
                    text="Bʟᴋ-Lɪsᴛ",
                    callback_data="exclusive_callback ex3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bʟᴏᴄᴋᴇʀs",
                    callback_data="exclusive_callback ex4",
                ),
                InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="exclusive_callback ex5",
                ),
                InlineKeyboardButton(
                    text="Exᴛʀᴀs",
                    callback_data="exclusive_callback ex6",
                ),
            ],
          mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_exclusive",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Exᴄʟᴜsɪᴠᴇ",
                callback_data="settings_back_exclusive",
            ),
        ],
    ]
    return buttons
