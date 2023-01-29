import pandas as pd
import numpy as py

#seri oluşturun

#seri=pd.Series([1,2,3,4,5])
#seri2=pd.Series(["a","b","c"])
#liste=[1,2,3,4,5]
#seri3=pd.Series(liste)
#print(type(seri3))


#oluşturduğun serinin bilgisini göster

#seri=pd.Series([1,2,3,4,5])
#print(seri.axes)

#oluşturduğun serinin veri tipini yazdır

#seri=pd.Series([1,2,3,4,5])
#print(seri.dtype)

#oluşturduğun serinin boyutunu yazdır

#seri=pd.Series([1,2,3,4,5])
#print(seri.ndim)

#seride kaç eleman olduğunu yazdır

#seri=pd.Series([1,2,3,4,5])
#print(seri.shape)

#serinin değerlerini yazdır

#seri=pd.Series([1,2,3,4,5])
#print(seri.values)

#serinin baştan 5 ve sondan 5 değerini yazdır

#seri=pd.Series([1,2,3,4,5,6,7])
#print(seri.head(),"\n")
#print(seri.tail(),"\n")

#serinin 2.indisi yazdır

#seri=pd.Series([10,11,12,13,14])
#print(seri[2])

#serinin indexlerini değiştir.

#seri=pd.Series([10,11,12,13,14,15],index=(0,2,4,6,8,10))
#print(seri[8])
#print(seri.loc[8])
#print(seri.iloc[4])


#oluşturulan seriyi  2. indisten 10. indise kadar yazır

#seri=pd.Series([10,11,12,13,14,15],index=(0,2,4,6,8,10))
#print(seri.loc[2:10])

#serinin dataframe ini oluştur

#frame=pd.DataFrame([10,11,12,13,14,15], columns=["baslik"])
#print(frame)
#print(frame.shape)
#print(frame.ndim)

#numpy ile 3 dizi oluşturup pandas ile dataframe şeklinde göster

seri1=py.random.randint(10,size=6)
seri2=py.random.randint(10,size=6)
seri3=py.random.randint(10,size=6)

data=pd.DataFrame({"s1":seri1, "s2":seri2, "s3":seri3})
print(data)

#oluşturuduğun serinin 3. kolonunu sil

print(data.drop("s3",axis=1))