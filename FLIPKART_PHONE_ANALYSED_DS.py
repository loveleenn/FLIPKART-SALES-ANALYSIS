import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data= pd.read_csv('Flipkart_mobile_brands_data.csv')
print(data)
print(data.head(5))
data['Model'].fillna('No Model',inplace=True)
data['Color'].fillna('Black',inplace=True)
data['Model'].fillna('No Model',inplace=True)
data['Selling Price'].fillna(data['Selling Price'].mean(),inplace=True)
data['Original Price'].fillna(data['Original Price'].mode()[0],inplace=True)
data['Storage_numeric'] = data['Storage'].str.extract(r'(\d+)').astype(float)
mode_value = data['Storage_numeric'].mode()[0]
data['Storage_numeric'].fillna(mode_value, inplace=True)
data['Storage'] = data['Storage_numeric'].astype(int).astype(str) + 'GB'
data.drop(columns=['Storage_numeric'], inplace=True)
data['Memory_numeric'] = data['Memory'].str.extract(r'(\d+)').astype(float)
mode_value = data['Memory_numeric'].mode()[0]
data['Memory_numeric'].fillna(mode_value, inplace=True)
data['Memory'] = data['Memory_numeric'].astype(int).astype(str) + 'GB'
data.drop(columns=['Memory_numeric'], inplace=True)
print(data)
print(data.isnull().sum())
print(data.describe())

data['Rating'].plot(kind='hist', bins=20, title='Rating')
plt.gca().spines[['top', 'right',]].set_visible(False)

data['Selling Price'].plot(kind='hist', bins=20, title='Selling Price')
plt.gca().spines[['top', 'right',]].set_visible(False)

data['Brand'].groupby(data['Memory']).count().sort_values(ascending=False)

sns.pairplot(data, hue='Brand')

sns.displot(data, x='Selling Price',bins=5, hue='Brand',aspect=1.2 )

fig, ax = plt.subplots(figsize=(15,3))
ax=sns.countplot(x="Brand", data=data )

round(data.groupby('Brand')['Selling Price'].mean(),0).sort_values(ascending=False)

plt.figure(figsize=(9,7))
sns.scatterplot(data=data ,x='Rating', y='Selling Price',hue="Brand")
plt.show()
