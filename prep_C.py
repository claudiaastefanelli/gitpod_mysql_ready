#Scrivi un programma che stampi gli animali inseriti al punto B

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "ANIMALII"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from Mammiferi")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)