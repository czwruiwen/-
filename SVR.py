#!/usr/bin/evn python
#-*- coding:utf-8 -*-
import numpy as np
import pandas as py
from scipy import sparse
from sklearn.datasets import load_boston
boston = load_boston()
x=boston.data
y=boston.target

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=33,test_size=0.25)

from sklearn.svm import SVR
linear_svr=SVR(kernel='linear')
linear_svr.fit(x_train,y_train)
linear_svr_predict=linear_svr.predict(x_test)
