# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:44:50 2022

@author: LENOVO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:/Users/LENOVO/Desktop/1ders_odevi/ogrenci_bilgileri.csv')

nunot = df.iloc[:,1:3].values

sehır = df.iloc[:,0:1].values

cinsiyet = df.iloc[:,-1].values

le = preprocessing.LabelEncoder()

ohe = preprocessing.OneHotEncoder()

sehır = ohe.fit_transform(sehır).toarray()

cinsiyet[:,-1] = le.fit_transform(cinsiyet[:,-1])

sehırdf = pd.DataFrame(data = sehır, index = range(11), columns = ['antalya','istanbul', 'izmir'])

cinsiyetdf = pd.DataFrame(data = cinsiyet, index = range(11), columns = ['cinsiyet'])

nunotdf = pd.DataFrame(data = nunot, index = range(11),columns=['numara', 'not'])

sehırnunotdf = pd.concat([sehırdf, nunotdf], axis=1)

df2 = pd.concat([sehırnunotdf, cinsiyetdf], axis=1)

x_train, x_test, y_train, y_test = train_test_split(sehırnunotdf, cinsiyetdf, test_size = 0.33, random_state = 0)

lr = LinearRegression()

lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)


ogrencı_not = nunotdf.iloc[:,2:3]

sag = nunotdf.iloc[:,:3]

sol = nunotdf.iloc[:,4:]


bagdeg = pd.concat([sag,sol],axis = 1)

x_train, x_test , y_train, y_test = train_test_split (bagdeg, ogrencı_not, test_size = 0.33, random_state = 0)

lr.fit(x_train, y_train)
y_pred=lr.predict(x_test)


plt.scatter(bagdeg[['numara']].values, ogrencı_not.values, color = 'green')

plt.plot(x_test[['numara']].values, y_pred, color = 'yellow')

plt.show