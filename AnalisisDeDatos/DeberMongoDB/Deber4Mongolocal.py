from pymongo import MongoClient
import numpy as np
import random
nombres = ['Luis', 'Kevin', 'Marco', 'Juan', 'Matias', 'Jose', 'Bryan', 'Pedro', 'Marcelo', 'Alex']
apellidos = ['Caza', 'Bravo', 'Vera', 'Flores', 'Vargas', 'Cruz', 'Ramos', 'Mendez', 'Caiza', 'Acosta']
dburl = MongoClient('mongodb://localhost', 27017)
database = dburl['Usuarios'] #Creacion de la base de datos
users= database.users #users es el nombre de la coleccion
a =int(input('Ingrese el numero de ciudadanos:'))
for z in range(a):
    m = chr(random.randint(ord('a'), ord('z')))
    for i in range(9):
        m = m + chr(random.randint(ord('a'), ord('z')))
    l = {'id': z, 'Nombre1': random.choice(nombres), 'Nombre2': random.choice(nombres), 'Apellido1': random.choice(apellidos), 'Apellido2': random.choice(apellidos),'Edad': random.randint(18, 80), 'Cedula': m}
    id = users.insert_one(l).inserted_id #Forma de ingresar los datos
    print(l) #nos permite saber los elementos que estan en la base de datos


