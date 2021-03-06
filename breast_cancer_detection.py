

import numpy as np
import sklearn.datasets
import pandas as pd
import matplotlib.pyplot as plt

data = sklearn.datasets.load_breast_cancer()

data.data[125,:]

data

print(dir(data))

data.target_names

data.data

data.target



X = data.data

Y = data.target

X.shape

Y.shape

data_set = pd.DataFrame(data.data,columns = data.feature_names)

data_set

data_set["class"] = data.target

data_set.head()

X_axis = data.data[:,0]
Y_axis = data.data[:,1]

plt.scatter(X_axis,Y_axis, c = data.target)
plt.show()

print(data_set["class"].value_counts())

print(data.target_names)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print(X_train.shape)
print(y_train.shape)

print(X_test.shape)
print(y_test.shape)

print(Y.mean(), y_train.mean(), y_test.mean())

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42,stratify = Y )

print(Y.mean(), y_train.mean(), y_test.mean())

from sklearn.linear_model import LogisticRegression

LR_classifier = LogisticRegression()

LR_classifier.fit(X_train,y_train)

from sklearn.svm import SVC

svm_classifier = SVC(kernel='rbf', random_state= 1)
svm_classifier.fit(X_train,y_train)

from sklearn.model_selection import cross_val_score

LR_cross_val = cross_val_score(LR_classifier, X,Y,cv = 5 )

print(LR_cross_val)

print(LR_cross_val.mean())##Logistic Regression

Svm_cross_val = cross_val_score(svm_classifier, X,Y,cv = 5 )

print(Svm_cross_val)

print(Svm_cross_val.mean())##rbf

svm_classifier = SVC(kernel='sigmoid', random_state= 1)
svm_classifier.fit(X_train,y_train)

Svm_cross_val = cross_val_score(svm_classifier, X,Y,cv = 5 )

print(Svm_cross_val)

print(Svm_cross_val.mean())##sigmoid

svm_classifier = SVC(kernel='linear', random_state= 1)
svm_classifier.fit(X_train,y_train)

Svm_cross_val = cross_val_score(svm_classifier, X,Y,cv = 5 )

print(Svm_cross_val)

print(Svm_cross_val.mean())##linear

svm_classifier = SVC(kernel='poly', random_state= 1)
svm_classifier.fit(X_train,y_train)

Svm_cross_val = cross_val_score(svm_classifier, X,Y,cv = 5 )

print(Svm_cross_val)

print(Svm_cross_val.mean())##poly









from sklearn.metrics import accuracy_score

prediction_on_test_data = LR_classifier.predict(X_test)

accuracy_on_test_data = accuracy_score(y_test,prediction_on_test_data)

print("Accuracy on test data =", accuracy_on_test_data * 100, "%")





input_data = (1.385e+01, 1.721e+01, 8.844e+01, 5.887e+02, 8.785e-02, 6.136e-02,
       1.420e-02, 1.141e-02, 1.614e-01, 5.890e-02, 2.185e-01, 8.561e-01,
       1.495e+00, 1.791e+01, 4.599e-03, 9.169e-03, 9.127e-03, 4.814e-03,
       1.247e-02, 1.708e-03, 1.549e+01, 2.358e+01, 1.003e+02, 7.259e+02,
       1.157e-01, 1.350e-01, 8.115e-02, 5.104e-02, 2.364e-01, 7.182e-02)

input_data_array = np.asarray(input_data)

type(input_data_array)

input_data_array

input_data_array_reshaped = input_data_array.reshape(1,-1)

input_data_array_reshaped

data.target_names

prediction = LR_classifier.predict(input_data_array_reshaped)

if(prediction[0] == 0):
    print("'Malignant")
else:
    print("Benign")
