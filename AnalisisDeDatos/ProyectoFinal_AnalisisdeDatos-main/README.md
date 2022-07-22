# RECOPILACIÓN DE DATOS Y POWER BI

## Integrantes :
- Bryan Tandazo
- Luis Valencia

### Data lake
![Modelo a realizar](https://user-images.githubusercontent.com/77359338/156857788-a561dc97-484e-46fa-95fb-19671eae47be.jpg)

### Bases de Datos No Relacionales y Relacionales
![image](https://user-images.githubusercontent.com/77359338/156857877-b6d5db65-101d-4029-850c-741faad7cf6b.png)

### Librerías Importantes
- Twitter: import tweepy
- Facebook: import facebook_scraper
- Spotify: import Spotipy
- Mysql: import mysql.connector
- MongoDb: import pymongo
- PostgreSQL: import psycopg2
- Microsoft SQL server: import pyodbc
- CouchDb: import couchdb
- Data Frame: import pandas
- Manejo de archivos: import json

##### Nota: 
Para realizar la sincronizacion de 🍃MongoDb con 📶Power Bi debemos instalar un drive para ello aquí esta el link de donde se puede descargar con una pequeña guía.
[link](https://www.magnitude.com/blog/connect-mongodb-tableau)

### 1. Politica en Ecuador

#### ![Captura de pantalla (2365)](https://user-images.githubusercontent.com/77359338/156854535-cf39b369-79bd-4689-8ce8-8c4cfe274158.png)

Para la recopilación de la información acerca de la política en Ecuador se utilizó la red social de Twitter, en donde por medio del siguiente script se extrajo la información, se almacenó en couchDb y finalmente la información fue migrada a MongoDB.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/Twitter) 

### 2. Noticias en Ucrania

#### ![Captura de pantalla (2367)](https://user-images.githubusercontent.com/77359338/156854836-a10d0668-a7af-4692-9500-dec616354535.png)

Lo  primero que se realizó fue recopilar información de todo lo referente a Ucrania, y una vez obtenida la información se la almacenó en la base de datos de CouchDB y luego migramos la información, todo eso lo realizamos mediante el siguiente script.
[codelink](AnalisisDeDatos/ProyectoFinal_AnalisisdeDatos-main/Facebook/Facebook_.py)

### 3. Juegos en linea

#### ![Captura de pantalla (2370)](https://user-images.githubusercontent.com/77359338/156855143-965b39c7-3833-41a4-98fa-059651efca81.png)

Para la recopilación de datos se utilizó la plataforma de Tiktok, mediante el cmd se obtuvo el archivo .csv el cual contenía información acerca de los juegos populares. Luego el archivo fue subida a la base de datos MongoDB atlas  y posteriormente fue migrada a MongoDb.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/TikTok)

### 4. Libros más vendidos

#### ![Captura de pantalla (2371)](https://user-images.githubusercontent.com/77359338/156855276-87d6f6c4-135a-4324-9d69-532a99ba7317.png)

Para la recopilación de datos de los libros más vendidos se buscó un archivo .csv en donde contenía toda la información y luego dicha información fue almacenada en la Base de datos Mysql y posteriormente dicha información fue migrada MongoDB, todo eso se realizó mediante el script.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/Github)

### 5. Canciones más escuchadas

#### ![Captura de pantalla (2374)](https://user-images.githubusercontent.com/77359338/156855644-db5d166c-c5a1-4faa-b28b-b55dde30c51b.png)

Para poder recolectar datos de Spotify tenemos que registrarnos como desarrollador en su plataforma para que de esta manera tengamos acceso a las claves que nos servirán en python. Spotipy es la librería que debemos instalar en nuestro compilador para establecer la conexión de además de la de librería de SQL de Microsoft la cual después importara la base de datos a MongoDB.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/Spotify)

### 6. Puntuación  de series y peliculas

#### ![Captura de pantalla (2375)](https://user-images.githubusercontent.com/77359338/156855814-5247e756-813b-4280-ada8-e1215f8a6f0f.png)

Utilizaremos un dataset que lo podemos encontrar un csv dentro de la siguiente carpeta. Utilizaremos la base de datos PosgreSql pero para ello necesitamos instalar sus librería que nos permitirán establecer la conexión con nuestro compilador, seguido estableceremos la relación con MongoDB para poder importar la base de datos.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/IMBD)

### 7. Videojuegos hasta la actualidad

#### ![Captura de pantalla (2378)](https://user-images.githubusercontent.com/77359338/156856094-042935cf-de9b-4491-9d15-958004c8bcd5.png)

Para ello se empleará un dataset que está ubicado en la carpeta carpetacorrespondiente del codigo, el csv contiene todos los registros de los video juegos hasta la actualidad, utilizaremos nuestra base de datos postgreSql con su debida librería en python, luego lo importaremos a nuestra base de datos MongoDB.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/Metacritic)

### 8. Población del Ecuador

#### ![Captura de pantalla (2379)](https://user-images.githubusercontent.com/77359338/156856302-49bd6957-4853-4f4a-a645-0108d66e2f3a.png)

Haremos uso de un dataset que contenga ubicación por latitud y longitud por que nos servirá más adelante. Nuevamente se hará uso de la base de datos PosgreSql la cual importara la información a MongoDB.
[codelink](https://github.com/stalin246/ProyectoFinal_AnalisisdeDatos/tree/main/Simplemaps)









