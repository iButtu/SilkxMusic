from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from strings import get_command, get_string, exclusivers
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils import exclusive_pannel
from AnonX.utils.database import get_lang, is_commanddelete_on
from AnonX.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from AnonX.utils.inline.exclusive import (exclusive_back_markup,
                                          private_exclusive_panel)

### Command
exclusive_COMMAND = get_command("exclusive_COMMAND")


@app.on_message(
    filters.command(exclusive_COMMAND)
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_exclusive") & ~BANNED_USERS
)
async def exclusiveer_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = exclusive_pannel(_, True)
        if update.message.photo:
            await update.edit_message_text(
                _["exclusive_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["exclusive_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = exclusive_pannel(_)
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["exclusive_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard)


@app.on_message(
    filters.command(exclusive_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def exclusive_com_group(client, message: Message, _):
    keyboard = private_exclusive_panel(_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["exclusive_2"], reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("exclusive_callback") & ~BANNED_USERS)
@languageCB
async def exclusiveer_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = exclusive_back_markup(_)
    if cb == "ex6":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "This button is only for sudoers.", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                exclusivers.EXCLUSIVE_6, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "ex1":
        await CallbackQuery.edit_message_text(
            exclusivers.EXCLUSIVE_1, reply_markup=keyboard
        )
    elif cb == "ex2":
        await CallbackQuery.edit_message_text(
            exclusivers.EXCLUSIVE_2, reply_markup=keyboard
        )
    elif cb == "ex3":
        await CallbackQuery.edit_message_text(
            exclusivers.EXCLUSIVE_3, reply_markup=keyboard
        )
    elif cb == "ex4":
        await CallbackQuery.edit_message_text(
            exclusivers.EXCLUSIVE_4, reply_markup=keyboard
        )
    elif cb == "ex5":
        await CallbackQuery.edit_message_text(
            exclusivers.EXCLUSIVE_5, reply_markup=keyboard
        )
