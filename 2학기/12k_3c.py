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

    # size = [2441, 2312, 1031, 1233]
    # label = ['a', 'b', 'ab', 'o']
    # color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
    # plt.axis('equal')
    #
    # # explode 돌출되는 정보
    # plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0, 0, 0.05, 0))
    # plt.legend()
    # plt.show()


    male = 0
    female = 0
    # name = input('인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력해주세요 :')
    name = '신도림동'
    with open('gender.csv') as f:
        data = csv.reader(f)

        for row in data:
            if (name) in row[0]:
                for i in row[3:104]:
                    male += int(i)
                for i in row[106:]:
                    female += int(i)

    print(male, female)

    plt.rc('font', family='Malgun Gothic')
    plt.axis('equal')
    plt.pie([male, female],
            labels=['남성', '여성'],
            autopct='%.1f%%',
            colors=['royalblue', 'deeppink'],
            startangle=90)      # 시작 각도, 0 의 위치는 3시 방향. 90의 값은 12시 방향
    plt.title(name + ' 지역의 남녀 성별 인구 분포')
    plt.legend()
    plt.savefig(name + ' 지역의 남녀 성별 인구 분포' + '.png')     # 이미지 파일로 저장.
    plt.show()