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
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # # 막대 그래프
    # result = []
    # # name = input('인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력해주세요 :')
    # name = '신도림동'
    # with open('age.csv') as f:
    #     data = csv.reader(f)
    #
    #     for row in data:
    #         # print(row)
    #         if (name) in row[0]:
    #             # print(row)
    #             for i in row[3:]:
    #                 # print(i)
    #                 # result.append(int(i))
    #                 result.append(int(i.replace(',', '')))
    #
    # print(result)
    # plt.figure(figsize=(7,4))
    # # plt.bar(range(101), result) # 수직막대 그래프
    # plt.barh(range(101), result)    # 수평 막대 그래프
    # plt.show()

    # 항아리 그래프
    male = []
    female = []
    # name = input('인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력해주세요 :')
    name = '신도림동'
    with open('gender.csv') as f:
        data = csv.reader(f)

        # 이런 방법도 있고.
        # for row in data:
        #     if (name) in row[0]:
        #         for i in range(0, 101):
        #             male.append(-int(row[i+3]))           # 남성의 나이를 - 로 변환
        #             female.append(int(row[-(i+1)]))
        # female.reverse()

        for row in data:
            if (name) in row[0]:
                for i in row[3:104]:
                    male.append(-int(i))  # 남성의 나이를 - 로 변환
                for i in row[106:]:
                    female.append(int(i))
    print(male[0], male[100])
    print(female[0], female[100])

    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5), dpi=300)
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(name + ' 지역의 남녀 성별 인구 분포')
    plt.barh(range(101), male, color='royalblue', label='남성')
    plt.barh(range(101), female, color='deeppink', label='여성')
    plt.legend()
    plt.show()
