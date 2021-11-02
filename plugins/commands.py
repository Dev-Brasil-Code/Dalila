import os
import logging
import random
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('➕ Me adicione ao seu grupo ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Procurar', switch_inline_query_current_chat=''),
            InlineKeyboardButton('Atualizações 🤖', url='https://t.me/Doacoes_full')
            ],[
            InlineKeyboardButton('ℹ️ Ajuda', callback_data='help'),
            InlineKeyboardButton('About 🤔', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Certifique-se de que o bot é administrador no canal")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "🤖 Canal de atualizações", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton(" 🔄 Tentar novamente", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**Junte-se ao canal de atualizações para usar este bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay"]:
        buttons = [[
            InlineKeyboardButton('➕ Me adicione ao seu grupo ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Procurar', switch_inline_query_current_chat=''),
            InlineKeyboardButton('Atualizaçoes 🤖', url='https://t.me/Doacoes_Full')
            ],[
            InlineKeyboardButton('ℹ️ Ajuda', callback_data='help'),
            InlineKeyboardButton('About 🤔', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
        return
    file_id = message.command[1]
    files = (await get_file_details(file_id))[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
        except Exception as e:
            print(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Envie informações básicas do canal"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Canais / grupos indexados**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Enviar arquivo de log"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Excluir arquivo do banco de dados"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Em processamento...⏳", quote=True)
    else:
        await message.reply('Responder ao arquivo com /delete qual você deseja deletar', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('Este formato de arquivo não é compatível')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('O arquivo foi excluído com sucesso do banco de dados')
    else:
        await msg.edit('Arquivo não encontrado no banco de dados')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'Isso excluirá todos os arquivos indexados.\nVocê quer continuar??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="SIM", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCELAR", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Todos os arquivos indexados foram excluídos com sucesso.')

