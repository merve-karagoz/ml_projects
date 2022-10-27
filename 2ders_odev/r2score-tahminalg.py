# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:42:12 2022

@author: LENOVO
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

data = pd.read_csv('C:/Users/LENOVO/Desktop/1ders_odevi/ogrenci_bilgileri.csv')

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
X = x.values
Y = y.values


# linear
lr = LinearRegression()
lr.fit(X,Y)
y_pred_lr = lr.predict(X)

# F(x)=ax+b

# polinom
poly_reg = preprocessing.PolynomialFeatures()
x_poly=poly_reg.fit_transform(X)

# F(x)=ax^2+bx1^2


lr2 = LinearRegression()
lr2.fit(x_poly,Y)
Y_pred_poly=lr2.predict(x_poly)

# StandardScale

sc = preprocessing.StandardScaler()
X_olc=sc.fit_transform(X)

y_train_olc=sc.fit_transform(Y)

# svr 

svr_reg = SVR(kernel='rbf')
svr_reg.fit(X_olc,y_train_olc)
y_pred_svr = svr_reg.predict(X_olc)

#karar ağacı

dtr = DecisionTreeRegressor(random_state = 0)
dtr.fit(X,Y)
y_pred_dt = dtr.predict(X)

#random forest

rf_reg = RandomForestRegressor(random_state = 0, n_estimators = 15)
rf_reg.fit(X,Y.ravel())
y_pred_rf=rf_reg.predict(X)

print("random forest r^2 score")
print(r2_score(Y, y_pred_rf))

print("karar ağacı r^2 score")
print(r2_score(Y,y_pred_dt))

print("SVR r^2 score")
print(r2_score(y_train_olc,y_pred_svr))

print("polinom r^2 score")
print(r2_score(Y,Y_pred_poly))

print("linear r^2 score")
print(r2_score(Y,y_pred_lr))