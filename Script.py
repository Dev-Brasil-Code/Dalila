class script(object):
    START_TXT = """Olá {},

Bot Dalila <a href='https://t.me/Doacaoes_Full'>Dalila</a> ka ni e!

<b>Obrigado Por Todos 😍</b>"""

    HELP_TXT = """Hey {}

<b>Comandos Status</b>

    ABOUT_TXT = """<b>➥ O meu nome: Dalila
➥ O Criador: Adm Claynet
➥ Biblioteca: Pyrogram
➥ Língua: Python 𝟹
➥ Data Base: MongoDB
➥ Servidor Bot: AWS
➥ Status da versão: v1.0.1 [ Beta ]</b>"""

    SOURCE_TXT = """Ajuda: <b>NOTE:</b>
- Código-fonte Dalila. 
- Source: <a href='https://github.com/Dev-Brasil-Code/Dalila'>GitHub 👉 Clique aqui</a>

<b>DEVS:</b>
- <a href=https://t.me/admclaynet>Adm Claynet</a>

<b>GRUPOS:</b>
- <a href='https://t.me/Doacoes_Full_Chat'>Zoram Hnaruak</a>'

<b>CANAIS:</b>
- <a href='https://t.me/Doacoes_Full'>Doações Full</a>"""

    MANUELFILTER_TXT = """Ajuda: <b>Filtros</b>
 
- Filtro é o recurso no qual os usuários podem definir respostas automatizadas para uma determinada palavra-chave e tessa responderá sempre que uma palavra-chave for encontrada na mensagem.

<b>NOTE:</b>
1. Adicione como admin
2. Filtro de grupos Admin.
3. Os botões de alerta limitam oi 64 caracteres por ni

<b>Comandos filtros:</b>
• /filter - <code>Adicionar de filtro de grupo a.</code>
• /filters - <code>Filtros de grupo-a Salvar zawng zawng.</code>
• /del - <code>Filtro salvar pakhat chiah delete-na.</code>
• /delall - <code>Filtro salvar zawng zawng delete-na.(Group Owner Chauh)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Dalila ambos os botões inline de alerta de url leh a Suporte.

<b>NOTA:</b>
1. O Telegram não permite o envio de botões sem nenhum conteúdo, portanto, o conteúdo é obrigatório.
2. A Dalila suporta botões com qualquer tipo de mídia de telegrama.
3. Os botões devem ser analisados ​​corretamente como formato de redução.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Doacoes_full_chat)</code>

<b>Botões de alerta:</b>
<code>[Button Text](buttonalert:Esta é uma mensagem de alerta)</code>"""

    AUTOFILTER_TXT = """Ajuda: <b>Filtro Automático</b>

<b>NOTE:</b>
1. Torne-me o administrador do seu canal, se for privado.
2. Certifique-se de que seu canal não contém arquivos cam rip, pornografia e arquivos falsos.
3. Encaminhe a última mensagem para mim com aspas.
 Vou adicionar todos os arquivos desse canal ao meu banco de dados."""

    CONNECTION_TXT = """Ajuda: <b>Conexões</b>

- Usado para conectar o bot ao PM para gerenciar filtros 
- Ajuda a evitar spam em grupos.

<b>NOTE:</b>
1. Apenas administradores podem adicionar uma conexão.
2. Mandar <code>/connect</code> por me conectar ao seu PM

<b>Commands leh Hmandân:</b>
• /connect  - <code>Private Chat-a Connect on.</code>
• /disconnect  - <code>Grupo de desconexão lehna.</code>
• /connections - <code>Conexões zawng² enna.</code>"""

    EXTRAMOD_TXT = """Ajuda: <b>Módulos Extra</b>

<b>NOTE:</b>
Esses são os recursos extras do tessa

<b>Comandos e uso:</b>
• /id - <code>obter id de um usuário specifed.</code>
• /info  - <code>obter informações sobre um usuário.</code>
• /imdb  - <code>obter informações da fonte IMDb filme.</code>
• /search  - <code>As informações get filme a partir de várias fontes.</code>"""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTA:</b>
Módulos comandos Criador.

<b>Comandos e uso:</b>
• /logs - <code>para obter os erros recentes</code>
• /stats - <code>para obter o status dos arquivos no banco de dados.</code>
• /users - <code>para obter uma lista de meus usuários e ids.</code>
• /chats - <code>para obter a lista dos meus chats e ids </code>
• /leave  - <code>sair de um bate-papo.</code>
• /disable  -  <code>desabilite um chat.</code>
• /ban  - <code>banir um usuário.</code>
• /unban  - <code>para cancelar o banimento de um usuário.</code>
• /channel - <code>para obter a lista do total de canais conectados</code>
• /broadcast - <code>para transmitir uma mensagem a todos os usuários</code>"""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
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
