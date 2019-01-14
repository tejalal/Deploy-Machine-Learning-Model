import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import SVC
import pickle
 
names=['sepal-length','sepal-width','petal-length','petal-width', 'class']
iris=pd.read_csv('IRIS.csv',names=names)
#iris.head() display first 5 records
# iris.info() # display dataset info
 
# split the datset into training and testing
array=iris.values
X = array[:,0:4]
Y = array[:,4]
x_train,x_test, y_train, y_test = model_selection.train_test_split(X,Y,test_size = 0.20)
print(x_train.shape)
print(x_test.shape)
 
 
# create SVC
seed = 7
model = SVC()
kfold = model_selection.KFold(n_splits = 10, random_state = seed)
cv_results = model_selection.cross_val_score(model, x_train, y_train, cv = kfold, scoring = 'accuracy')
print(cv_results.mean())
 
# fit the model
model.fit(x_train, y_train)
predict = model.predict(x_test)
print(accuracy_score(y_test, predict))
 
# print(confusion_matrix(y_test,predict))
# print(classification_report(y_test, predict))
 
# taking user input
x = np.array([5.4,3.2,5.4,2.8])
x=x.reshape(1,4)
p=model.predict(x)
print(x)
print(p)
 
# save the model
pickle.dump(model, open('model.pk','wb'))
print("model saved")