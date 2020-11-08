# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

from numpy import nan as NP
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv, qr
from random import normalvariate
import time
import logging
import sys
import csv
import tables
import sqlite3

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # string_data = pd.Series(['addrvark', 'artichoke', np.nan, 'avocado'])
    # print(string_data)
    # string_data[0] = None
    # # print(string_data)
    # # print(string_data.isnull())
    # print(string_data.dropna())
    # print(string_data[string_data.notnull()])

    # data = pd.DataFrame([[1., 6.5, 3.],
    #                     [1., np.nan, np.nan],
    #                     [np.nan, np.nan, np.nan],
    #                     [np.nan, 6.5, 3.]]
    #                     )
    #
    # cleaned = data.dropna()
    # print(cleaned)
    # print(data.dropna(how='all'))             # 모든 데이터가 nan 일때 dropna
    #
    # data[4] = np.nan
    # print(data)
    # print(data.dropna(axis=1, how='all'))     # 모든 데이터가 nan 일때 dropna, 축 지정

    # df = pd.DataFrame(np.random.randn(7, 3))
    # print(df)
    # df.iloc[:4, 1] = np.nan
    # df.iloc[:2, 2] = np.nan
    # print(df)
    # print(df.dropna())
    # print(df.dropna(thresh=2))          # 데이터가 2개 이상인것으로 dropna 지정
    #
    # # print(df.fillna(0))
    # # print(df.fillna({1:0.5, 2:1.5}))    # 컬럼별로 채우는 값을 지정.
    # df.fillna(0, inplace=True)              # 값을 채우고 , 원본 객체를 변경
    # print(df)


    df = pd.DataFrame(np.random.randn(6,3))
    df.iloc[2:, 1] = np.nan
    df.iloc[4:, 2] = np.nan
    print(df)

    print(df.fillna(method='ffill'))            # ffill, bfill 옵션 지정.
    print(df.fillna(method='ffill', limit=1))   # 몇개를 채울건지 지정.
    print(df.fillna(df.mean()))                 # 평균값으로 채음.


# # pandas의 NA 처리 메서드
# dropna 누락된 데이터가 있는 축(로우, 컬럼) 을 제외시킨다.
# fillna 누락된 데이터를 대신할 값을 채우거나 ‘ffill’ 이나 ‘bfill’ 같은 보간 메서드를 적용한다.
# isnull 누락되거나 NA인 값을 알려주는 블리언값이 저장된 같은 형의 객체를 반환한다.
# notnull isnull과 반대되는 메서드

# # fillna 옵션 설명
# value 비어 있는 값을 채울 스칼라값이나 사전 형식의 객체
# method 보간 방식. 기본적으로 ‘ffill’을 사용한다.
# axis 값을 채워 넣을 축. 기본값은 axis=0 이다.
# inplace 복사본을 생성하지 않고 호출한 객체를 변경한다. 기본값은 False이다.
# limit 값을 앞 혹은 뒤에서부터 몇 개까지 채울지 결정한다