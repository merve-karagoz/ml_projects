# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:04:55 2022

@author: LENOVO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing as pr
from sklearn.model_selection import train_test_split as trs
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_csv('C:/Users/LENOVO/Desktop/çoklu-gerieleme-ödevi/employee_revenue_lastyear.csv')

df2 = df.apply(pr.LabelEncoder().fit_transform)

name = df2.iloc[:,:1]
name2 = pr.OneHotEncoder().fit_transform(name).toarray()

namedf = pd.DataFrame(data = name2, index = range(11), columns = ['Omer','Arnold','Aidan', 'Sue', 'Ben', 'Rose', 'Lucy', 'Ellen','Karen', 'Jamaall','Omer'])
finaldata = pd.concat([namedf, name2.iloc[:,1:3]], axis = 1)
finaldata2 = pd.concat([finaldata.iloc[:,:3], df.iloc[:,1:3]], axis = 1)

finaldata3 = pd.concat([finaldata2, df2.iloc[:,-2]],axis=1)
Y= df2.iloc[:,-1]

x_train, x_test, y_train, y_test = trs(finaldata3, Y, test_size = 0.33, random_state = 0)
lr = LinearRegression()
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

X = np.append(arr = np.ones((14,1)).astype(int), values = finaldata3, axis = 1)
X_l = finaldata3.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(Y,X_l).fit()
print(r_ols.summary())


X_l2 = finaldata3.iloc[:,[0,1,2,4,5]].values
r_ols2 = sm.OLS(Y,X_l2).fit()
print(r_ols2.summary())

x_train, x_test, y_train, y_test = trs(finaldata3.iloc[:,[0,1,2,4,5]], Y, test_size = 0.33, random_state = 0)
lr = LinearRegression()
lr.fit(x_train, y_train)

y_pred2 = lr.predict(x_test)
