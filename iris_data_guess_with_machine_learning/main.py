#iris datasetini çekelim
from sklearn.datasets import load_iris
iris_dataset=load_iris()
#print(iris_dataset)

#veriyi ikiye bölelim
from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest=train_test_split(iris_dataset["data"], iris_dataset["target"], test_size=0.4)
#print(xTrain.shape)
#print(xTest.shape)

#uygun modeli seçme
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)

#öğrenme
knn.fit(xTrain, yTrain)

#tahmin
xNew=[[3.5, 2.1, 3.4, 1.2]]
guess=knn.predict(xNew)
print("Guess: {}".format(guess))

#doğruluk ve test verisi
import numpy as np
verify=knn.predict(xTest)
verify=np.mean( (verify==yTest)*100)
print("Verify: {}".format(verify))