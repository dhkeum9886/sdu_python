# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

# from numpy import nan as NP
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

    # ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    # bins = [18, 25, 35, 60, 100]
    #
    # cats = pd.cut(ages, bins)       # 카테고리컬 객체로 반환
    # print(cats)
    # print(cats.codes)               # 각 몇번 카테고리에 속해있는지 출력
    # print(cats.categories)          # 각 카테고리의 정보를 출력
    # print(pd.value_counts(cats))    # 각 요소가 그룹별로 몇개의 요소를 가지고 있는지 출력
    #
    # group_name=['youth', 'youngadult', 'middleage', 'senior']
    # # cats2 = pd.cut(ages, [18, 26, 36, 61, 100], right=False) # right=false 오른쪽에 나오는 값은 포함이 안되게
    # cats2 = pd.cut(ages, bins, labels=group_name) # right=false 오른쪽에 나오는 값은 포함이 안되게

    # data = np.random.rand(20)
    # cats = pd.cut(data, 4, precision=2) # 4개의 그룹으로 나누겠다. 소수점 2자리 기준.
    # print(cats)
    # print(cats.categories)

    data = np.random.randn(1000)

    cats = pd.qcut(data, 4)             # 표본 변위치를 기반으로 데이터를 나눔
    print(cats)
    print(cats.codes)
    print(cats.categories)
    print(pd.value_counts(cats))

    cats2 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.0])  # 변위치를 직접 지정할수 있음.
    print(cats2)
    print(cats2.codes)
    print(cats2.categories)
    print(pd.value_counts(cats2))


