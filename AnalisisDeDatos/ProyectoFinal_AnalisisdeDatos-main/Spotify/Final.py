from pymongo import MongoClient
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import timeit
import pandas as pd
import pyodbc
start = timeit.default_timer()
#id Clave de usuario spotify, Secret Clave secreta
cid ="52aa01e5d89742a8a8e48e90ddbaa2eb"
secret = "3d11a4273c66438aaa122540917d00a1"
#Establezco la conexion con mis ids a spotify
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#Listo las propiedades generales en arreglos vacios de spotify
artist_name = []
track_name = []
popularity = []
track_id = []
#Establezco un rango el cul tendra el top d los artistas
for i in range(0, 1000, 50):
    track_results = sp.search(q='year:2022', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        #data = {artist_name.append(t['artists'][0]['name']),track_name.append(t['name']),track_id.append(t['id']),popularity.append(t['popularity'])}
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

    stop = timeit.default_timer()
    print('Tiempo para ejecutar este código (en segundos):', stop - start)
    print('Numero de elemnto en la lista track_id :', len(track_id))
    df_tracks = pd.DataFrame( {'artist_name': artist_name, 'track_name': track_name, 'track_id': track_id, 'popularity': popularity})
df_tracks.to_csv('musica.csv')

#MicrosofSqlserver
#Envio de la informacion spotify a Micrososft sql server
print("Envio datos a Microsoft SQL Server...")
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9LVDDH;DATABASE=Spotify;UID=sa;PWD=1234')

cursor = conn.cursor()
empdata = pd.read_csv('musica.csv', index_col=False, delimiter =',', encoding='utf-8')
empdata.head()

#Creamos una tabla musica en mysqlserver
cursor.execute("CREATE TABLE musica (num int,artist_name varchar(500),track_name varchar(500),track_id varchar(100),popularity int)")

for i, row in empdata.iterrows():
    #consulta = "Insert into musica"
    sql = "Insert into musica(num,artist_name,track_name,track_id,popularity) values (?,?,?,?,?)"
    cursor.execute(sql,tuple(row))
    conn.commit()
conn.close()


#Envio deSQl A mongo
print("Enviando datos a mongo......")
dburl = MongoClient('mongodb://localhost', 27017) #Establezco mi conexion Con MongodB
database = dburl['Spotify'] #Creacion de la base de datos
musica= database.musica #musica es el nombre de la coleccion

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9LVDDH;DATABASE=Spotify;UID=sa;PWD=1234')
mycursor = connection.cursor()
mycursor.execute("SELECT * from musica;")
query_result = [ dict(line) for line in [zip([ column[0] for column in mycursor.description], row) for row in mycursor.fetchall()] ]
#print (query_result)

if len(query_result) > 0:
    x = musica.insert_many(query_result)
    connection.commit()
   # print(len(x.inserted_ids))
print("Base de datos exportada a MongoDB")
connection.close()
