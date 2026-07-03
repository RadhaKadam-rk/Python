import pandas as pd

#Dataset
df = pd.read_csv("C:/Users/kadan/Desktop/Dataset/diabetes.csv")

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

#Import scikit
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,r2_score,accuracy_score,precision_score,classification_report
from sklearn.neighbors import KNeighborsClassifier

X = df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Pedigree','Age']]
y = df['Outcome']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=50,test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
confusion = confusion_matrix(y_pred,y_test)
r2 = r2_score(y_pred,y_test)
precision = precision_score(y_pred,y_test)
report = classification_report(y_pred,y_test)

print("Accuracy:",accuracy)
print("confusion matrix:",confusion)
print("R2 score:",r2)
print("Precision:",precision)
print("Classification report:",report)