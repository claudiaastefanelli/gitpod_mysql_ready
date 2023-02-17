#Seleziono tutti i record dalla tabella "clienti" e visualizzo il risultato:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()


 #utilizzare l'istruzione "SELECT" seguito dal/i nome/i della colonna per  selezionare solo alcune delle colonne in una tabella
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

#utilizzo fetchone() per farmi restituire la prima riga del risultato:

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

