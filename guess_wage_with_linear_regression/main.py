import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#plt.plot([1,2,3,4,5],[1,4,9,16,25])
#plt.xlabel("Sayılar")
#plt.ylabel("Sayıların Kareleri")
#plt.show()

data=pd.read_csv("yenimaas.csv")
x=data.iloc[:,0].values.reshape(-1,1)
y=data.iloc[:,1].values.reshape(-1,1)
print(y)

#plt.scatter(x,y)
#plt.xlabel("Tecrübe")
#plt.ylabel("Maaş")
#plt.show()

xtrain, xtest, ytrain, ytest=train_test_split(x,y,test_size=0.3,random_state=28)
lr=LinearRegression()
lr.fit(xtrain, ytrain)
yhead=lr.predict(xtest)
print(lr.predict([[1.3]]))