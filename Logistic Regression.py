import pandas as pd

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/Titanic.csv")

#Preprocessing
print(df)
print(df.isnull())
df = df.dropna()
print(df.head())
print(df.size)
print(df.shape)
print(df.describe())
print(df.info())
df = df.select_dtypes(include='number')
print(df.tail())

#Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,classification_report

X = df[['Pclass','Age','SibSp','Parch','Fare']]
y = df['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_pred,y_test))
print("Confusion Matrix:",confusion_matrix(y_pred,y_test))
print("Precision score:",precision_score(y_pred,y_test))
print("Classification Report:",classification_report(y_pred,y_test))