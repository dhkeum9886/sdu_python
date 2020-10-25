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

    df = pd.DataFrame([[1.4, np.nan],
                       [7.1, -4.5],
                       [np.nan, np.nan],
                       [0.75, -1.3]],
                      index=['a', 'b', 'c', 'd'],
                      columns=['one', 'two']
                      )
    print(df)
    # print(df.sum())
    # print(df.sum(axis=1))
    print(df.mean(axis=1))                  # 평균
    print(df.mean(axis=1, skipna=False))
    print(df.idxmax())
    print(df.idxmin())
    print(df.cumsum())
    print(df.describe())

    obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
    print(obj)
    print(obj.describe())

    # 요약 통계 관련 메서드
    # 메서드        설명
    # count  NA  값을  제외한  값의  수를  반환한다.
    # describe  Series나  DataFrame의  각  컬럼에  대한  요약  통계를  계산한다.
    # min, max  최소값과  최대값을  계산한다.
    # argmin, argmax  각각  최소값과  최대값을  담고  있는  색인의  위치(정수)  를  반환한다.
    # idxmain, idxmax  각각  최소값과  최대값을  담고  있는  색인의  값을  반환한다.
    # quantile  0  부터  1  까지의  분위수를  계산한다.
    # sum  합을  계산한다.
    # mean  평균을  계산한다.
    # median  중갑값(50 % 분위의  값)을  반환한다.
    # mad  평균값에서  평균절대  편차를  계산한다.
    # prod  모든  값의  곱  var  표본분산의  값을  계산한다.
    # std  표본표준편차의  값을  계산한다.
    # skew  표본비대칭도(3  차  적률)의  값을  계산한다.
    # kurt  표본첨도(4  차  적률)의  값을  계산한다.
    # cumsum  누적합을  계산한다.
    # cumin, cummax  각각  누적  최소값과  누적  최대값을  계산한다.
    # cumprod  누적곱을  계산한다.
    # diff  1  차  산출차를  계산한다.
    # pct_change  퍼센트  변화율을  계산한다.

    
    # obj = pd.Series(range(5), index=list('aabbc'))
    # print(obj)
    # print(obj.index.is_unique)
    # print(obj['a'])
    # print(obj['c'])

    # df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
    # print(df)
    # print(df.loc['b'])
