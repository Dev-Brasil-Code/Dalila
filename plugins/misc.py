import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == "private":
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>➲ Primeiro nome:</b> {first}\n<b>➲ Último nomee:</b> {last}\n<b>➲ Nome do usuário:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += (
            "<b>➲ ID de bate-papo</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>➲ ID do usuário</b>: "
                f"<code>{message.from_user.id}</code>\n"
                "<b>➲ ID de usuário respondida</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ ID do usuário</b>: "
                f"<code>{message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Buscando informações do usuário...`"
    )
    await status_message.edit(
        "`Processando informações do usuário...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("Não válido ID do usuário / mensagem especificada")
    else:
        message_out_str = ""
        message_out_str += f"<b>➲Primeiro nome:</b> {from_user.first_name}\n"
        last_name = from_user.last_name or "<b>None</b>"
        message_out_str += f"<b>➲Último nome:</b> {last_name}\n"
        message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
        username = from_user.username or "<b>None</b>"
        dc_id = from_user.dc_id or "[O usuário não tem um DP válido]"
        message_out_str += f"<b>➲Centro de dados:</b> <code>{dc_id}</code>\n"
        message_out_str += f"<b>➲Nome do usuário:</b> @{username}\n"
        message_out_str += f"<b>➲Usuário 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Clique aqui</b></a>\n"
        if message.chat.type in (("supergroup", "channel")):
            try:
                chat_member_p = await message.chat.get_member(from_user.id)
                joined_date = datetime.fromtimestamp(
                    chat_member_p.joined_date or time.time()
                ).strftime("%Y.%m.%d %H:%M:%S")
                message_out_str += (
                    "<b>➲Entrou neste bate-papo em:</b> <code>"
                    f"{joined_date}"
                    "</code>\n"
                )
            except UserNotParticipant:
                pass
        chat_photo = from_user.photo
        if chat_photo:
            local_user_photo = await client.download_media(
                message=chat_photo.big_file_id
            )
            buttons = [[
                InlineKeyboardButton('🔐 Fechar', callback_data='close_data')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(
                photo=local_user_photo,
                quote=True,
                reply_markup=reply_markup,
                caption=message_out_str,
                parse_mode="html",
                disable_notification=True
            )
            os.remove(local_user_photo)
        else:
            buttons = [[
                InlineKeyboardButton('🔐 Fechar', callback_data='close_data')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_text(
                text=message_out_str,
                reply_markup=reply_markup,
                quote=True,
                parse_mode="html",
                disable_notification=True
            )
        await status_message.delete()

@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Pesquisando ImDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("Nenhum resultado encontrado")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('Aqui está o que eu encontrei em IMDb', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Me dá um filme / nome da série')

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')} - {imdb.get('year')}",
                    url=imdb['url'],
                )
            ]
        ]
    if imdb.get('poster'):
        await query.message.reply_photo(photo=imdb['poster'], caption=f"IMDb Data:\n\n🏷 Título:<a href={imdb['url']}>{imdb.get('title')}</a>\n🎭 Gêneros: {imdb.get('genres')}\n📆 Ano:<a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n🌟 Avaliação: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\n🖋 Enredo: <code>{imdb.get('plot')} </code>", reply_markup=InlineKeyboardMarkup(btn))
        await query.message.delete()
    else:
        await query.message.edit(f"IMDb Data:\n\n🏷 Título:<a href={imdb['url']}>{imdb.get('title')}</a>\n🎭 Gêneros: {imdb.get('genres')}\n📆 Ano:<a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n🌟 Avaliação: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10\n🖋 Enredo: <code>{imdb.get('plot')} </code>", reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await query.answer()
        

        
