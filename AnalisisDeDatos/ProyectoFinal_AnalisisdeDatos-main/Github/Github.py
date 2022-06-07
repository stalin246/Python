#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as msql
import pandas as pd

conn = msql.connect(host='127.0.0.1', database="libros",user='root', password='123456')

#Examina ya trae la base de datos en mongo


#Ubicacion del archivo a enviar
empdata = pd.read_csv('C:\\Users\\Admi\\Desktop\\Universidad\\Tercer Semestre\\Analisis de Datos\\Trabajos\\Examen_\\libros.csv', index_col=False, delimiter = ',')
empdata.head()

cursor = conn.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("Estas conectado a la base de datos: ", record)
cursor.execute("CREATE TABLE libros_amazon (NAME  varchar(500),AUTOR varchar(50),User_rating float,Reviews int,Price int, Year int, Genre varchar(50))")

for i, row in empdata.iterrows():
    sql = """INSERT INTO libros.libros_amazon VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, tuple(row))
    conn.commit()
print(f"Los datos del archivo .csv fueron guardadis en la base de datos libros de MySql")


#Name,Author,User Rating,Reviews,Price,Year,Genre


# In[2]:


#Mysql-Mongo
import mysql.connector
import datetime
from pymongo import MongoClient
dburl = MongoClient('mongodb://localhost', 27017)
database= dburl['libros_prueba']
datos=database.datos
mysqldb = mysql.connector.connect(host='127.0.0.1', database='libros', user='root', password='123456')
mycursor = mysqldb.cursor(dictionary=True)
mycursor.execute("SELECT * from libros_amazon;")

myresult = mycursor.fetchall()
#datos.insert_all(myresult)
if len(myresult) > 0:
        x = datos.insert_many(myresult) #myresult comes from mysql cursor
        #print(len(x.inserted_ids))
print(myresult)
print(f"Los datos de la base datos facebook de MySql fueron guardados exitosamente en la base de datos mysql_Mongo de MongoDB")


# In[ ]:




