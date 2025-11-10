from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')
def home():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="exampleuser",
 password="MUISTA LAITTAA SALASANA TÄHÄN",
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
<h1>TERVEHDYS SINULLE!</h1>
<p1>MYSQL-kello on nyt {result[0]}</p1>
</head>
<body>
<button onClick="history.go(0);">Tässä on nappula joka päivittää sivun!</button>
<iframe width="420" height="345" src="https://www.youtube.com/embed/muRo4F7n4RI" title="Ikea reissu tiedossa (Reupload)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></ifra>

</body>
"""

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
