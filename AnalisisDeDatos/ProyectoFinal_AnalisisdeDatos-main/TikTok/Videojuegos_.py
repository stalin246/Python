#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Tiktok_MongoAtlas
from pymongo import MongoClient
import csv

name = str(input("Ingrese el nombre del archivo .csv: "))
dburl = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')
database= dburl['Videojuegos_Mongo']
hashtag= database.hashtag #Nombre de l acoleccion

data = {}
with open(name,encoding= 'utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows
        envio = hashtag.insert_one(rows).inserted_id
print(f"Los datos fueron guardados exitosamente en la base de datos Videojuegos_Mongo") 


# In[4]:


#MongoAtlas_Mongo
from pymongo import MongoClient
import pandas as pd

# Obteniendo la coleccion de mongo atlas
client = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')
db = client.get_database('Videojuegos_Mongo') # Dayabases
info = db.get_collection('hashtag') # Colection
#df = pd.DataFrame(list(info.find()))

#Iniciando en MongoDB
CLIENT = MongoClient('mongodb://localhost:27017')
database=CLIENT['MongoAtlas_Mongo']#Nombre de la base de datos en mongo
coleccion=database.coleccion #Nombre de la coleccion

for documento in info.find({}):
    envio=coleccion.insert_one(documento).inserted_id # Envio de datos
    #print(documento)

print(f"Los datos de la base datos de CouchDB fueron guardados exitosamente en la base de datos de MongoDB")


# In[ ]:




