#!/usr/bin/env python
# coding: utf-8

# In[102]:


# 16
def mysqlMongoAtlas():
    import mysql.connector
    import datetime
    from pymongo import MongoClient
    dburl = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')
    database= dburl['mysqlMongoAtlas']
    datos=database.datos
    mysqldb = mysql.connector.connect(host='127.0.0.1', database='mongoatlasmysql', user='root', password='123456')
    mycursor = mysqldb.cursor(dictionary=True)
    mycursor.execute("SELECT * from mongoatlasmysql;")

    myresult = mycursor.fetchall()
    #datos.insert_all(myresult)
    if len(myresult) > 0:
            x = datos.insert_many(myresult) #myresult comes from mysql cursor
            #print(len(x.inserted_ids))
    #print(myresult)
    print(f"Los datos de la base datos mongoatlasmysql de MySql fueron guardados exitosamente en la base de datos mysqlMongoAtlas de MongDB Atlas")
    


# In[100]:


# 15 MongoDB - MySql
def mongoAtlasMysql():

    from pymongo import MongoClient
    import mysql.connector as msql
    import pandas as pd
    client = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')
    conn = msql.connect(host='127.0.0.1', database="mongoAtlasMySql",user='root', password='123456')

    #Examina ya trae la base de datos en mongo
    db = client.get_database('Facebookmysql')
    coleccion = db.get_collection('facebook')#Nombre de la coleccion en mongo
    df = pd.DataFrame(list(coleccion.find()))
    df.to_csv('facebookmysql2.csv')

    #Ubicacion del archivo a enviar
    empdata = pd.read_csv('C:\\Users\\Admi\\Desktop\\Universidad\\Tercer Semestre\\Analisis de Datos\\Trabajos\\Prueba\\facebookmysql2.csv', index_col=False, delimiter = ',')
    empdata.head()

    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("Estas conectado a la base de datos: ", record)
    cursor.execute("CREATE TABLE mongoAtlasMysql (numero int,_id varchar(16),Id INT,text varchar(500),likes int, comments int, shares int, post_url varchar(500))")

    for i, row in empdata.iterrows():
        sql = """INSERT INTO mongoAtlasMySql.mongoAtlasMysql VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, tuple(row))
        conn.commit()
    print(f"Los datos de la base datos facebookmysql de MongoAtkas fueron guardados exitosamente en la base de datos mongoAtlasMySql de MySql")


# In[98]:


# 14 
def mysqlMongo():
    import mysql.connector
    import datetime
    from pymongo import MongoClient
    dburl = MongoClient('mongodb://localhost', 27017)
    database= dburl['mysql_Mongo']
    datos=database.datos
    mysqldb = mysql.connector.connect(host='127.0.0.1', database='facebook', user='root', password='123456')
    mycursor = mysqldb.cursor(dictionary=True)
    mycursor.execute("SELECT * from mongomysql;")

    myresult = mycursor.fetchall()
    #datos.insert_all(myresult)
    if len(myresult) > 0:
            x = datos.insert_many(myresult) #myresult comes from mysql cursor
            #print(len(x.inserted_ids))
    print(myresult)
    print(f"Los datos de la base datos facebook de MySql fueron guardados exitosamente en la base de datos mysql_Mongo de MongoDB")


# In[5]:


# 13 MongoDB - MySql
def mongoMysql():

    from pymongo import MongoClient
    import mysql.connector as msql
    import pandas as pd
    client = MongoClient('mongodb://localhost', 27017)
    conn = msql.connect(host='127.0.0.1', database="facebook",user='root', password='123456')

    #Examina ya trae la base de datos en mongo
    db = client.get_database('Facebookmysql')
    coleccion = db.get_collection('facebook')#Nombre de la coleccion en mongo
    df = pd.DataFrame(list(coleccion.find()))
    df.to_csv('facebookmysql2.csv')

    #Ubicacion del archivo a enviar
    empdata = pd.read_csv('C:\\Users\\Admi\\Desktop\\Universidad\\Tercer Semestre\\Analisis de Datos\\Trabajos\\Prueba\\facebookmysql2.csv', index_col=False, delimiter = ',')
    empdata.head()

    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("Estas conectado a la base de datos: ", record)
    cursor.execute("CREATE TABLE mongoMysql (numero int,_id varchar(16),Id INT,text varchar(500),likes int, comments int, shares int, post_url varchar(500))")

    for i, row in empdata.iterrows():
        sql = """INSERT INTO facebook.mongoMysql VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, tuple(row))
        conn.commit()
    print(f"Los datos de la base datos facebook de Mongo fueron guardados exitosamente en la base de datos facebook de MySql")


# In[92]:


# 12 ***
def mongoAtlasCouch():
    import json
    from argparse import ArgumentParser
    import requests
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
    from bson import json_util, ObjectId
    import couchdb

    URL = 'http://Dominick:123456@localhost:5984' 
    print(URL)

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print('CouchDB connection: Success')
        if response.status_code == 401:
            print('CouchDB connection: failed', response.json())
    except requests.ConnectionError as e:
        raise e

    server=couchdb.Server(URL)
    HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    CLIENT = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')

    try:
        CLIENT.admin.command('ismaster')
        print('MongoDB connection: Success')
    except ConnectionFailure as cf:
        print('MongoDB connection: failed', cf)


    DBS=['Usuarios']    # Nomjbre base del mongoAtlas
 

    try:
        dbc=server.create('mongoatlas_couch')
    except:
        dbc=server['mongoatlas_couch']    # Nombre Base del couch 


    for db in DBS:
        if db not in ('admin', 'local','config'):  
            cols = CLIENT[db].list_collection_names()  
            for col in cols:
                print('Querying documents from collection {} in database {}'.format(col, db))
                for x in CLIENT[db][col].find():  
                    try:

                        documents=json.loads(json_util.dumps(x))

                        documents["_id"]=str(documents["_id"]["$oid"])


                        print(documents)
                        doc=dbc.save(documents)

                    except TypeError as t:

                        print('current document raised error: {}'.format(t))
                        SKIPPED.append(x)  # creating list of skipped documents for later analysis
                        continue    # continue to next document
                    except Exception as e:
                        raise e
    print(f"Los datos de la base datos {DBS} de MongoDB fueron guardados exitosamente en la base de datos {dbc} de CouchDB") 


# In[91]:


# 11 ***
def couchMongoAtlas():
    from pymongo import MongoClient
    import couchdb
    dburl = MongoClient('mongodb+srv://Admin:1234@cluster0.xngys.mongodb.net/test')
    database = dburl['couch_mongoAtlas'] #Creacion de la base de datos
    users= database.users #users es el nombre de la coleccion
    couch =couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
    dbs=couch['facebook_resint']#BD subida en CouchDB
    for docid in dbs.view('_all_docs'):
        id=docid['id']
        doc=dbs[id]
        dato={ "_rev": doc['_rev'],"id": doc['id'],"texto": doc['texto'],"date": doc['date'],"likes": doc['likes'],"comments": doc['comments'],"shares": doc['shares']}
        #colect.insert_one(dato)
        envio=users.insert_one(dato).inserted_id
    print(f"Los datos de la base datos facebook_resint de CouchDB fueron guardados exitosamente en la base de datos couch_mongoAtlas de MongoDB Atlas")


# In[88]:


# 10 ***
def couchMongo():
    from pymongo import MongoClient
    import couchdb
    couch =couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
    CLIENT = MongoClient('mongodb://localhost:27017')
    dbs=couch['facebook_resint']#BD subida en CouchDB
    database=CLIENT['couch_mongo']#Nombre de la base de datos en mongo
    coleccion=database.coleccion #Nombre de la coleccion
    for docid in dbs.view('_all_docs'):
        id=docid['id']
        doc=dbs[id]
        dato={ "_rev": doc['_rev'],"id": doc['id'],"texto": doc['texto'],"date": doc['date'],"likes": doc['likes'],"comments": doc['comments'],"shares": doc['shares']}
        #colect.insert_one(dato)
        envio=coleccion.insert_one(dato).inserted_id
    print(f"Los datos de la base datos {dbs} de CouchDB fueron guardados exitosamente en la base de datos {database} de MongoDB")


# In[87]:


# 9 ***
def mongoCouch():
    import json
    from argparse import ArgumentParser
    import requests
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
    from bson import json_util, ObjectId
    import couchdb

    URL = 'http://Dominick:123456@localhost:5984' 
    print(URL)

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print('CouchDB connection: Success')
        if response.status_code == 401:
            print('CouchDB connection: failed', response.json())
    except requests.ConnectionError as e:
        raise e

    server=couchdb.Server(URL)
    HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    CLIENT = MongoClient('mongodb://localhost:27017')

    try:
        CLIENT.admin.command('ismaster')
        print('MongoDB connection: Success')
    except ConnectionFailure as cf:
        print('MongoDB connection: failed', cf)


    DBS=['tiktokMongo']


    try:
        dbc=server.create('mongo_couch')
    except:
        dbc=server['mongo_couch']


    for db in DBS:
        if db not in ('admin', 'local','config'):  
            cols = CLIENT[db].list_collection_names()  
            for col in cols:
                print('Querying documents from collection {} in database {}'.format(col, db))
                for x in CLIENT[db][col].find():  
                    try:

                        documents=json.loads(json_util.dumps(x))

                        documents["_id"]=str(documents["_id"]["$oid"])


                        print(documents)
                        doc=dbc.save(documents)

                    except TypeError as t:

                        print('current document raised error: {}'.format(t))
                        SKIPPED.append(x)  # creating list of skipped documents for later analysis
                        continue    # continue to next document
                    except Exception as e:
                        raise e
    print(f"Los datos de la base datos tiktokMongo de MongoDB fueron guardados exitosamente en la base de datos mongo_couch de CouchDB") 


# In[83]:


# 8
def webScrapingMongo():
    from bs4 import BeautifulSoup
    import requests
    from pymongo import MongoClient

    client = MongoClient('mongodb://localhost', 27017)#Establecemos la conexion
    database = client['WebMongo'] #Nombre de la base de datos
    datos = database.datos #Nombre de l acoleccion
    data = {}


    urlBase = "https://game.capcom.com/residentevil/en/"
    maxPages = 20
    counter = 0

    for i in range(1,maxPages):

        # Construyo la URL
        if i > 1:
            url = "%spage/%d/" %(urlBase,i)
        else:
            url = urlBase

        # Realizamos la petición a la web
        req = requests.get(url)
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text)

            # Obtenemos todos los divs donde estan las entradas
            entradas = html.find_all('div',{'class':'col-md-4 col-xs-12'})

            # Recorremos todas las entradas para extraer el título, autor y fecha
            for entrada in entradas:
                counter += 1
                #titulo = entrada.find('span', {'class' : 'tituloPost'}).getText()
                #autor = entrada.find('span', {'class' : 'autor'}).getText()
                #fecha = entrada.find('span', {'class' : 'fecha'}).getText()

                #webd = {'titulo': titulo,'autor': autor,'fecha': fecha}
                webd1={'titulo': entrada.find('span', {'class' : 'tituloPost'}).getText(),'autor': entrada.find('span', {'class' : 'autor'}).getText(),'fecha': entrada.find('span', {'class' : 'fecha'}).getText()      }
                #print(webd1)
                #movie_ = {'title': 'Mr. Robot', 'Starring': 'Rami Malek, Christian Slater, Carly Chaikin',
                  #        'created': 'Sam Esmail', 'Year': '2016'}
                envio = datos.insert_one(webd1).inserted_id

                # Imprimo el Título, Autor y Fecha de las entradas
               # print ("%d - %s  |  %s  |  %s" %(counter,titulo,autor,fecha))

        else:
            # Si ya no existe la página y me da un 400
            break


# In[50]:


