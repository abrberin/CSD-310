import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="root", 
    database="pysports"
)

if connection.is_connected():
    print("Connected to the pysports database")


    cursor = connection.cursor()

    team_query = "SELECT team_id, team_name, mascot FROM team"

    cursor.execute(team_query)

    print("Team Table:")
    for (team_id, team_name, mascot) in cursor:
        print(f"Team ID: {team_id}, Team Name: {team_name}, Mascot: {mascot}")

    player_query = "SELECT player_id, first_name, last_name, team_id FROM player"

    cursor.execute(player_query)

    print("\nPlayer Table:")
    for (player_id, first_name, last_name, team_id) in cursor:
        print(f"Player ID: {player_id}, First Name: {first_name}, Last Name: {last_name}, Team ID: {team_id}")

    cursor.close()
    connection.close()

else:
    print("Connection to the pysports database failed")
