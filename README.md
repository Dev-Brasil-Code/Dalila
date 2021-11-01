# Telegram Movie Bot

## Features

- [] Auto Filter
- [x] Manuel Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel


## Variables

### Required Variables
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


## Admin commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
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
