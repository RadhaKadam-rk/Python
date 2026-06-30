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
df= df.dropna()
print(df)
print(df.describe())
print(df.info())
print(df.size)
print(df.shape)

#Histogram using matplotlib
plt.figure(figsize=(10,10))
plt.hist(x='price',y='bedrooms',data=df,color='blue',edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Bedrooms")
plt.title("Price vs. Bedrooms")
plt.show()

#Histogram using seaborn
plt.figure(figsize=(10,10))
sns.histplot(x='price',y='bedrooms',data=df,bins=5,edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Bedrooms")
plt.title("Price vs. Bedrooms")
plt.show()
