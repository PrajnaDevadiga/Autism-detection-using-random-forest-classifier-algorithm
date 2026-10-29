import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
asd_data = pd.read_csv('C:\\Users\\Prajna\\Downloads\\asd_dataset.csv',index_col=0)
asd_data.head(10)
asd_data.tail()
asd_data.columns
asd_data.Class .unique()
asd_data.head()
asd_data.Sex.unique()
asd_data['Sex'].replace('m',0,inplace=True)
asd_data['Sex'].replace('f',1,inplace=True)
asd_data.Jaundice.unique()
asd_data['Jaundice'].replace('no',0,inplace=True)
asd_data['Jaundice'].replace('yes',1,inplace=True)
asd_data.Family_mem_with_ASD.unique()
asd_data['Family_mem_with_ASD'].replace('no',0,inplace=True)
asd_data['Family_mem_with_ASD'].replace('yes',1,inplace=True)
asd_data.Who_completed_the_test.unique()
asd_data['Who_completed_the_test'].replace('Health Care Professional','Health care professional',inplace=True)
asd_data.Who_completed_the_test.unique()
asd_data['Who_completed_the_test'].replace('family member',0,inplace=True)
asd_data['Who_completed_the_test'].replace('Health care professional',1,inplace=True)
asd_data['Who_completed_the_test'].replace('Self',2,inplace=True)
asd_data['Who_completed_the_test'].replace('Others',3,inplace=True)
asd_data.head(10)
asd_data.describe()
data = asd_data.groupby('Class')
df=data.describe()
df.to_excel('C:\\Users\\Prajna\\Downloads\\new1.xlsx')
asd_data.to_excel('C:\\Users\\Prajna\\Downloads\\cleandata.xlsx')
plt.figure(figsize=(15,7), dpi=100)
sns.countplot(x='Sex',hue='Class',data=asd_data, palette='Set1')
plt.figure(figsize=(15,8), dpi=100)
sns.countplot(x='Age_Mons',hue='Class',data=asd_data, palette='Set1')
plt.figure(figsize=(12,7), dpi=100)
sns.countplot(x='Family_mem_with_ASD',hue='Class',data=asd_data, palette='Set1')
from sklearn.model_selection import train_test_split
X = asd_data.drop('Class', axis=1)
y = asd_data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
X_train.head(10)
X_train.to_excel("C:\\Users\\Prajna\\Downloads\\test.xlsx",index=False)
X_test.to_excel("C:\\Users\\Prajna\\Downloads\\test.xlsx" ,index=False)
y_train.to_excel("C:\\Users\\Prajna\\Downloads\\test.xlsx",index=False)
y_test.to_excel("C:\\Users\\Prajna\\Downloads\\test.xlsx" ,index=False)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
rfc = RandomForestClassifier(n_estimators=600)
rfc = rfc.fit(X_train,y_train)
predictions_rf = rfc.predict(X_test)
acc_rf = accuracy_score(y_true=y_test, y_pred= predictions_rf)
print("Overall accuracy of ADA model using test-set is : %f" %(acc_rf*100))
print(classification_report(y_test,predictions_rf))

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
ada = AdaBoostClassifier(n_estimators=500)
ada.fit(X_train, y_train)
prediction_ada = ada.predict(X_test)
acc_ada = accuracy_score(y_true=y_test, y_pred= prediction_ada)
print("Overall accuracy of ADA model using test-set is : %f" %(acc_ada*100))
print(classification_report(y_test,prediction_ada))
print(confusion_matrix(y_test,prediction_ada))

from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
model_svm = SVC()
model_svm.fit(X_train, y_train)
predictions_svm = model_svm.predict(X_test)
acc_svm = accuracy_score(y_true=y_test, y_pred= predictions_svm)
print("Overall accuracy of SVM model using test-set is : %f" %(acc_svm*100))
print(classification_report(y_test,predictions_svm))

print(confusion_matrix(y_test,predictions_svm))

li_x = ['Rf', 'Ada', 'SVM']
li_y = [acc_rf, acc_ada,acc_svm]

print(li_y)
sns.barplot(x=li_x, y=li_y)

l=[[0,1,0,1,0,1,1,1,0,0,15,0,1,1,1]]
predict = rfc.predict(l)
print(predict)
