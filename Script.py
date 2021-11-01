class script(object):
    START_TXT = """Hello {},

Kei oi <a href='https://t.me/'>Dingdi</a> ka ni e!

<b>I Filme bom né 😍</b>"""

    HELP_TXT = """Ei {}

<b>Estou aqui pra ajudar-lo basta me dizer quais sao sua ordens</b>"""

    ABOUT_TXT = """<b>➥ Meu nome: Dalila
➥ Criador: AdmClaynet
➥ Library: Pyrogram
➥ Linguagem: Python 𝟹
➥ Base de dados: MongoDB
➥ Servidor Bot: AWS
➥ Status da versão: v1.0.1 [ Beta ]</b>"""

    SOURCE_TXT = """<b>NOTA:</b>
- Meu OpenSource esta aqui contribua com o projeto. 
- Source: <a href='https://github.com/Dev-Brasil-Code/Dalila'>GitHub 👉 Clique aqui</a>

<b>DEVS:</b>
- <a href=https://t.me/admclaynet>Adm Claynet</a>

<b>GRUPOS:</b>
- <a href='https://t.me/joinchat/CyMpHLeZPvQ0M2Ix'>Doacoes Full Chat</a>

<b>CANAIS:</b>
- <a href='https://t.me/joinchat/UF6hMfaaBUKx3b_q'>Doacoes Full Channel</a>"""

    MANUELFILTER_TXT = """Ajuda: <b>Filtros</b>

- O filtro é o recurso no qual os usuários podem definir respostas automáticas para uma determinada palavra-chave e tessa responderá sempre que uma palavra-chave for encontrada na mensagem

<b>NOTA:</b>
1. Me coloque como adm
2. Filtro de Admin de grupo
3. Os botões de alerta limitam oi 64 caracteres.

<b>Commands Filtros:</b>
• /filter - <code>Adicionar filtro</code>
• /filters - <code>Ver filtros do grupo.</code>
• /del - <code>Deletar filtro</code>
• /delall - <code>Deletar todos os filtros. (Dono do Grupo Chauh)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Dingdi hian both url leh alert inline buttons a Support.

<b>NOTE:</b>
1. O Telegram não permite o envio de botões sem nenhum conteúdo, portanto, o conteúdo é obrigatório.
2. A Dalila suporta botões com qualquer tipo de mídia de telegrama.
3. Os botões devem ser analisados ​​corretamente como formato de redução.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/mizotelegram)</code>

<b>Botões de alerta:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTA:</b>
1. Torne-me o administrador do seu canal, se for privado.
2. Certifique-se de que seu canal não contém arquivos cam rip, pornografia e arquivos falsos.
3. Encaminhe a última mensagem para mim com aspas.
 Vou adicionar todos os arquivos desse canal ao meu banco de dados."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Usado para conectar o bot ao PM para gerenciar filtros 
- Ajuda a evitar spam em grupos.

<b>NOTE:</b>
1. Apenas administradores podem adicionar uma conexão.
2. Mandar <code>/connect</code> por me conectar ao seu PM

<b>Commands conecxoes:</b>
• /connect  - <code>Conecte ao seu grupo/canal.</code>
• /disconnect  - <code>Desconectar grupo/canal.</code>
• /connections - <code>Verificar conexões</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTA:</b>
Esses são os recursos extras do tessa

<b>Comandos Extramods:</b>
• /id - <code>obter id de um usuário especificado.</code>
• /info  - <code>obter informações sobre um usuário.</code>
• /imdb  - <code>obter as informações do filme da fonte IMDb.</code>
• /search  - <code>obter as informações do filme de várias fontes.</code>"""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTA:</b>
Estes são comandos apenas para os ADM.

<b>Commands and Usage:</b>
• /logs - <code>para obter os erros recentes</code>
• /stats - <code>para obter o status dos arquivos em db.</code>
• /users - <code>para obter a lista de meus usuários e ids.</code>
• /chats - <code>para obter a lista dos meus chats e ids </code>
• /leave  - <code>para sair de um bate-papo.</code>
• /disable  -  <code>desabilite o chat.</code>
• /ban  - <code>para banir um usuário.</code>
• /unban  - <code>para cancelar o banimento de um usuário.</code>
• /channel - <code>para obter a lista do total de canais conectados</code>
• /broadcast - <code>para transmitir uma mensagem a todos os usuários</code>"""

    STATUS_TXT = """<b>Total de arquivos:</b> <code>{}</code>
<b>Total de usuários:</b> <code>{}</code>
<b>Total de bate-papos:</b> <code>{}</code>
<b>Armazenamento Usado:</b> <code>{}</code> 𝙼𝚒𝙱
<b>Armazenamento grátis:</b> <code>{}</code> 𝙼𝚒𝙱"""

    LOG_TEXT_G = """#Novo grupo
Grupo = {}(<code>{}</code>)
Total de membros = <code>{}</code>
Adicionado por - {}
"""

    LOG_TEXT_P = """#Novo usuário
ID - <code>{}</code>
Nome - {}
"""
