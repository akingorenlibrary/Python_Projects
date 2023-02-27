import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('dataset/multiple-regression-dataset.csv')

deneyimveyas=data.loc[:, ['deneyim','yas'] ].values
#deneyim=data["deneyim"].values.reshape(-1,1)
maas=data["maas"].values.reshape(-1,1) #y

#algorithm
import sklearn.linear_model as lm
reg=lm.LinearRegression()

#data split
import sklearn.model_selection as ms
x_train, x_test, y_train, y_test=ms.train_test_split(deneyimveyas, maas, test_size=1/3, random_state=0)

#train
reg.fit(x_train, y_train)

#predict
y_predict=reg.predict(x_test)
print("deneyimler: ",x_test)
print("tahminler: ",y_predict)


#score
import sklearn.metrics as mt
score=mt.r2_score(y_test, y_predict)
score=score*100
scoreString=score.__str__().split(".")[0]
print("Doğruluk yüzdesi: %{}".format(scoreString))

'''
#graph
plt.scatter(deneyimveyas[:,1], maas, color="r")
plt.scatter(x_test[:,1], y_predict, color="b")
plt.show()
'''


def maasTahminEt(deneyim, yas_giris):
    return reg.predict([[deneyim,yas_giris]])


deneyim_giris = input("Deneyim Giriniz: ")
yas_giris = input("Yaş Giriniz: ")
maas_tahmini = maasTahminEt(int(deneyim_giris),int(yas_giris))
print("Verilmesi gereken maaş: ", maas_tahmini)


#print("tahmin: ",reg.predict([[5,22]]))
