import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user="root2",
passwd="root",
db="pysports")

cursor = connection.cursor()

query="SELECT first_name, last_name FROM player WHERE player_id ='3'"

cursor.execute(query)
rows=cursor.fetchall()

for x in rows:
    print(x)

connection.close()