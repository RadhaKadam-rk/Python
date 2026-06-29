import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/housing.csv")
print(df.head())

#preprocessing
print(df.tail())
print(df.isnull())
print(df.describe())
print(df.info())
print(df.size)
print(df.shape)
df = df.dropna()
print(df)

#Barplot using matplotlib
plt.figure(figsize=(10,10))
x= df['price']
y=df['bedrooms']
plt.bar(x,y,data = df,color='blue',edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Bedrooms")
plt.title("Price vs. Bedrooms")
plt.show()

#Barplot using seaborn
plt.figure(figsize=(10,10))
sns.barplot(x='price',y='bedrooms',data=df,palette='viridis',edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Bedrooms")
plt.title("Price vs. Bedrooms")
plt.show()