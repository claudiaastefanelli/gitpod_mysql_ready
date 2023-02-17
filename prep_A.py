#Crea un programma che crei un DB chiamato Animali, contenente una tabella Mammiferi con i seguenti campi
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ANIMALI")