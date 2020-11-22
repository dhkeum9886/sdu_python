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

    result = []
    name = input('인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력해주세요 :')
    with open('age.csv') as f:
        data = csv.reader(f)

        for row in data:
            # print(row)
            # if ('신도림동') in row[0]:
            if (name) in row[0]:
                # print(row)
                for i in row[3:]:
                    # print(i)
                    # result.append(int(i))
                    result.append(int(i.replace(',', '')))

    print(result)
    plt.style.use('ggplot')
    plt.rc('font', family='Malgun Gothic')  # 한글 사용위해서는 한글 폰트에 대한 패밀리 속성 지정 필요.
    plt.title(name + ' 지역의 인구 구조')
    plt.plot(result)
    plt.show()
