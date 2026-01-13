import os
from dotenv import load_dotenv
from mysql.connector import connect

load_dotenv()

conn = connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Income;")
data = cursor.fetchall()

for row in data:
    print(row)


conn.close()
