# IA_noSupervisado
## Algoritmo modificado en Python utilizando Jupyter Lab
Este codigo analiza informacion obtenida de varios pacientes con estudios sobre cancer.

## Content
Explicación creada para exlpicar el uso y en que se puede aplicar los algoritmos no supervisados.

## How to clone
Instalar Python preferiblemente el que viene integrado en [Anaconda](https://www.anaconda.com/products/distribution)
* Abrir Jupyter Notebook 
* Abrir el cuaderno de Jupyter
* Instalar librerias requeridas.



## Installation
Para instalar las librerías ejecute este Código
```bash
pip install pandas
```
```bash
pip install -U scikit-learn
```
## Preview
Importación de librerias 

```bash
import pandas as pd
from sklearn.tree import DecisionTreeClassifier,  export_graphviz 
from sklearn.tree import plot_tree
import pydotplus 

```
Carga de datos, conversión a DataFrame

```bash
dfPred = pd.read_csv('./nombreDataset.csv')

```
Limpieza del DataFrame
```bash

dfPred.isnull().any()
dfPred.isnull().sum()

```
Creación de argumentos para el entrenamiento

```bash
features = dfPred.drop(columns = "Biopsy") 

features.info()

```
Entrenamiento de modelo 
```bash
modelPred = DecisionTreeClassifier()
modelPred.fit(X = features, y = target)

```
Creación de imagen del árbol

```bash
arbol = export_graphviz(modelPred, out_file = True , filled=True, rounded=True, feature_names=features.columns)

features.info()

```
Visualización del entrenamiento
```bash
graph = pydotplus.graph_from_dot_data(arbol)
image = graph.create_png()
graph.write_png("imagen.png")
Image(filename="imagen.png")
```
Árbol de decisión

![arbol](https://user-images.githubusercontent.com/75056800/174831469-b267c81c-777a-4165-a7ac-2a3ed7fc3bfd.png)

### Notes
If you want to learn all about markdown i recommend you visit the site [markdown.es](https://markdown.es/sintaxis-markdown/)

