import pandas as pd

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/Titanic.csv")

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

#Only the numerical data
df = df.select_dtypes(include='number')
print(df)

#Import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,accuracy_score,confusion_matrix,classification_report

X = df[['PassengerId','Pclass','Age','SibSp','Parch','Fare']]
y = df['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 42, test_size = 0.2)
svc = SVC()
svc.fit(X_train,y_train)
y_pred = svc.predict(X_test)

print("Accuracy:",accuracy_score(y_pred,y_test))
print("Confusion matrix:",confusion_matrix(y_pred,y_test))
print("r2 score:",r2_score(y_pred,y_test))
print("Classification report:",classification_report(y_pred,y_test))