# 7
def tiktokMongo():
    from pymongo import MongoClient
    import csv

    name = str(input("Ingrese el nombre del archivo .csv: "))
    client = MongoClient('mongodb://localhost', 27017)#Establecemos la conexion
    database = client['tiktokMongo'] #Nombre de la base de datos
    hashtag= database.hashtag #Nombre de l acoleccion
    data = {}
    with open(name,encoding= 'utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['id']
            data[id] = rows
            envio = hashtag.insert_one(rows).inserted_id
    print(f"Los datos fueron guardados exitosamente en la base de datos tiktokMongo") 


# In[71]:


# 6
def facebookMongo():
    from facebook_scraper import get_posts
    from pymongo import MongoClient
    import time

    name = str(input("Ingrese el tema a buscar: "))
    dburl = MongoClient('mongodb://localhost', 27017)
    database = dburl['FacebookMongo'] #Creacion de la base de datos
    facebook= database.facebook #users es el nombre de la coleccion

    i = 1
    for post in get_posts(name, pages=2, extra_info=True):
        print(i)

        time.sleep(5)
        mydate = post['time']

        l={'Id':i,'text': post['text'],'date': mydate.timestamp(),'likes':post['likes'],'comments':post['comments'],'shares':post['shares'],'reactions':post['reactions'],'post_url':post['post_url']}
        id = facebook.insert_one(l).inserted_id
        i = i + 1
    print(f"Los datos fueron guardados exitosamente en la base de datos FacebookMongo") 


# In[57]:


# 5 ***
def twiterMongo():
    from pymongo import MongoClient
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
                doc = twiter.insert_one(dictTweet).inserted_id
                #print("SAVED" + str(doc) + "=>" + str(data))
                print(f"Los datos fueron guardados exitosamente en la base de datos twiter_resint de Mongo")
            except:
                print("Already exists")
                pass
            return True

        def on_error(self, status):
            print(status)

    twitter_stream = listener(ckey, csecret,atoken,asecret)

    try:
        dburl = MongoClient('mongodb://localhost', 27017)  #('http://115.146.93.184:5984/')
        db = dburl['TwiterMongo']
        twiter= db['Resint']
    except:
        print("Coneccion rechazada")
    #twiter= db.twiter
    twitter_stream.filter(track=['ResidentEvil'])
    


# In[82]:


# 4 ***
def webScrapingCouch():
    from bs4 import BeautifulSoup
    import requests
    import couchdb
    import csv
    
    couch = couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
    db = couch['web_couch']


    urlBase = "https://game.capcom.com/residentevil/en/"
    maxPages = 20
    counter = 0

    for i in range(1,maxPages):

        # Construyo la URL
        if i > 1:
            url = "%spage/%d/" %(urlBase,i)
        else:
            url = urlBase

        # Realizamos la petición a la web
        req = requests.get(url)
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text)

            # Obtenemos todos los divs donde estan las entradas
            entradas = html.find_all('div',{'class':'col-md-4 col-xs-12'})

            # Recorremos todas las entradas para extraer el título, autor y fecha
            for entrada in entradas:
                counter += 1
                titulo = entrada.find('span', {'class' : 'tituloPost'}).getText()
                autor = entrada.find('span', {'class' : 'autor'}).getText()
                fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                doc = {}
                doc['counter'] = counter
                doc['Titulo'] = entrada.find('span', {'class' : 'tituloPost'}).getText()
                doc['autor'] = entrada.find('span', {'class' : 'autor'}).getText()
                doc['fecha'] = entrada.find('span', {'class' : 'fecha'}).getText()
                db.save(doc)

                # Imprimo el Título, Autor y Fecha de las entradas
                #print ("%d - %s  |  %s  |  %s" %(counter,titulo,autor,fecha))
                print(f"Los datos fueron guardados exitosamente en la base de datos {db}")
                
                

        else:
            # Si ya no existe la página y me da un 400
            break


# In[ ]:





# In[77]:


