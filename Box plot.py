import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/housing.csv")

#Preprocessing
print(df.head())
df = df.dropna()
df = df.isnull()
print(df)
print(df.size)
print(df.shape)

df_num = df.select_dtypes(include = 'number')
print(df_num)

#Box plot
plt.figure(figsize=(10,10))
plt.boxplot(df_num)
plt.show()

#Remove outliers
def remove_outliers(df,columns):
    df_clean = df.copy()
    for col in columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR
        df_clean = df_clean[(df_clean[col]>=lower)&(df_clean[col]<upper)]
        return df_clean

cleaned_data = remove_outliers(df,df_num)
print(cleaned_data)

#Boxplot using Seaborn
sns.boxplot(data = cleaned_data)
plt.title("Age vs. Outcome")
plt.show()