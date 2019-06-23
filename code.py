# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:38:15 2018

@author: Bikash
"""

# Importing Lib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pSat = 1936

# Importing Dataset
dataset = pd.read_csv('data.csv')
p = dataset.iloc[:, 0:1].values
v = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2:3].values
v_mod = np.array(np.zeros([9, 1]))
y_mod = np.zeros([9, 1])

# Fitting Simple Linear Regression to trainning set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(p, y)

# predecting the test set result
a = regressor.intercept_
b = regressor.coef_

for i in range(len(v)):
    v_mod[i] = (1 + (pSat - p[i])/(p[i]*(a + b*p[i])))
    y_mod[i] = a + b*p[i]
    
# Visualizing the test set
pv = plt.figure(1);
plt.scatter(p, v, color = "red")
plt.plot(p, v_mod, color = "blue")
plt.title("P vs V modified graph")
plt.xlabel("P in PSIG")
plt.ylabel("V")
pv.show()

# Visualizing the test set
py = plt.figure(2);
plt.scatter(p, y_mod, color = "red")
plt.plot(p, y_mod, color = "blue")
plt.title("P vs Y modified graph")
plt.xlabel("P in PSIG")
plt.ylabel("Y")
py.show()
