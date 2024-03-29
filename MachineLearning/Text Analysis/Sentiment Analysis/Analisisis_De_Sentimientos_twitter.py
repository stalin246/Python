# -*- coding: utf-8 -*-
"""Analisisis de sentimientos Twitter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMxmG8-MsRSqXQ0dX_L0DuwJYdsceDcs

Importamos las librerias que necesitamos
"""

import tweepy 
from textblob import TextBlob 
from wordcloud import WordCloud
import pandas as pd
import numpy as np 
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

"""Utilizamos los tokens de la api de twitter"""

consumer_key = 'tu token'
consumer_secret = 'tu token'
acces_token = 'tu token'
acces_t_secret = 'tu token'

"""Validamos la autenticacion con twitter por medio de nuestro token"""

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
#seteamos los tokens
authenticate.set_access_token(acces_token, acces_t_secret)
#pasamos la informacion
api = tweepy.API(authenticate, wait_on_rate_limit= True)

"""Definimos el idioma e informacion reciente de 100 twets"""

hashtag = api.user_timeline(screen_name='Cuenca', lang='en', tweet_mode='extended', count=100)
#hashtag = api.search(q='#Guayaquil', lang='en', result_type='recent', count=100)

"""Utilizamos un for hasta el final de los hashtag y los mostramos de los 50"""

print('show 50 tweets')
i=1
for tweet in hashtag[:50]:
  print(str(i) + ') ' + tweet.full_text + '\n')
  i += 1

"""Creamos un dataframe con pandas bajo la columna Tweets y un id"""

df = pd.DataFrame([tweet.full_text for tweet in hashtag], columns=['Tweets'])
df.head(10)

"""Limpiamos nuestro dataframe de ciertos caracteres que no necesitaremos"""

#utilizamos una funcion para limpiar cada registro
def clean_text(text):
  text = re.sub(r'@[A-Za-z09]+', '', text)
  text = re.sub(r'#', '', text)
  text = re.sub(r'_', '', text)
  text = re.sub(r'\n', '', text)
  text = re.sub(r':', '', text)
  text = re.sub(r'RT[\s]+', '', text)
  text = re.sub(r'https?:\/\/?', '', text)
#retornamos nuestra variable
  return text
#utilizamos nuestra funcion en nuestro dataframe "df"
df['Tweets'] = df['Tweets'].apply(clean_text)
df.head(10)

"""Realizamos el analisis deacuerdo al analisis de sentimiento recordando lo siguiente:

**Polaridad** hace referencia a cómo positivo o negativo el tono de las tasas de texto de entrada de -1 a + 1, por -1 son más negativo y + 1 está más positiva. 

**Subjetividad** hace referencia a cómo subjetiva las tasas de instrucción de 0 a 1, siendo 1 el alta subjetiva.
"""

#utilizamos una funcion mediante ya el metodo de sentimiento->subjetividad
def get_subjectivity(text):
  return TextBlob(text).sentiment.subjectivity
 # return TextBlob(text).translate(from_lang='es',to='en').sentiment.subjectivity
  return TextBlob(text).sentiment.subjectivity

#utilizamos una funcion mediante ya el metodo de sentimiento->polaridad
def get_polarity(text):
   return TextBlob(text).sentiment.polarity
  #return TextBlob(text).translate(from_lang='es',to='en').sentiment.polarity

"""Definimos las columnas que tendra el dataframe segun la subjetividad y polaridad"""

df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)
df.head()

"""Utilizamos una grafica para representar las palabras mas usadas"""

all_words = ' '.join( [twts for twts in df['Tweets']])
#Establecemos el modelo que tendra la grafica
word_Cloud = WordCloud(width=1080, height=720, random_state=21, max_font_size=119).generate(all_words)
#Definimos el tipo de interpolacion
plt.imshow(word_Cloud, interpolation='bilinear')
plt.axis('off')
plt.show()

"""Establecemos la subjetividad y polaridad, tambien establecemos el analisis deacuerdo a las condiciones que mencionamos antes, todas ellas ubicadas ya en columnas en nuestro dataframe"""

def analysis(score):
  if score < 0:
    return 'Negative'
  # elif score == 0:
  #   return 'Neutral'
  # else:
  #   return 'Positive'
  elif score > 0:
    return 'Positive'

df['Analysis'] = df['Polarity'].apply(analysis)

df

"""Mostramos los tweets positivos siendo el 1ro el mas +"""

j=1
sortedDF = df.sort_values(by=['Polarity'])
for i in range(0, sortedDF.shape[0]):
  if(sortedDF['Analysis'][i] == 'Positive'):
    print(str(j) + ') ' + sortedDF['Tweets'][i])
    print()
    j += 1

"""Mostramos los tweets positivos siendo el 1ro el mas -"""

j=1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for i in range(0, sortedDF.shape[0]):
  if(sortedDF['Analysis'][i] == 'Negative'):
    print(str(j) + ') ' + sortedDF['Tweets'][i])
    print()
    j += 1

"""Utilizamos una grafica de analisis de la subjetividad y polaridad"""

plt.figure(figsize=(8,6))
for i in range(0, df.shape[0]):
  plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='blue')

plt.title('Analisis de sentimientos')
plt.xlabel('polarity')
plt.ylabel('subjectivity')
plt.show()

"""Sacamos un porcentaje de los positivos y negativos"""

ptweet = df[df.Analysis == 'Positive']
pteet = ptweet['Tweets']

round(ptweet.shape[0] / df.shape[0] * 100, 1)

ntweet = df[df.Analysis == 'Negative']
nteet = ntweet['Tweets']

round(ntweet.shape[0] / df.shape[0] * 100, 1)

"""Finalmente graficamos las columnas positivas y negativas"""

df['Analysis'].value_counts()

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()