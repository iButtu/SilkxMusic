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
            callback_data=f"settingsback_helper",
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
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Aᴜᴛʜ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Bʟᴋ-Lɪsᴛ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bʟᴏᴄᴋᴇʀs",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="Exᴛʀᴀs",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Lʏʀɪᴄs",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Pʟᴀʏʟɪsᴛ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Pɪɴɢ",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="C-Pʟᴀʏ",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="Sᴜᴅᴏᴇʀs",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Hᴇʀᴏᴋᴜ",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Cᴏɴғɪɢ",
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text="Bᴏᴛ Cᴍɴᴅs",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="Pᴠᴛ Bᴏᴛ",
                    callback_data="help_callback hb15",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="V-Cʜᴀᴛs",
                    callback_data="help_callback hb16",
                ),
                InlineKeyboardButton(
                    text="Rᴇʙᴏᴏᴛ",
                    callback_data="help_callback hb17",
                ),
                InlineKeyboardButton(
                    text="G-Bᴀɴ",
                    callback_data="help_callback hb18",
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
                    callback_data=f"settings_back_helper",
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
                text="Hᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
