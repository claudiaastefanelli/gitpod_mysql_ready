#Scrivi un programma che Chieda all’utente se vuole inserire un nuovo animale per 5 volte. Nota: ogni volta deve inserire tutti i dati.
#Utilizza il programma al punto B per verificare che i nuovi animali siano stati inseriti correttamente

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "ANIMALII"
)

mycursor = mydb.cursor()


for x in range(5):
    Nome= input("inserisci nome animale: ");
    Razza= input("inserisci razza animale: ");
    Peso= int( input("inserisci peso animale: "));
    Eta= int( input("inserisci eta animale: "));

    query = "INSERT INTO Mammiferi ( Nome_Proprio, Razza, Peso, Eta) VALUES(%s, %s, %s, %s)"
    values = (Nome, Razza, Peso, Eta)
    mycursor.execute(query, values)
    mydb.commit()

mycursor.close()
mydb.close()

