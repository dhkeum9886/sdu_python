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


# def fx(x: pd.DataFrame) -> pd.DataFrame:
def fx(x):
    return x.max() - x.min()


def fx2(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
    #
    # print(obj)
    # print(obj.rank())   # default method = 'average'
    # print(obj.rank(method='min'))
    # print(obj.rank(method='max'))
    # print(obj.rank(method='first'))
    # print(obj.rank(method='dense'))

    # 순위의 동률을 처리하는 method 옵션 값 지정
    # ‘average’ 같은 값을 가지는 항목들의 순위 평균값을 순위로 삼는다.(default 설정)
    # ‘min’ 같은 값을 가지는 그룹내 가장 낮은 순위(가장 작은 수의 순위)를 부여한다.
    # ‘max’ 같은 값을 가지는 그룹내 가장 높은 순위(가장 큰 수의 순위))를 부여한다.
    # ‘first’ 같은 값을 가지는 그룹내 먼저 나타나는 순서따라 순위를 매긴다.
    # ‘dense’ method =‘min’과 같은 방법으로 순위를 부여하나, 'min' 과는 다르게 그룹 간 순위가 '1' 씩 증가한다.

    df = pd.DataFrame({'name': ['kim', 'lee', 'park', 'choi', 'jung', 'gang', 'nam'],
                       'score': [70, 95, 100, 95, 70, 90, 70]})

    df['rank_by_average'] = df['score'].rank(method='average', ascending=False)
    df['rank_by_min'] = df['score'].rank(method='min', ascending=False)
    df['rank_by_max'] = df['score'].rank(method='max', ascending=False)
    df['rank_by_first'] = df['score'].rank(method='first', ascending=False)
    df['rank_by_dense'] = df['score'].rank(method='dense', ascending=False)
    print(df)

    frame = pd.DataFrame({'b':[4.3,7,-3,2],
                          'a':[0,1,0,1],
                          'c':[-2,5,8,-2.5]})
    print(frame)
    print(frame.rank())
    print(frame.rank(axis=0))
    print(frame.rank(axis=1))
    print(frame.rank(axis='columns'))

    # sort, values/index , by

    # obj = pd.Series(range(4), index=list('dabc'))
    # print(obj.sort_index())
    # print('')
    # obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
    # print(obj.sort_values())    # 값에 의한 정렬. NaN 은 마지막에 위치함.

    # frame = pd.DataFrame({'b': [4, 7, 7, 7],
    #                       'a': [0, 1, 0, 1],
    #                       'c': [9, 4, 3, 6]
    #                       })
    # print(frame)
    # print('')
    # print(frame.sort_values(by=['a', 'b']))
    # print(frame.sort_values(by=['b', 'a']))

    # frame = pd.DataFrame(np.arange(8).reshape(2,4) , index=['three', 'one'],
    #                      columns=list('dabc'))
    # print(frame)
    # print('')
    # print(frame.sort_index())
    # print('')
    # print(frame.sort_index(axis=1))
    # print('')
    # print(frame.sort_index(axis=1, ascending=False))

    # apply, applymap

    # frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
    #                      index=['utah', 'ohio', 'texas', 'oregon'])
    #
    # print(frame)
    # print(np.abs(frame))  # 벡터화기능이 지원됨.
    #
    # # apply : 브로드캐스팅 연산 , 핸/열 단위로 연산
    #
    # # 아래와 동일.
    # f = lambda x: x.max() - x.min()  # = fx(x) = x.max() - x.min()
    # print(frame.apply(f))  # = f(frame)
    #
    # # print(frame.apply(f, axis='columns'))
    # # print(frame.apply(f, axis=0))   # axis=0 행들간
    # # print(frame.apply(f, axis=1))   # axis=1 열들간
    #
    # # print(fx(frame))  # 동일 방법
    # # print(frame.apply(fx))  # 동일 방법
    # # print(frame.apply(fx2))
    #
    # # applymap : 벡터화 연산 / 각 요소별 연산
    #
    # format = lambda x: '%.2f' % x
    # print(frame.applymap(format))
    #
    # print(frame['e'].map(format))   # map Series 객체만 대상으로 동작
