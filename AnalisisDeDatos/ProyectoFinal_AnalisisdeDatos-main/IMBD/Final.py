from pymongo import MongoClient
import psycopg2
import pandas as pd
# Conexion  a postgresql
connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='IMBD')
#Busqueda del archivo a enviar
empdata = pd.read_csv('SeriesIMBD.csv', index_col=False, delimiter =',', encoding="ISO-8859-1")
empdata.head()

print("Enviando datos a postgresql 🐘......")
cursor = connection.cursor()#Creamos un cursor
cursor.execute("Create table Series (tconst varchar(10),Titulo varchar(100),Genero varchar(100),NumVotos int8,PuntuacionMedia real,AñoInicio varchar(20),NombreSerie varchar(100))")
#For para insertar los datos en postgresql
for i, row in empdata.iterrows():
    sql = """INSERT INTO Series VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, tuple(row))
    connection.commit()
connection.close()


#Envio deSQl A mongo
print("Enviando datos a mongo 🍃......")
dburl = MongoClient('mongodb://localhost', 27017) #Establezco mi conexion Con MongodB
database = dburl['IMBD'] #Creacion de la base de datos
series= database.series #series es el nombre de la coleccion


connection = psycopg2.connect(host='localhost',user='postgres', password='sony1234',database='IMBD')
mycursor = connection.cursor()
mycursor.execute("SELECT * from Series;")

query_result = [ dict(line) for line in [zip([ column[0] for column in mycursor.description], row) for row in mycursor.fetchall()] ]
#print (query_result)

if len(query_result) > 0:
    x = series.insert_many(query_result)
    #y = series.insert_one(query_result).inserted_id
    connection.commit()
print("Base de datos exportada a MongoDB 🍃")
connection.close()
