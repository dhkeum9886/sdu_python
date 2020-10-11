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

    data = {
        'state': ['ohio', 'ohio', 'ohio', 'nevada', 'nevada', 'nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
    }

    # frame = pd.DataFrame(data)
    # print(frame)
    # print(frame.head()) # 처음 5개
    # print(frame.tail()) # 끝 5개
    # print(pd.DataFrame(data, columns=['year', 'state', 'pop'])) # 컬럼의 순서 임의 지정 가능

    # frame2 = pd.DataFrame(data,
    #                       columns=['year', 'state', 'pop', 'debt'],
    #                       index=['one', 'two', 'three', 'four', 'five', 'six'])
    #
    # print(frame2)
    # print(frame2.columns)
    # print(frame2.index)
    # print(frame2['state'])          # 컬럼으로 접근
    # print(frame2.state)             # 컬럼으로 접근
    # print(frame2.loc['three'])      # 인덱스 이름으로 접근
    # print(frame2.loc['three'].state)# 인덱스 이름으로 접근
    # print(frame2.iloc[1])              # 인덱스 번호로 접근
    # print(frame2.iloc[1].state)        # 인덱스 번호로 접근
    # print(frame2.iloc[1:])             # 인덱스 번호로 접근    이런것도 가능
    # print(frame2.iloc[1:].state)       # 인덱스 번호로 접근    이런것도 가능

    # frame2['debt'] = 16.5
    # print(frame2)
    # frame2['debt'] = np.arange(5.)  # 에러 / 배열의 갯수 일치 해야됨.
    # print(frame2)
    # frame2['debt'] = np.arange(6.)  # 배열의 갯수 일치 해야됨.
    # print(frame2)

    # val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    # frame2['debt'] = val
    # print(frame2)
    #
    # print(frame2.state=='ohio')
    # frame2['eastern'] = frame2.state=='ohio'
    # print(frame2)
    #
    # del frame2['eastern']
    # print(frame2)

    pop = {'nevada': {2001: 2.4, 2003: 2.9},
           'ohio': {2000: 1.5, 2001: 1.7, 2003: 3.6}}
    frame3 = pd.DataFrame(pop)
    print(frame3)
    print(frame3.T)  # 데이터 전치

    print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

# DataFrame
# 2차원 ndarray  데이터를 담고 있는 행렬, 선택적으로 행과 열의 이름을 전달할 수 있다.
# 배열, 리스트, 튜플의 사전 사전의 모든 항목은 같은 길이를 가져야 하며, 각 항목의 내용이
# DataFrame의 컬럼이 된다.
# NumPy의 구조화 배열 배열의 사전과 같은 방식으로 취급된다.
# Series의 사전 Series의 각 값이 컬럼이 된다. 명시적으로 색인을 넘겨주지 않으면 각
# Series의 색인이 하나로 합쳐져서 로우의 색인이된다.
# 사전의 사전 내부에 있는 사전이 컬럼이 된다. 키값은 'Series의 사전'과 마찬가지로
# 합쳐져서 로우의 색인이 된다.
# 사전이나 Series의 리스트 리스트의 각 항목이 DataFrame의 로우가 된다. 합쳐진 사전의 키값이나
# Series의 색인 DataFrame의 컬럼 이름이 된다.
# 리스트나 튜플의 리스트 '2차원 ndaraay'의 경우와 같은 방색으로 취급된다.
# 다른 DataFrame 색인을 따로 지정하지 않으면 DataFrame의 색인이 그대로 사용된다.
# NumPy MaskedArray '2차원 ndaraay'의 경우와 같은 방색으로 취급되지만 마스크값은 반환
# 되는 DataFrame에서 NA 값이 된다.
