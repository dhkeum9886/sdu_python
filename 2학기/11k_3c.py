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

    # hist 발생된 빈도
    # plt.hist([1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
    # plt.show()

    # dice = []
    # for i in range(100):
    #     dice.append(random.randint(1, 6))
    # print(dice)
    # plt.hist(dice, bins=6)
    # plt.show()


    # # 1월과 8월의 최고기온을 히스토그램으로
    # aug = []
    # jan = []
    # with open('seoul.csv') as f:
    #     data = csv.reader(f)
    #     next(data)
    #     for row in data:
    #         if row is None or 0 >= len(row) or str(row) == '':
    #             continue
    #         if 2 > len(row[0].split('-')):
    #             continue
    #
    #         year = row[0].split('-')[0]
    #         mon = row[0].split('-')[1]
    #         day = row[0].split('-')[2]
    #
    #         if int(mon) == 8:
    #             aug.append(float(row[-1]))
    #
    #         if int(mon) == 1:
    #             jan.append(float(row[-1]))
    #
    # plt.hist(aug, bins=100, color='r', label='aug')
    # plt.hist(jan, bins=100, color='b', label='jan')
    # plt.legend(loc=2)
    # plt.show()

    # # # 최고기온 데이터를 월별로 구분하여 표현
    # month = [[], [], [], [], [], [], [], [], [], [], [], []]
    # with open('seoul.csv') as f:
    #     data = csv.reader(f)
    #     next(data)
    #     for row in data:
    #         if row is None or 0 >= len(row) or str(row) == '':
    #             continue
    #         if row[0] is None or 0 >= len(row[0]) or str(row[0]) == '':
    #             continue
    #         if row[-1] is None or 0 >= len(row[-1]) or str(row[-1]) == '':
    #             continue
    #         if 2 > len(row[0].split('-')):
    #             continue
    #
    #         year = row[0].split('-')[0]
    #         mon = row[0].split('-')[1]
    #         day = row[0].split('-')[2]
    #         print(float(row[-1]))
    #
    #         month[int(mon)-1].append(float(row[-1]))
    #
    #
    # plt.figure(figsize=(12,5))
    # plt.boxplot(month)
    # plt.show()




    # 과제
    high = []
    low = []
    with open('seoul.csv') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if row is None or 0 >= len(row) or str(row) == '':
                continue
            if row[0] is None or 0 >= len(row[0]) or str(row[0]) == '':
                continue
            if row[-1] is None or 0 >= len(row[-1]) or str(row[-1]) == '':
                continue
            if 2 > len(row[0].split('-')):
                continue

            year = row[0].split('-')[0]
            mon = row[0].split('-')[1]
            day = row[0].split('-')[2]

            if int(mon) == 12 and int(day) == 25:
                high.append(float(row[-1]))
                low.append(float(row[-2]))
                print(year, mon, day, (float(row[-1])) , (float(row[-2])))

    plt.boxplot([high, low])
    plt.show()
