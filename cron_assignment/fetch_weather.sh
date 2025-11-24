#!/bin/bash
# Polku virtuaaliympäristöön
VENV_DIR="/home/ubuntu/cron_assignment/venv"
# Luo virtuaaliympäristö, jos ei ole olemassa
if [ ! -d "$VENV_DIR" ]; then
 echo "Luodaan virtuaaliympäristö..."
 python3 -m venv $VENV_DIR
fi
# Aktivoi virtuaaliympäristö
. $VENV_DIR/bin/activate
cd /home/ubuntu/cron_assignment
# Asenna riippuvuudet requirements.txt-tiedostosta
if [ -f "requirements.txt" ]; then
 echo "Asennetaan riippuvuudet..."
 pip install --upgrade pip
 pip install -r requirements.txt
else
 echo "requirements.txt ei löytynyt!"
fi
# Suorita fetch_weather.py
if [ -f "fetch_weather.py" ]; then
 echo "Suoritetaan fetch_weather.py..."
 python fetch_weather.py
else
 echo "fetch_weather.py ei löytynyt!"
fi
echo "Valmis!"