# 3 ***
def tiktokCouch():
    import couchdb
    import json
    import csv

    name = str(input("Ingrese el nombre del archivo .csv: "))
    couch = couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
    db = couch['tiktok_couch']
    data={}

    with open(name,encoding= 'utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['id']
            data[id] = rows
            db.save(rows)
    print(f"Los datos fueron guardados exitosamente en la base de datos tiktok_couch") 


# In[67]:


# 2 ***
def facebookCouch():
    from facebook_scraper import get_posts
    import couchdb
    import json
    import time
      
    name = str(input("Ingrese el tema a buscar: "))
    couch=couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')
    nombredb='facebook_resint'                              # hay que crear una BD y cambiar a Resinde the evil
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

            print(f"Los datos fueron guardados exitosamente en la base de datos {nombredb}")

        except Exception as e:
            print("no se pudo grabar:" + str(e))


# In[51]:


# 1 ***
def twiterCouch():
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
                #print("SAVED" + str(doc) + "=>" + str(data))
                print(f"Los datos fueron guardados exitosamente en la base de datos twiter_resint de CouchDB")
            except:
                print("Already exists")
                pass
            return True

        def on_error(self, status):
            print(status)

    twitter_stream = listener(ckey, csecret,atoken,asecret)
    server = couchdb.Server('http://Dominick:123456@127.0.0.1:5984/')  #('http://115.146.93.184:5984/')
    try:
        db = server.create('twiter_resint')
    except:
        db = server['twiter_resint']
    twitter_stream.filter(track=['ResidentEvil'])
    print(f"Los datos fueron guardados exitosamente en la base de datos twiter_resint de CouchDB")


# In[ ]:





# In[103]:


print("********************************************************************")
print("*                          PRUEBA                                  *")
print("********************************************************************")
print("1. Twiter - CouchDB") # ***
print("2. Facebook - CouchDB") # ***
print("3. Tik-Tok - CouchDB") # ***
print("4. WebScraping - CouchDB") #***
print("5. Twiter - MongoDB") 
print("6. Facebook - MongoDB") # ***
print("7. Tik-Tok - MongoDB") # ***
print("8. WebScraping - MongoDB") #***
print("9. MongoDB - CouchDB") # ***
print("10. CouchDB - MongoDB") # ***
print("11. CouchDB - MongoDB Atlas") # ***
print("12. MongoDB Atlas - CouchDB") # ***
print("13. MongoDB - MySql") # ***
print("14. MySql - MongoDB") # ***
print("15. MongoDB Atlas - MySql") # ***
print("16. MySql - MongoDB Atlas") # ***
op = int(input("\nIngrese una opcion: "))


if op == 1:
    print("Twiter - CouchDB")
    twiterCouch()
    
elif op == 2:
    print ("\tFacebook - CouchDB")
    facebookCouch()
    
elif op == 3:
    print ("\tTik-Tok - CouchDB")
    tiktokCouch()
    
elif op == 4:
    print ("WebScraping - CouchDB")
    webScrapingCouch()
    
elif op == 5:
    print ("Twiter - MongoDB")
    twiterMongo()
    
elif op == 6:
    print ("\tFacebook - MongoDB")
    facebookMongo()
    
elif op == 7:
    print ("\tTik-Tok - MongoDB")
    tiktokMongo()
    
elif op == 8:
    print ("WebScraping - MongoDB")
    webScrapingMongo()
    
elif op == 9:
    print ("\tMongoDB - CouchDB")
    mongoCouch()
    
elif op == 10:
    print ("CouchDB - MongoDB")
    couchMongo()

elif op == 11:
    print ("CouchDB - MongoDB Atlas")
    couchMongoAtlas()
    
elif op == 12:
    print ("MongoDB Atlas - CouchDB")
    mongoAtlasCouch()
    
elif op == 13:
    print ("MongoDB - MySql")
    mongoMysql()
    
elif op == 14:
    print ("MySql - MongoDB")
    mysqlMongo()

elif op == 15:
    print ("MongoDB Atlas - MySql")
    mongoAtlasMysql()
    
elif op == 16:
    print ("MySql - MongoDB Atlas")
    mysqlMongoAtlas()
    
else:
    print("La opción que ingreso no es válida")


# In[ ]:




