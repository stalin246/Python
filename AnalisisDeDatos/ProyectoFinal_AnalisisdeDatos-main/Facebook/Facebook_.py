#!/usr/bin/env python
# coding: utf-8

# In[6]:


from facebook_scraper import get_posts
import couchdb
import json
import time

#conucrania 


name = str(input("Ingrese el tema a buscar: "))
couch=couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
nombredb='ucrania_'                              # Nombre de la base de datos Couch
db=couch[nombredb]
i = 1
for post in get_posts(name, pages=3, extra_info=True):
    print(i)
    i = i + 1
    time.sleep(5)

    id = post['post_id']
    doc = {}

    doc['id'] = id

    mydate = post['time']

    try:
        doc['texto'] = post['text']
        doc['date'] = mydate.timestamp()
        doc['likes'] = post['likes']

        doc['comments'] = post['comments']
        doc['shares'] = post['shares']
        try:
            doc['reactions'] = post['reactions']
        except:
            doc['reactions'] = {}
        doc['post_url'] = post['post_url']
        db.save(doc)

        print(f"Los datos fueron guardados exitosamente en la base de datos de Couch: ucrania_")

    except Exception as e:
        print("no se pudo grabar:" + str(e))


# In[ ]:





# In[7]:


from pymongo import MongoClient
import couchdb
couch =couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
CLIENT = MongoClient('mongodb://localhost:27017')
dbs=couch['ucrania_']#nombre_debase en couch
database=CLIENT['ucrania_mongo']#Nombre de la base de datos en mongo
coleccion=database.coleccion #Nombre de la coleccion
for docid in dbs.view('_all_docs'):
    id=docid['id']
    doc=dbs[id]
    dato={ "_rev": doc['_rev'],"id": doc['id'],"texto": doc['texto'],"date": doc['date'],"likes": doc['likes'],"comments": doc['comments'],"shares": doc['shares']}
    #colect.insert_one(dato)
    envio=coleccion.insert_one(dato).inserted_id
print(f"Los datos de la base datos ucrania_ de CouchDB fueron guardados exitosamente en la base de datos ucrania_mongo de MongoDB")


# In[ ]:


# Power Bi
#Texto, likes - embudo
#id, shares - Grafico circular

