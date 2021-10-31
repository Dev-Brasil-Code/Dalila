from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS

@Client.on_message((filters.private | filters.group) & filters.command('connect'))
async def addconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Insira no formato correto!</b>\n\n"
                "<code>/connect id do grupo</code>\n\n"
                "<i>Obtenha seu ID de grupo adicionando este bot ao seu grupo e use  <code>/id</code></i>",
                quote=True
            )
            return

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            await message.reply_text("Você deve ser um administrador em determinado grupo!", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "ID de grupo inválido!\n\nSe estiver correto, certifique-se de que estou presente em seu grupo!!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Conectado com sucesso a **{title}**\nAgora gerencie seu grupo do meu pm !",
                    quote=True,
                    parse_mode="md"
                )
                if chat_type in ["group", "supergroup"]:
                    await client.send_message(
                        userid,
                        f"Conectado a **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "Você já está conectado a este bate-papo!",
                    quote=True
                )
        else:
            await message.reply_text("Adicione-me como administrador no grupo", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text('Ocorreu algum erro! Tente mais tarde.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnect'))
async def deleteconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Clique /connections para ver ou desconectar de grupos!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Desconectado com sucesso deste chat", quote=True)
        else:
            await message.reply_text("Este bate-papo não está conectado a mim!\nFazer /connect conectar.", quote=True)


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "Não há conexões ativas !! Conecte-se a alguns grupos primeiro.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - ACTIVE" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Detalhes do seu grupo conectado ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
