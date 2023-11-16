import mysql.connector

def connect_to_database():
            
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='hostelmanagement',
            )
            return connection

connection = connect_to_database()
cur = connection.cursor()

with open('Tables.sql') as f:
    cur.execute(f.read(), multi=True)