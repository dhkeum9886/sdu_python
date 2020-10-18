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
    # obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    # print(obj)
    #
    # new_obj = obj.drop('d')
    # print(new_obj)
    #
    # new_obj2 = obj.drop(['c', 'd'])
    # print(new_obj2)

    data = pd.DataFrame(np.arange(16).reshape(4, 4),
                        index=['ohio', 'colorado', 'utah', 'newyork'],
                        columns=['one', 'two', 'three', 'four'])
    print(data)

    data2 = data.drop(['colorado', 'ohio'])
    print(data2)

    data3 = data.drop(columns=['one', 'three'])  # equls =  data3 = data.drop(['one', 'three'], axis='columns')
    print(data3)

    data4 = data.drop(index=['colorado', 'ohio'], columns=['one', 'three'])
    print(data4)

    obj = data
    print(obj)

    obj.drop('ohio', inplace=True)  # inplace 새로운 객채를 반환하지 않고, 원본 객체를 변경한다.
    # inplace default = False
    print(obj)

    # obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    # print(obj)
    #
    # # 재색인
    # obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    # print(obj2)

    # obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
    # print(obj3)
    #
    # obj4 = obj3.reindex(range(6), method='nearest')   # ffill 빈값은 이전 값으로 채워넣음.
    # # method = None ,  pad / ffill , backfill , nearest
    # print(obj4)

    # frame = pd.DataFrame(np.arange(9).reshape(3,3),
    #                      index=['a', 'b', 'c'],
    #                      columns=['ohio', 'texas', 'california'])
    # print(frame)
    #
    # frame2 = frame.reindex(['a', 'b', 'c', 'd'])
    # print(frame2)
    #
    # states = ['texas', 'utah', 'california']
    # frame2_1 = frame.reindex(columns=states)
    # print(frame2_1)

# 재색인 , reindex
# index 색인으로 사용할 새로운 순서. Index 인스턴스나 다른 순차적인 자료구조가 사
# 용 가능하다.
# method 채움 메서드. ffill은 직전 값을 채워 넣고 bfill은 다음 값을 채워 넣는다.
# fill_value 재색인 과정 중에 새롭게 나타나는 비어있는 데이터를 채우기 위한 값
# limit 전/후 보간 시에 사용할 최대 gap 크기(채워 넣을 원소의 수)
# tolerance 전/후 보간 시에 사용할 최대 gap 크기(값의 차이)
# level MultiIndex의 단계(level)에 단순 색인을 맞춘다. 그렇지 않으면 MultiIndex의
# 하위집합에 맞춘다.
# copy True인 경우 새로운 색인이 이전 색인과 동일하더라도 데이터를 복사한다. False
# 인 경우 새로운 색인이 이전 색인과 동일할 경우 복사하지 않는다.
