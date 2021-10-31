from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-----------------------------------------https://t.me/Doacoes_full --------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NÃO PERMITIDO 🐞\n\nMeus administradores me restringiram de trabalhar aqui! Se você quiser saber mais sobre isso, entre em contato com o suporte..</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('ℹ️ Ajuda', url=f"https://t.me/{temp.U_NAME}?start=help"),
            InlineKeyboardButton('📢 Atualizações', url='https:/t.me/Doações_full')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>Obrigado por me adicionar {message.chat.title} ❣️\n\nSe você tiver alguma dúvida sobre como me usar, entre em contato com o suporte.</b>",
            reply_markup=reply_markup)
    else:
        for u in message.new_chat_members:
            if (temp.MELCOW).get('welcome') is not None:
                try:
                    await (temp.MELCOW['welcome']).delete()
                except:
                    pass
            temp.MELCOW['welcome'] = await message.reply(f"<b>👋 Olá! {u.mention},</b> Bem-vindo ao <b>{message.chat.title}</b>")


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Dê-me um id de bate-papo ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Olá amigos, \nMeu administrador me disse para sair do grupo, então eu vou! Se você quiser me adicionar novamente, entre em contato com meu grupo de suporte.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Me dê um id de bate-papo')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Nenhum motivo fornecido"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Dê-me um ID de bate-papo válido')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Bate-papo não encontrado no banco de dados")
    if cha_t['is_disabled']:
        return await message.reply(f"Este bate-papo já está desativado:\nRazão-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Bate-papo desativado com sucesso')
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Olá amigos, \nMeu administrador me disse para sair do grupo, então eu vou! Se você quiser me adicionar novamente, entre em contato com meu grupo de suporte.</b> \nRazão : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Me dê um id de bate-papo')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Dê-me um ID de bate-papo válido')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Bate-papo não encontrado no banco de dados !")
    print(sts)
    if not sts.get('is_disabled'):
        return await message.reply('Este bate-papo ainda não está desativado.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Bate-papo reativado com sucesso")


@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Buscando estatísticas..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))


# a function for trespassing into others groups, Inspired by a Vazha
# Not to be used , But Just to showcase his vazhatharam.
# @Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Me dê um id de bate-papo')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Dê-me um ID de bate-papo válido')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Falha na geração do link de convite, Iam não tem direitos suficientes")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Aqui está o seu link de convite {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('Dê-me um ID de usuário / nome de usuário')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Nenhum motivo fornecido"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Este é um usuário inválido, certifique-se de tê-lo conhecido antes.")
    except IndexError:
        return await message.reply("Este pode ser um canal, certifique-se de que é um usuário.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} já está banido\nRazão: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Banido com sucesso {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Dê-me um ID de usuário / nome de usuário')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Nenhum motivo fornecido"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Este é um usuário inválido, certifique-se de tê-lo conhecido antes.")
    except IndexError:
        return await message.reply("Pode ser um canal, certifique-se de que é um usuário.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} ainda não foi banido.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Banido com sucesso {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Obtendo lista de usuários')
    users = await db.get_all_users()
    out = "Os usuários salvos no banco de dados são:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>\n"
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="Lista de usuários")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Obtendo lista de bate-papos')
    chats = await db.get_all_chats()
    out = "Os bate-papos salvos no banco de dados são:\n\n"
    async for chat in chats:
        out += f"**Título:** `{chat['title']}`\n**- ID:** `{chat['id']}`\n"
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="Lista de bate-papos")
