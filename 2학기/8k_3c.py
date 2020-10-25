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
import pandas_datareader.data as web

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    obj = pd.Series([7,-5,-7,4,6,6,0])
    print(obj.rank(method='average'))

    # obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    # print(obj)
    # unique = obj.unique()
    # print(unique)           # 유니크 값만 추림
    # print(obj.value_counts())   # 값의 출현 횟수 카운트
    # # print(obj.value_counts(sort=False))  # 값의 출현 횟수 카운트
    # mask = obj.isin(['b', 'c'])
    # print(mask)
    # print(obj[mask])

    # to_match = pd.Series(['c', 'a', 'b', 'c', 'a'])
    # unique_vals = pd.Series(['c', 'b', 'a'])
    # print(pd.Index(unique_vals).get_indexer(to_match))

    # 유일값, 값 세기, 멤버십 메서드
    # sin Series의 각 원소가 넘겨받은 연속된 값에 속하는지를 나타태는 블리언 배열을 반환한다.
    # match 각 값에 대해 유일한 값을 담고 있는 배열에서의 정수 색인 계산한다.
    # unique Series에서 중복된 값을 제거하고 유일값만 포함하는 배열을 반환한다.
    # 결과는 Series에서 발견된 순서대로 반환한다.
    # value_counts Series에서 유일값에 대한 색인과 도수를 계산한다.
    # 도수는 내림차순으로 정렬 된다


    # data = pd.DataFrame({'qu1': [1,3,4,3,4],
    #                      'qu2': [2,3,1,2,3],
    #                      'qu3': [1,5,2,4,4]})
    # print(data)
    #
    # # print(data.apply(pd.value_counts))
    # print(data.apply(pd.value_counts).fillna(0))    # Nan 을 0 으로 채움.

    

    # 상관관계, 공분산

    # all_data = {ticker: web.get_data_yahoo(ticker)
    #             for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG', 'TSLA', 'AMZN']}
    #
    # price = pd.DataFrame({ticker :  data['Adj Close']
    #                       for ticker, data in all_data.items()})
    #
    # volume = pd.DataFrame({ticker: data['Volume']
    #                       for ticker, data in all_data.items()})
    #
    # # print(all_data)
    # # print(price.head())
    # # print(volume.head())
    #
    # returns = price.pct_change()
    # print(returns.tail())
    # # print(returns['MSFT'].corr(returns['IBM']))
    # # print(returns['MSFT'].corr(returns.IBM))
    # # print(returns['MSFT'].cov(returns['IBM']))
    #
    # print(returns.corr())   # 상관관계
    # print(returns.cov())    # 공분산
    #
    # print(returns.corrwith(returns.IBM))    # 모든 항목의 IBM 에 대한 상관관계
    # print(returns.corrwith(volume))         # 거래량에 따른 상관관계
