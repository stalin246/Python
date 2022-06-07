from pymongo import MongoClient
import psycopg2
import pandas as pd

#Envio a Sqlpos por medio del csv

connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='ubicacion')
empdata = pd.read_csv('ec.csv', index_col=False, delimiter =',', encoding="ISO-8859-1")
empdata.head()

print("Enviando datos a postgresql 🐘......")
cursor = connection.cursor()
cursor.execute("Create table herec (Ciudad varchar(200),latitud real,longitud real,Pais varchar(200),iso2 varchar(200),Administrador varchar(200),Capital varchar(200),Poblacion int8,PoblacionPropia int8)")

for i, row in empdata.iterrows():
    sql = """INSERT INTO herec VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, tuple(row))
    connection.commit()
connection.close()

#Envio deSQl A mongo
print("Enviando datos a mongo 🍃......")
dburl = MongoClient('mongodb://localhost', 27017) #Establezco mi conexion Con MongodB
database = dburl['UBICACION'] #Creacion de la base de datos
herec= database.herec #herec es el nombre de la coleccion

connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='ubicacion')#Establezco conexion con Postgres
mycursor = connection.cursor()
mycursor.execute("SELECT * from herec;")

query_result = [ dict(line) for line in [zip([ column[0] for column in mycursor.description], row) for row in mycursor.fetchall()] ]
#print (query_result)

if len(query_result) > 0:
    x = herec.insert_many(query_result)
    connection.commit()
print("Base de datos exportada a MongoDB")
connection.close()
