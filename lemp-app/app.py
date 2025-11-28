
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
 return f"""
<head>
<h1>LINUX KURSSIN NETTISIVUT!</h1>
<p1>MYSQL-kello on nyt {result[0]}</p1>
</head>

<body>
<br>
<button onClick="history.go(0);">Tässä on nappula joka päivittää sivun!</button>
<br>
<a href="http://86.50.23.172/data-analysis">TÄÄLTÄ LÖYTYY DATA-ANALYSIS</a>
<br>
<a href="http://86.50.23.172/chat">TÄÄLTÄ LÖYTYY CHAT-PALVELU!</a>


</body>
"""
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)

