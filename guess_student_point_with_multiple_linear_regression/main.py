import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import  LinearRegression

data=pd.read_csv("student.csv")
data=data[["G1","G2","G3","studytime","failures","absences","age"]]

data.rename(columns={"G1":"Not1",
                     "G2":"Not2",
                     "G3":"Final",
                     "studytime":"calisma_suresi",
                     "failures":"sinif_tekrari",
                     "absences":"devamsizlik",
                     "age":"yas"},inplace=True)
print(data.head(),"\n")

y=np.array(data["Final"])
x=np.array(data.drop("Final",axis=1))

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=2)

lr=LinearRegression()
lr.fit(x_train,y_train)
#print(lr.score(x_test,y_test))
#print(lr.score(x_train,y_train))
yeni_veri=np.array([[5,6,2,0,6,18]])
print(lr.predict(yeni_veri))