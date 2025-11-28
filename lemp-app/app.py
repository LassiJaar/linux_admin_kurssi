
from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')
def home():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="exampleuser",
 password="SALASANA",
 database="exampledb"
 )
 cursor = conn.cursor()
 cursor.execute("SELECT CURTIME()")
 result = cursor.fetchone()
 # Clean up
 cursor.close()
 conn.close()
 with open('app.html', 'r') as ff:
  html_string = ff.read()
 return html_string

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)

