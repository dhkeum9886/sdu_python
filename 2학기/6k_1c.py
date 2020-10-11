# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv, qr
from random import normalvariate
import time

if __name__ == '__main__':
    print('file :', __file__)
    # TODO


    # # 판다스 자료 생성
    obj = pd.Series([4,7,-5,3])
    obj.index = ['bob', 'steve', 'jeff', 'ryan']
    print (obj)
    print (obj.values)
    print (obj.index)


    # # 인덱스 별도 지정 가능
    # obj2 = pd.Series([4,7,-5,3], index=['a', 'b', 'c', 'd'])
    # # print (obj)
    # print(obj2['a'])
    # print(obj2 > 0)
    # print(obj2[obj2 > 0])
    # print(obj2 * 2)
    #
    # print(np.exp(obj2))  # 지수
    # print('b' in obj2)

    # # 시리즈
    # sdata = {"ohio" : 3500,"texax" : 71000,"oregon" : 16000,"utah" : 5000}
    # obj3 = pd.Series(sdata)
    # # print(obj3)
    #
    # states = ['caliponia', 'ohio', 'oregon', 'texax']
    # obj4 = pd.Series(sdata, index=states)
    # obj4.name = 'population'
    # obj4.index.name = 'state'
    # # print(obj3)
    #
    # print(obj4) # 'caliponia' 키값이 없으므로 NaN , Not a Number
    # print(pd.isnull(obj4))
    # print(obj4.isnull())
    # print(pd.notnull(obj4))
    # print(obj4.notnull())
    #
    # obj5 = obj3+obj4
    # print(obj5)



