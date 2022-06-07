from pymongo import MongoClient
import psycopg2
import pandas as pd

#Envio a Sqlpos por medio del csv

connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='METACRITIC')
empdata = pd.read_csv('games-data.csv', index_col=False, delimiter =',', encoding="ISO-8859-1")
empdata.head()

print("Enviando datos a postgresql 🐘......")
cursor = connection.cursor()
cursor.execute("Create table Videogames (Titulo varchar(200),plataforma varchar(200),lanzamiento varchar(200),Puntuacion int,PuntuacionUsuario varchar(200),Desarrollador varchar(200),Genero varchar(200),Jugadores varchar(200),Criticas int,Usuarios int)")

for i, row in empdata.iterrows():
    sql = """INSERT INTO Videogames VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, tuple(row))
    connection.commit()
connection.close()

#Envio deSQl A mongo
print("Enviando datos a mongo 🍃......")
dburl = MongoClient('mongodb://localhost', 27017) #Establezco mi conexion Con MongodB
database = dburl['Metacritic'] #Creacion de la base de datos
videogames= database.videogames #videogames es el nombre de la coleccion

connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='METACRITIC')#Establezco conexion con Postgres
mycursor = connection.cursor()
mycursor.execute("SELECT * from Videogames;")

query_result = [ dict(line) for line in [zip([ column[0] for column in mycursor.description], row) for row in mycursor.fetchall()] ]
#print (query_result)

if len(query_result) > 0:
    x = videogames.insert_many(query_result)
    connection.commit()
print("Base de datos exportada a MongoDB")
connection.close()
