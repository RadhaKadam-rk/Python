import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/housing.csv")

#preprocessing
print(df.head())
print(df.tail())
print(df.isnull())
df = df.dropna()
print(df)
print(df.size)
print(df.shape)

#Scatter plot using matplotlib
plt.figure(figsize=(10,10))
plt.scatter(x='bedrooms',y='price',data=df,color='blue',edgecolor='black')
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Price vs. Bedrooms")
plt.show()

#Scatter plot using seaborn
plt.figure(figsize=(10,10))
sns.scatterplot(x='bedrooms',y='price',data=df,palette='viridis')
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Price vs. Bedrooms")
plt.show()