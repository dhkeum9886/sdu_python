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

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    result = []
    high = []
    low = []
    with open('seoul.csv') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if row is None or 0 >= len(row) or str(row) == '':
                continue
            if 2 > len(row[0].split('-')):
                continue

            year = row[0].split('-')[0]
            mon = row[0].split('-')[1]
            day = row[0].split('-')[2]

            if int(mon) == 12 and int(day) == 25:
                high.append(float(row[-1]))
                low.append(float(row[-2]))
                print(year, mon, day)

    plt.plot(
        high, 'r', label='high'
    )
    plt.plot(
        low, 'b', label='low'
    )
    plt.figure(figsize=(12, 2))
    plt.show()

    # with open('seoul.csv') as f:
    #     lines = list(csv.reader(f))
    #     header, value = lines[0], lines[1:]
    #     # print(lines)
    #     print(value)
    #     print(header)

    # df = pd.read_csv('seoul.csv')
    # print(df)
    # plt.title('plotting2')
    # plt.plot(
    #     df['최저기온(℃)'], 'b', label='low'
    # )
    # plt.plot(
    #     df['최고기온(℃)'], 'r', label='high'
    # )
    # plt.show()
