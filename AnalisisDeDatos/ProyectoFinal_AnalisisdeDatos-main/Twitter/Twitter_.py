#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# twiterCouch
import couchdb
import tweepy
from tweepy import OAuthHandler
import json
###API ########################
ckey = "o3JzU2JIlxGxANC57aLrQ2q6j"
csecret = "xjsM14A8h1rusARwJ29WsBVEHBW7Ns6kDKEnUiy1l1Vg4GZkbK"
atoken = "1401018163291119616-nEwFJzW6mXkdFB2B9IXNXwJx6JTncN"
asecret = "5Mvz77zbqIHvU4VPNxmD6mBmpVreMfMsho3y661TzMIxv"
#####################################
class listener(tweepy.Stream):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
            print(f"Los datos fueron guardados exitosamente en la base de datos politica_ de CouchDB")
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)

twitter_stream = listener(ckey, csecret,atoken,asecret)
server = couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('politica_')
except:
    db = server['politica_']
twitter_stream.filter(track=['LassoGuillermo','AbAlvaroNoboa','MashiRafael','MauricioRodasEC','CesarMontufar51']) 

print(f"Los datos fueron guardados exitosamente en la base de datos politica_ de CouchDB")


#@LassoGuillermo
#@AbAlvaroNoboa
#@MashiRafael
#@LucioGutierrez3
#@daloes10
#@pesanteztwof
#@MauricioRodasEC
#@CesarMontufar51


# In[ ]:





# In[1]:


#CouchMongo
from pymongo import MongoClient
import couchdb
couch =couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
CLIENT = MongoClient('mongodb://localhost:27017')
dbs=couch['politica_']#BD subida en CouchDB
database=CLIENT['twiter_mongo']#Nombre de la base de datos en mongo
coleccion=database.coleccion #Nombre de la coleccion
for docid in dbs.view('_all_docs'):
    id=docid['id']
    doc=dbs[id]
    dato = { "Descripcion": doc['text'],"Nombre": doc['source'], "Usuario": doc['user'],"Propiedades": doc['entities']}
    #dato={ "Descripcion": doc['text'],"Nombre": doc['source']}  #Cambiar los parametros
    #dato={ "_rev": doc['_rev'],"id": doc['id'],"texto": doc['texto'],"date": doc['date'],"likes": doc['likes'],"comments": doc['comments'],"shares": doc['shares']}
    #colect.insert_one(dato)
    envio=coleccion.insert_one(dato).inserted_id
print(f"Los datos de la base datos {dbs} de CouchDB fueron guardados exitosamente en la base de datos {database} de MongoDB")


# In[ ]:




