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

    # # 선모양
    # plt.title('plotting2')
    # plt.plot(
    #     [10, 20, 30, 40], color='skyblue', label='asc', linestyle='--'
    # )
    #
    # plt.plot(
    #     # [40, 30, 20, 10], color='pink', label='desc'
    #     # [40, 30, 20, 10], 'pink', label='desc'
    #     [40, 30, 20, 10], 'r', label='desc', linestyle='dotted'
    # )
    # plt.legend()
    # plt.show()


    # # 그래프 마커
    # plt.title('plotting2')
    # plt.plot(
    #     [10, 20, 30, 40], 'r*'
    # )
    #
    # plt.plot(
    #     [40, 30, 20, 10], 'g^'
    # )
    # plt.legend()
    # plt.show()

    # 그래프 마커, 선 모양 동시
    plt.title('plotting2')
    plt.plot(
        [10, 20, 30, 40], 'r', marker='.', label='circle up'
    )

    plt.plot(
        [40, 30, 20, 10], 'g^--', label='triangle down'
    )
    plt.legend(loc=9)
    plt.show()
