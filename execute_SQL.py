import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def connect_to_database():
    connection = mysql.connector.connect(
        host=os.environ["HOST"],
        port=3306,
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        database=os.environ["DATABASE"],
    )
    return connection


connection = connect_to_database()
cur = connection.cursor()

with open("Tables.sql") as f:
    cur.execute(f.read(), multi=True)
