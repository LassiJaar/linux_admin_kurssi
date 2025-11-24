#!/usr/bin/env python3
import requests
import mysql.connector
from datetime import datetime
API_KEY = 'bd16aeeecb576eafefd1d9d6143b3b53'
CITY = 'Helsinki'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY>
conn = mysql.connector.connect(host='localhost', user='exampleuser', password='>
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (id INT AUTO_INCREMEN>
response = requests.get(URL)
data = response.json()
temp = data['main']['temp']
desc = data['weather'][0]['description']
timestamp = datetime.now()
cursor.execute('INSERT INTO weather_data (city, temperature, description, times>
conn.commit()
cursor.close()
conn.close()
print(f'Data tallennettu: {CITY} {temp}°C {desc}')
