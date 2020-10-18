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

    # s1 = pd.Series([7.3, -2.5, 3.4, 1.5] , index = ['a', 'c', 'd', 'e'])
    # s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'd', 'e', 'f', 'g'])
    # print(s1)
    # print(s2)
    # print(s1+s2)    # 공통적으로 가지고 있는 라벨은 계산된 결과값이출력
    #                 # 공통적으로 가지고 있지 않는 라벨은 NaN
    # print (s1.add(s2, fill_value=0))

    # df1 = pd.DataFrame(np.arange(9.).reshape(3,3), columns=list('bcd'), index=['ohio', 'texas', 'colorado'])
    # df2 = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])
    # print(df1)
    # print(df2)
    # print(df1+df2)

    # df1 = pd.DataFrame({'a': [1, 2]})
    # df2 = pd.DataFrame({'b': [3, 4]})
    # print(df1)
    # print(df2)
    # print(df1-df2)
    # print(df1.add(df2, fill_value=0))

    # df1 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
    # df2 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
    # print(df1)
    # df2.loc[1, 'b'] = np.nan
    # print(df2)
    # print('')
    # print(df1+df2)
    # print('')
    # print(df1.add(df2, fill_value=0))   # Nan 을 0 으로 채워서 계산 하기로 함.

    # df1 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
    # df2 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
    # print(df1)
    # print(1/df1)
    # print(df1.rdiv(1))  # df1.div 의 역 계산, 짝궁 메모드

    # df1 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
    # df2 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
    # df3 = df1.reindex(columns=df2.columns, fill_value=-1)
    # print(df3)

    # arr = np.arange(12.).reshape(3,4)
    # print(arr)
    # print(arr[0])
    # print(arr-arr[0])   # 행 단위로 반복 연산이 이루어짐.

    frame = pd.DataFrame(np.arange(12.).reshape(4,3),
                         columns=list('bde'),
                         index=['utah', 'ohio', 'texas', 'oregon']
                         )
    print(frame)
    # series = frame.iloc[0]
    # print(frame)
    # print(series)
    # print(frame-series)

    # series2 = pd.Series(range(3), index=list('bef'))
    # print(series2)
    # print(frame+series2)

    series3 = frame['d']
    print(series3)
    frame2 = frame.sub(series3, axis='index')
    print(frame2)

# 산술 연산 메서드
# add, radd 덧셈(+)을 위한 메서드
# sub, rsub 뺄셈(-)을 위한 메서드
# div, rdiv 나눗셈(/)을 위한 메서드
# floordiv, rfloordiv 소수점 내림(//) 연산을 위한 메서드
# mul, rmul 곱셈(*)을 위한 메서드
# pow, rpow 멱승(**)을 위한 메서드