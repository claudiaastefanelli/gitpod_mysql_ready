#Scrivi un programma che inserisce all’interno del DB 5 Animali
#Verifica tramite la console dei comandi di aver inserito gli animali nel DB
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "ANIMALII"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('1', 'Roditore','Criceto', 1, 8),
  ('2', 'Gatto','Persiano', 4, 2),
  ('3', 'Felino', 'Leone', 120, 9),
  ('4', 'Pesci', 'Delfino', 160, 6),
  ('5', 'Cane', 'Bulldog', 8, 4),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")