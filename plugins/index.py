import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from info import ADMINS, LOG_CHANNEL
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp
logger = logging.getLogger(__name__)
lock = asyncio.Lock()



@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    if query.data.startswith('index_cancel'):
        temp.CANCEL=True
        return await query.answer("Cancelando indexação")
    _, raju, chat, lst_msg_id, from_user = query.data.split("#")
    if raju == 'reject':
        await query.message.delete()
        await bot.send_message(int(from_user), f'Seu envio para indexação {chat} foi recusado por nossos moderadores.', reply_to_message_id=int(lst_msg_id))
        return

    if lock.locked():
        return await query.answer('Espere até que o processo anterior seja concluído.', show_alert=True)
    msg = query.message

    await query.answer('Em processamento...⏳', show_alert=True)
    if int(from_user) not in ADMINS:
        await bot.send_message(int(from_user), f'Seu envio para indexação {chat} foi aceito por nossos moderadores e será adicionado em breve.', reply_to_message_id=int(lst_msg_id))
    await msg.edit(
        "Iniciando a Indexação",
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Cancelar', callback_data='index_cancel')]]
        )
    )
    try:
        chat = int(chat)
    except:
        chat = chat
    await index_files_to_db(int(lst_msg_id), chat, msg, bot)


@Client.on_message(filters.forwarded & filters.private & filters.incoming)
async def send_for_index(bot, message):
    if message.forward_from_chat.type != 'channel':
        return
    
    last_msg_id = message.forward_from_message_id
    chat_id = message.forward_from_chat.username or message.forward_from_chat.id
    try:
        await bot.get_messages(chat_id, last_msg_id)
    except:
        return await message.reply('Certifique-se de que sou um administrador no canal, se o canal for privado')
    
    if message.from_user.id in ADMINS:
        buttons = [
            [
                InlineKeyboardButton('Sim', callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')
            ],
            [
                InlineKeyboardButton('Fechar', callback_data='close_data'),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        return await message.reply(f'Quer indexar este canal?\n\nID de bate-papo/ Nome do usuário: <code>{chat_id}</code>\nID da última mensagem: <code>{last_msg_id}</code>', reply_markup=reply_markup)

    if not message.forward_from_chat.username:
        try:
            link = (await bot.create_chat_invite_link(chat_id)).invite_link
        except ChatAdminRequired:
            return await message.reply('Certifique-se de que eu seja um administrador no bate-papo e tenha permissão para convidar usuários.')
    else:
        link = f"@{message.forward_from_chat.username}"
    buttons = [
        [
            InlineKeyboardButton('Aceitar índice', callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')
        ],
        [
            InlineKeyboardButton('Índice de rejeição', callback_data=f'index#reject#{chat_id}#{message.message_id}#{message.from_user.id}'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(LOG_CHANNEL, f'#IndexRequest\n\nBy : {message.from_user.mention}\nChat ID/ Nome do usuário - <code> {chat_id}</code>\nID da última mensagem - <code>{last_msg_id}</code>\nInviteLink - {link}', reply_markup=reply_markup)
    await message.reply('Obrigado pela contribuição, espere que meus moderadores verifiquem os arquivos.')
        
        

@Client.on_message(filters.command('setskip') & filters.user(ADMINS))
async def set_skip_number(bot, message):
    if ' ' in message.text:
        _, skip = message.text.split(" ")
        try:
            skip = int(skip)
        except:
            return await message.reply("O número de salto deve ser um inteiro.")
        await message.reply(f"Definido com sucesso o número SKIP como {skip}")
        temp.CURRENT=int(skip)
    else:
        await message.reply("Dê-me um número de salto")


async def index_files_to_db(lst_msg_id, chat, msg, bot):
    total_files = 0
    async with lock:
        try:
            total=lst_msg_id + 1
            current=temp.CURRENT
            temp.CANCEL=False
            while current < total:
                if temp.CANCEL:
                    await msg.edit("Cancelado com sucesso")
                    break
                try:
                    message = await bot.get_messages(chat_id=chat, message_ids=current, replies=0)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    message = await bot.get_messages(
                        chat,
                        current,
                        replies=0
                        )
                except Exception as e:
                    print(e)
                try:
                    for file_type in ("document", "video", "audio"):
                        media = getattr(message, file_type, None)
                        if media is not None:
                            break
                        else:
                            continue
                    media.file_type = file_type
                    media.caption = message.caption
                    await save_file(media)
                    total_files += 1
                except TypeError:
                    pass
                except Exception as e:
                    print(e)
                current+=1
                if current % 20 == 0:
                    can = [[InlineKeyboardButton('Cancelar', callback_data='index_cancel')]]
                    reply = InlineKeyboardMarkup(can)
                    await msg.edit_text(
                        text=f"Total de mensagens obtidas: <code>{current}</code>\nTotal mensagens salvou: <code>{total_files}</code>",
                        reply_markup=reply)
        except Exception as e:
            logger.exception(e)
            await msg.edit(f'Error: {e}')
        else:
            await msg.edit(f'Total <code>{total_files}</code> Salvo em Base de dados!')
