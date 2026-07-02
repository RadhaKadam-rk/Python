import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/housing.csv")

#Preprocessing
print(df.head())
print(df.tail())
print(df.isnull())
df = df.dropna()
print(df)
print(df.describe())
print(df.info())
print(df.size)
print(df.shape)

#Pie Chart
data = df['bedrooms']
colors = sns.color_palette('viridis')
plt.pie(data,labels =data.index,colors=colors,autopct='%0.1f%%',startangle=0.25)
plt.title("Bedrooms")
plt.show()