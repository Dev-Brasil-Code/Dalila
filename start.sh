echo "Cloning Repo...."
git clone https://github.com/Dev-Brasil-Code/Dalila.git /Dalila
cd /Dalila
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
