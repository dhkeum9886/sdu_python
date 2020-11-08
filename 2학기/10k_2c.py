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

    # data = pd.DataFrame({
    #     'k1': ['one', 'two'] * 3 + ['two'],
    #     'k2': [1, 1, 2, 3, 3, 4, 4]})
    # # print(data)
    # # print(data.duplicated())        # 중복된 정보를 찾음.
    # # print(data[data.duplicated()])  # 중복된 열만 출력
    # # print(data.drop_duplicates())   # 중복된 정보를 제거.
    #
    # data['v1'] = range(7)
    # print(data)
    # print(data.drop_duplicates(['k1']))  # k1 을 기준으로 중복된 정보를 제거.
    #
    # print(data.drop_duplicates(['k1', 'k2'], keep='last'))
    # # 5,6 행
    # # 중복된 정보가 있으면 중복된 마지막 행을 남기고
    # # 중복된 정보의 먼저 나온 행을 삭제

    # meat_to_animal = {
    #     'bacon': 'pig',
    #     'pulled pork': 'pig',
    #     'pastrami': 'cow',
    #     'corned beef': 'cow',
    #     'honey ham': 'pig',
    #     'nova lox': 'salmon',
    # }
    # data = pd.DataFrame({
    #     'food': ['bacon', 'pulled pork', 'bacon',
    #              'Pastrami', 'corned beef', 'Bacon',
    #              'pastrami', 'honey ham', 'nova lox'],
    #     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
    # print(data)
    #
    # lowercased = data['food'].str.lower()
    # print(lowercased)
    # # data['animal'] = lowercased.map(meat_to_animal)
    #
    # # data['animal'] = data['food'].str.lower().map(meat_to_animal)   # 특정 딕트에 맵핑해서 입력
    # # print(data)
    #
    # data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])  # 특정 딕트에 맵핑해서 입력 # 람다식으로
    # print(data)

    # data = pd.Series([1., -999., 2., -999., -1000., 3.])
    # print(data)
    #
    # print(data.replace(-999, np.nan))
    # print(data.replace([-999, -1000], np.nan))  # 치환할 대상을 리스트 형태로.
    # print(data.replace([-999, -1000], [np.nan, 0]))  # 치환할 값도 리스트 형태로
    # print(data.replace({-999: np.nan, -1000: 0}))  # 딕트 형태로도 가능



    data = pd.DataFrame(np.arange(12).reshape(3,4),
                        index = ['ohio', 'colorado', 'new york'],
                        columns=['one', 'two', 'three', 'four']
                        )
    print(data)

    transform = lambda x: x[:4].upper()         # 인덱스 객체를 대문자로 변경.
    # print(data.index.map(transform))
    # data.index = data.index.map(transform)    # 원본 객체를 변경함.
    # print(data)

    print(data.rename(index=str.title, columns=str.upper))  # str.title 첫 글자만 대문자로. str.upper 대문자로

    print(data.rename(index={'ohio':'indiana'},             # 인덱스와 컬럼을 각 이름 변경.
                columns={'three':'peekaboo'}))


