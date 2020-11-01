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
import sys
import csv

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # pd.options.display.max_rows = 10
    # df = pd.read_csv('examples/ex6.csv')
    # print(df)
    #
    # df = pd.read_csv('examples/ex6.csv', nrows=5)
    # print(df)

    # # 파일을 나눠서  읽기
    # chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
    # print(chunker)
    # tot = pd.Series([])
    # for piece in chunker:
    #     tot = tot.add(piece['key'].value_counts(), fill_value=0)
    #                         #  'key' 나오는 빈도를 체크
    # tot = tot.sort_values(ascending=False)
    # print(tot[:10])

    # data = pd.read_csv('examples/ex5.csv')
    # # print(data)
    # # data.to_csv('examples/ex5_out.csv', sep='|')
    # # data.to_csv(sys.stdout, sep='|')                # 화면에 바로 출력
    #
    # data.to_csv(sys.stdout, na_rep='NULL')
    # data.to_csv(sys.stdout, na_rep='NULL', index=False, header=False)
    # data.to_csv(sys.stdout, na_rep='NULL', index=False, header=False, columns=['a'])

    # dates = pd.date_range('1/1/2020', periods=7)
    # print(dates)
    #
    # ts = pd.Series(np.arange(7), index=dates)
    # print(ts)
    #
    # ts.to_csv('examples/date_series_out.csv', header=False)

    f = open('examples/ex7.csv')
    reader = csv.reader(f)
    for line in reader:
        print(line)

    with open('examples/ex7.csv') as f:
        lines = list(csv.reader(f))
        header, value = lines[0], lines[1:]
        print(lines)
        print(header)
        print(value)

        data_dict = {h: v for h, v in zip(header, zip(*value))}
        print(data_dict)

#  # CSV 관련 옵션
# delimiter 필드를 구분하기 위한 문자로 된 구분자. 기본값은 ','
# lineterninator 파일을 저장할 때 사용할 개행 문자. 기본값은 '\n\n'. 파일을 읽을 때는 이 값을
# 무시하며 자동으로 플랫폼별 개행 문자를 인식한다.
# quotechar 각 필드에서 값을 둘러싸고 있는 문자. 기본 값은 '"'
# quoting 값을 읽거나 쓸 때 둘러쌀 문자 컨벤션.
# csv.QUOTE_ALL (모든 필드에 적용). csv.QUOTE_MINIMAL (구분자 같은
# 특별한 문자가 포함된 필드만 적용). csv.QUOTE_NONE (값을 둘러싸지 않음)
# skipinitialspace 구분자 뒤에 있는 공백 문자를 무시할지 여부. 기본값은 False
# doublequote 값을 둘러싸는 문자가 필드 내에 존재할 경우 처리 여부. True일 경우 그 문자
# 까지 모두 둘러싼다.
# escapechar quotin이 csv.QUOTE_NONE일 때 값에 구분자와 같은 문자가 있을 경우
# 구별할 수 있도록 해주는 이스케이프 문자('\' 같은). 기본값은 None