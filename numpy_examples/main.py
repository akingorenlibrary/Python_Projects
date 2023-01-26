import numpy as np

# (10,15,30,45,60) değerlerine sahip numpy dizisini oluşturun

#result=np.array([10,15,30,45,60])
#print("tip: ",type(result))
#print("Dizi: {}".format(result))

#---------------------------------------------------------------

# (5-15) arasındaki sayılarla numpy dizisi oluşturun.
#result=np.arange(5,15)
#print(result)

#---------------------------------------------------------------

# (50-100) arasında 5 er 5 er artarak numpy dizisi olusturun

#result=np.arange(50,100,5)
#print(result)

# 10 elemanlı sıfırlardan oluşan bir dizi oluşturun

#result=np.zeros(10)
#print(result)

#10 elemanlı birlerden oluşan bir dizi oluşturun

#result=np.ones(10)
#print(result)

# (0,100) arasında eşit aralıklı 5 sayı üretin

#result=np.linspace(0,100,5)
#print(result)

# (10-30) arasında rastgele 5 tane tamsayı üretin

#result=np.random.randint(10,30,5)
#print(result)

# [-1 ile 1] arasında 10 adet sayı üretin

#result=np.random.randn(10)
#print(result)

# (3x5) boyutlarında (10-50) arasında rastgele bir matris olusturun.

#result=np.random.randint(10,50,15).reshape(3,5)
#print(result)

# üretilen matrisin satır ve sütün sayıları toplamlarını bul

#result=np.random.randint(10,50,15).reshape(3,5)
#print(result,"\n")
#satirToplam=result.sum(axis=1)
#sutunToplam=result.sum(axis=0)
#print(satirToplam,"\n")
#print(sutunToplam,"\n")

#üretilen matrisin en büyük ve en küçük değerlerini bul

#result=np.random.randint(10,50,15).reshape(3,5)
#print(result,"\n")

#print("max: {}".format(result.max()))
#print("min: {}".format(result.min()))

#üretilen matrisin en büyük değerinin indexi kaçtır

#result=np.random.randint(10,50,15).reshape(3,5)
#print(result,"\n")

#print("max: {}, index: {}".format(result.max(),result.argmax()))
#print("min: {}, index: {}".format(result.min(), result.argmin()))

# (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını yazdırın.

#result=np.arange(10,20)
#print(result)
#print(result[0:3])

#üretilen dizinin elemanlarını tersten yazdrın.

#result=np.arange(10,20)
#print(result)
#print(result[::-1])

#üretilen matrisin ilk satırını seçin.

#result=np.random.randint(10,20,15).reshape(3,5)
#print(result,"\n")
#print(result[0],"\n")

#üretilen matrisin 2.satır 3.sutundaki elemanı hangisidir.

#result=np.random.randint(10,20,15).reshape(3,5)
#print(result,"\n")
#print(result[2,3])

#üretilen matristeki tüm satırlardaki ilk elamanı seçin.

#result=np.random.randint(10,20,15).reshape(3,5)
#print(result,"\n")
#print(result[:,0])

#üretilen matrisin her bir elemanının karesini alın.

#result=np.random.randint(10,20,15).reshape(3,5)
#print(result,"\n")
#print(result**2)

#üretilen matrisin elemanlarının hangisi çift sayıdır.

#result=np.random.randint(10,20,15).reshape(3,5)
#print(result,"\n")
#print(result%2==0)

