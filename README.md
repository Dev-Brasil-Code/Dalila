# Telegram Movie Bot

## Features

- [x] Filtro Automático
- [x] Manuel Filter
- [x] IMDB
- [x] Comandos de Admin
- [x] Transmissão
- [x] Índice
- [x] Pesquisa IMDB
- [x] Pesquisa Inline
- [x] Fotos aleatórias
- [x] ids e informações do usuário
- [x] Estatísticas, usuários, bate-papos, banir, cancelar, sair, desativar, canal


## Variáveis

### Variáveis ​​Requeridas
* `BOT_TOKEN`: Crie um bot usando [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Obtenha este valor de [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Obtenha este valor de [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Nome de usuário ou ID do canal ou grupo. Separe vários IDs por espaço
* `ADMINS`: Nome de usuário ou ID do administrador. Separe vários administradores por espaço
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Obtenha este valor de [mongoDB](https://www.mongodb.com)
* `DATABASE_NAME`: Nome do banco de dados em [mongoDB](https://www.mongodb.com)
* `LOG_CHANNEL` : Um canal para registrar as atividades do bot. Certifique-se de que o bot é um administrador no canal.
### Optional Variables
* `PICS`: Links de telegrama de imagens para mostrar na mensagem inicial. (Várias imagens podem ser usadas separadas por espaço)
* Verificar [info.py](info.py) para mais


## Deploy
Você pode implantar este bot em qualquer lugar.

<details><summary>Implantar no Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/Dev-Brasil-Code/Dalila/tree/master">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Implantar para VPS</summary>
<p>
<pre>
git clone https://github.com/Dev-Brasil-Code/Dalila
# Install Packages
pip3 install -r requirements.txt
Editar info.py com as variáveis ​​fornecidas abaixo, em seguida, execute o bot
python3 bot.py
</pre>
</p>
</details>


## Comandos de administração
```
• /logs - para obter os erros recentes
• /stats - para obter o status dos arquivos no banco de dados.
* /filter - adicionar filtros manuais
* /filters - ver filtros
* /connect - conectar ao PM.
* /disconnect - desconectar do PM
* /del - deletar um filtro
* /delall - deletar todos os filtros
* /deleteall - deletar todo o índice (filtro automático)
* /delete - exclua um arquivo específico do índice.
* /info - obter informações do usuário
* /id - obter ids tg.
* /imdb - buscar informações do imdb.
• /users - para obter a lista de meus usuários e ids.
• /chats - para obter a lista dos meus chats e isso 
• /index  - adicionar arquivos de um canal
• /leave  - para sair de um bate-papo.
• /disable  -  desabilite um chat.
* /enable - reative o bate-papo.
• /ban  - para banir um usuário.
• /unban  - para cancelar o banimento de um usuário.
• /channel - para obter a lista do total de canais conectados
• /broadcast - para transmitir uma mensagem a todos os usuários de Dalila
```

## Créditos 
* [![Zaute-Km](https://img.shields.io/static/v1?label=Dingdi-Dev&message=devs&color=critical)](https://telegram.dog/zautebot)


## Graças a 
 - Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey

## Isenção de responsabilidade
[![GNU Affero General Public License 3.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 3.0.](https://github.com/Dev-Brasil-Code/Dalila/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.
