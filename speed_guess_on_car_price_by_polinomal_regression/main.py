import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('dataset/polynominal-regression.csv')


fiyat=data["araba_fiyat"].values.reshape(-1,1)#x
hiz=data["araba_max_hiz"].values.reshape(-1,1) #y
''''''
#algorithm
import sklearn.linear_model as lm
from sklearn.preprocessing import PolynomialFeatures
reg=lm.LinearRegression()
polynominal_reg=PolynomialFeatures(degree=4)

x_polynominal=polynominal_reg.fit_transform(fiyat,hiz)

#fit
reg.fit(x_polynominal, hiz)

#predict
y_predict=reg.predict(x_polynominal)

from sklearn.metrics import r2_score
score=r2_score(hiz, y_predict)
print("score: ",score)

x_polynominal_predict=polynominal_reg.fit_transform([[1500]], hiz)
y_predict=reg.predict(x_polynominal_predict)
print(y_predict)

'''
#graph
plt.plot(fiyat, y_predict, color="b", label="poly")
plt.legend()
plt.scatter(fiyat,hiz, color="r")
plt.xlabel("Araç fiyatları")
plt.ylabel("Araç Hızları")
plt.show()
'''