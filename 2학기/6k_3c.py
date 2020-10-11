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

    data = {'year' : [2000, 2001],
            'pop' : [3.6, 1.5]}
    frame = pd.DataFrame(data)
    print(frame.T)

    # obj = pd.Series(range(3), index=['a', 'b', 'c'])
    # index = obj.index
    # print(index)
    #
    # try:    # 인덱스는 변경이 불가능
    #     index[1] = 'd'
    # except Exception as e:
    #     # logging.exception(e)
    #     print(e)
    # finally:
    #     print(index)
    #     print("인덱스는 변경이 불가능합니다")
    #
    # labels = pd.Index(np.arange(3))
    # print(labels)
    #
    # obj2 = pd.Series([1.5, -2.5, 0], index=labels)
    # print(obj2)
    # print(obj2.index is labels)
    #
    #
    # pop = {'ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
    #         'nevada': {2001: 2.4, 2002: 2.9}}
    # frame3 = pd.DataFrame(pop)
    # print(frame3)
    # print(frame3.columns)
    # print('ohio' in frame3.columns)
    # print(2003 in frame3.index)

    # 판다스의 인덱스는 중복이 가능....왜 그랬엉
    # dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
    # print(dup_labels)

# # 색인 객체
# append 추가적인 색인 객체를 덧붙여 새로운 색인을 반환한다.
# difference 색인의 차집합을 반환한다.
# intersection 색인의 교집합을 반환한다.
# union 색인의 합집합을 반환한다.
# isin 색인이 넘겨받은 색인에 존재하는지 알려주는 블리언 배열을 반환한다.
# delete i 위치의 색인이 삭제된 새로운 색인을 반환한다.
# drop 넘겨받은 값이 삭제된 새로운 색인을 반환한다.
# insert i 위치의 색인이 추가된 색인을 반환한다.
# is_monotonic 색인 단조성을 가진다면 True를 반환한다.
# is_unique 중복되는 색인이 없다면 True를 반환한다.
# unique 색인에서 중복되는 요소를 제거하고 유일한 값만 반환한다.



