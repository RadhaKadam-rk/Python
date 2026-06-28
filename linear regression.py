import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/uber.csv")
print(df.head())

#Preprocessing
print(df.isnull())
df = df.dropna()
print(df)
print(df.size)
print(df.shape)
print(df.info())
print(df.describe())

#Outlier
df_num = df.select_dtypes(include = 'number')
print(df_num)
plt.boxplot(df_num)
plt.show()

def remove_outlier(df,columns):
    df_clean = df.copy()
    for col in columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        Q2 = Q3-Q1
        lower = Q1 - 1.5*Q2
        upper = Q3 + 1.5*Q2
        df_clean = df_clean[(df_clean[col]>=lower)&(df_clean[col]<upper)]
        return df_clean

clean_data = [ 'Unnamed: 0','fare_amount','pickup_longitude','pickup_latitude','dropoff_latitude','passenger_count']
cleaned_data = remove_outlier(df,clean_data)
print(cleaned_data.head())

sns.boxplot(data = 'clean_data')
plt.show()

#Co-relation
relation_fare_pickup_lon = df['fare_amount'].corr(df['pickup_longitude'])
print(relation_fare_pickup_lon)

df = df.select_dtypes(include = 'number')
corr_matrix = df.corr(method = 'pearson')
print(corr_matrix)

#Linear regression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count']]
y = df['fare_amount']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
mse = mean_squared_error(y_test,y_predict)
rmse = np.sqrt(mse)
print(rmse)
print(r2_score(y_test,y_predict))

#Boxplot
sns.boxplot(data = y_predict)
plt.show()