#Import Libraries-Importar Librerías 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import scipy
#Data Preprocessing-Procesamiento de Datos
df=pd.read_csv('Amazon_Best_Seller_2021_June.csv',index_col="Category")
df_filtrado=df.fillna(0)
print(df.keys())
print(df['Product Link'])
df.nunique()
df.shape
df.describe()
df.isnull().sum()
df = df.drop(['Product Link'], axis=1)
df['Reviews Count'] = df['Reviews Count'].replace(',','', regex=True)
df['Price'] = df['Price'].str.replace('$','', regex=True)
df['Rank'] = df['Rank'].str.replace('#','', regex=True)
df['No of Sellers'] = df['No of Sellers'].str.replace(' Sellers','', regex=True)
df['No of Sellers'] = df['No of Sellers'].astype(int)
df['Rank'] = df['Rank'].astype(float)
df['Reviews Count'] = df['Reviews Count'].astype(int)
df['Price'] = df['Price'].astype(float)
#Data Visualizations-Visualización de datos
#Univariate Analysis-Análisis Invariado
df['Rating'].value_counts()
sns.histplot(df['Rating'])
df['Rating'].value_counts().plot.pie()
plt.show()
#Bivariate Analysis-Análisis bivariado
sns.boxplot(x=df['Rating'])
#As expected, the higher ratings are more frequent in the dataset, though 4.9 and 5.0 is less frequent than expected but this is most likely due to the scarcity of these ratings
df['No of Sellers'].value_counts()
sns.histplot(df['No of Sellers'])
df['No of Sellers'].value_counts().plot.pie()
plt.show()
df['Price'].value_counts()
sns.histplot(df['Price'])
df['Price'].value_counts().plot.pie()
plt.show()
sns.pairplot(data=df)
#We are going to analyze the relation of each data point to price and rating
sns.boxplot(x=df['Rating'], y=df['Price'])
df.groupby('Rank')['Price'].describe()
sns.boxplot(x=df['Reviews Count'], y=df['Rating'])
df.groupby('Category')['Rating'].describe()
sns.boxplot(x=df['Price'], y=df['Rating'])
df.groupby('Price')['No of Sellers'].describe()
sns.boxplot(x=df['No of Sellers'], y=df['Rating'])
df.groupby('Rating')['No of Sellers'].describe()