# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#kütüphane kurma işlemi
import numpy as np
import pandas as pd
import matplotlib as mp


#data yükleme işlemi
veriler = pd.read_csv('veriler.csv')
print(veriler)


#veri ön işleme işlemleri

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)


class insan:
    boy = 150
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(20))


#liste oluşturma işlemi
l = [1, 2, 3] 



#eksik veri ön işleme işlemi

veriler2 = pd.read_csv('eksikveriler.csv')
print(veriler2)

'''eksik verileri temizlemek için birçok yöntem bulunuyor. öncelikle eksik olan verimiz nominal mi , sayısal mı buna bakıyoruz.
sayısal verilerde bazen kolonun ortalaması alınarak eksik veri düzeltilebilir. bazen eksik veriler komple data setten silenebilir. '''


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values= np.nan , strategy='mean') #ortalama alma yöntemi

yas =veriler2.iloc[:,1:4].values
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])

print(yas)


#Kategorik veriler (veri dönüşümü)
#öncelikle veri setimizde hem nominal(kategorik) hem numeric(sayı) veriler bulunmakta.
#ulke kolonunu cinsiyet kolonuna göre farklı dönüştürmemiz gereklidir. 

ulke=veriler.iloc[:,0:1].values
print(ulke)


#sayısal degere ceviriyoruz
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

ulke[:,0]= le.fit_transform(veriler.iloc[:,0])
print(ulke)

#matris formatına ceviriyoruz

ohe= preprocessing.OneHotEncoder()
ulke= ohe.fit_transform(ulke).toarray()
print(ulke)


#Verilerin dönüştürülmüş hallerinin birleştirilmesi

print(list(range(22)))
sonuc=pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2=pd.DataFrame(data=yas, index=range(22), columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3=pd.DataFrame(data=cinsiyet, index=range(22), columns=['cinsiyet'])
print(sonuc3)

s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

#eğitim ve test 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s,sonuc3, test_size=0.33, random_state = 0)

#ölçekleme
#değişkenlerin içideki datayı birbirine sayıca yaklaştırıyoruz

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train= sc.fit_transform(x_train)
X_test= sc.fit_transform(x_test)

































 
