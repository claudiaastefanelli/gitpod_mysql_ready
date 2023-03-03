#Crea un programma che crei un DB chiamato Animali, contenente una tabella Mammiferi con i seguenti campi
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ANIMALII")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALII"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")