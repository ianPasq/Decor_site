import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passwordsafe",
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE auth")