# mydb.py (MySQL)
import mysql.connector

dataBase = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE comferre")

print("pass ok")