'''Usaremos un conjunto de datos arbitrario de Kaggle solo 
para entender lo que se esta realizando en este repositorio
We will use an arbitrary Kaggle dataset only
to understand what is being done in this repository'''
#Importamos librerias
import pandas as pd
'''Ponemos el nombre de como llamar el documento que abriremos con pd.read_csv,
después ponemos una coma e index_col= después la columna
entre comillas del csv del cual queremos fijar el doumento, es decir a partir
de esa columna concentrarnos de esa a la derecha'''
drinks=pd.read_csv('drinks.csv',index_col='country')
'''Usamos print, para imprimir algún valor, en este caso el documento'''
print(drinks)
#Como quitar valores que tienen NaN
drinks_filtrado=drinks.dropna()
'''Sustituir los valores NaN por el valor que tu quieras, por 
ejemplo 2'''
drinks_filtrado=drinks.fillna(2)
'''Ver las columnas en las que se separa el csv'''
print(drinks.keys())
drinks_filtrado=drinks.fillna({'beer_servings':0})
'''También se puede para varias columnas'''
drinks_filtrado=drinks.fillna({'beer_servings':0,'spirit_servings':2})
'''Como extraer una columna'''
drinks['beer_servings']
'''Como extraer varias columnas'''
drinks[['beer_servings','spirit_servings']]
'''Ver un renglón, por ejemplo el primer renglón
donde indican que se ve en cada columna'''
drinks.iloc[0]
'''Ver un conjunto de renglones a través de un rango'''
drinks.iloc[0:50]
'''Ver renglones por id'''
drinks.iloc[[0,3,5,49]]
'''Filtrado de renglones por identificador'''
drinks.loc[['Yemen', 'Uganda']]
'''Filtrado por condiciones'''
drinks[drinks['beer_servings']>3]
