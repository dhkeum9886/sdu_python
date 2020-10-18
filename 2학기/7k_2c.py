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
import logging

if __name__ == '__main__':
    print('file :', __file__)
    # TODO
    #
    # obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    # print(obj)
    #
    # # print(obj['a'])
    # # print(obj[0])
    #
    # # print(obj[0:2])
    # # print(obj[obj < 1.5])
    #
    # print(obj[1:2])
    # print(obj['b':'c']) # 0:2 방식과 달리 시작점과 끝점이 모두 포함됨.
    #                     # 틀리기 쉬운 부분
    #
    # obj['b':'c'] = 5
    # print(obj)


    data = pd.DataFrame(np.arange(16).reshape(4, 4),
                        index=['ohio', 'colorado', 'utah', 'newyork'],
                        columns=['one', 'two', 'three', 'four'])
    print(data)
    # print(data['two'])
    # print(data[['two', 'three']])

    # 색인의 문자로 지정되면 색인의 value, 숫자로 지정되면 색인의 where
    # print(data['two'])  #   밸류는 열을 기준으로
    # print(data[1:2])    #   where는 행을 기준으로
    #
    # print(data[data > 5])           # 값이 5 보다 큰것.
    # print(data[data['three'] > 5])  # 'three' 컬럼의 값이 5 보다 큰것.

    # loc [ row , col ]
    # print(data.loc['colorado', ['two', 'three']]  )
    # print(data.iloc[2, [3,0,1]])

    # print(data.iloc[[0,1] , [3,0,1] ])
    # print(data.loc[ :'utah', 'two'])

    # print(data.iloc[:, :3])
    # print(data.iloc[:, :3][data.three > 5])

    ser = pd.Series(np.arange(3.))
    print(ser)
    print('')
    print(ser[:1])
    print('')
    print(ser.loc[:1])  # 라벨색인  # 끝부분 포함
    print('')
    print(ser.iloc[:1]) # 정수색인  # 끝부분 포함하지 않음.


    # ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
    # print(ser2)
    # print(ser2[-1])

# DataFrame의 값 선택하기
# df[val] DataFrame에서 하나의 컬럼 또는 여러 컬럼을 선택한다.
# df.loc[val] DataFrame에서 라벨값으로 로우의 부분집합을 선택한다.
# df.loc[:, val] DataFrame에서 라벨값으로 컬럼의 부분집합을 선택한다.
# df.loc[val1, val2] DataFrame에서 라벨값으로 로우와 컬럼의 부분집합을 선택한다.
# df.iloc[where] DataFrame에서 정수 색인으로 로우의 부분집합을 선택한다.
# df.iloc[:, where] DataFrame에서 정수 색인으로 컬럼의 부분집합을 선택한다.
# df.iloc[where_i, where_j] DataFrame에서 정수 색인으로 로우와 컬럼의 부분집합을 선택한다.
# df.at[label_i, Label_j] 로우와 컬럼의 라벨로 단일 값을 선택한다.
# df.at[i, j] 로우와 컬럼의 정수색인으로 단일 값을 선택한다.
# reindex 메서드 하나 이상의 축을 새로운 색인으로 맞춘다.
# get_value, set_value 메서드 로우와 컬럼 이름으로 DataFrame의 값을 선택한다.

