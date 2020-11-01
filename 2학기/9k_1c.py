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

    # df = pd.read_csv('./examples/ex1.csv');
    # print(df);

    # df = pd.read_csv('./examples/ex1.csv', sep=',');
    # print(df);

    # df = pd.read_csv('./examples/ex2.csv', header = None);
    # print(df);

    # df = pd.read_csv('./examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message']);
    # print(df);
    #
    # df = pd.read_csv('./examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col='message');
    # print(df);
    #
    # df = pd.read_csv('./examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message']);
    # print(df);

    # df = pd.read_table('./examples/ex2.csv', sep=',', names=['a', 'b', 'c', 'd', 'message'], index_col='message');
    # print(df);

    # df = pd.read_csv('./examples/csv_mindex.csv', index_col=['key1', 'key2']);
    # print(df)

    # lst = list(open('examples/ex3.txt'))
    # print(lst)
    # df = pd.read_table('examples/ex3.txt', sep='\s+') # 중요 # 텍스트파일에서 백슬래시 파싱
    # print(df)

    # df = pd.read_table('examples/ex4.csv', skiprows=[0, 2, 3])
    # print(df)

    df = pd.read_csv('examples/ex5.csv')
    print(df)
    print(pd.isnull(df))

    df = pd.read_csv('examples/ex5.csv', na_values=['NULL'])
    print(df)

    df = pd.read_csv('examples/ex5.csv', na_values=[1, 5, 9])
    print(df)

    sentinels = {'message': ['foo', 'NA'],
                 'something': ['two']}
    df = pd.read_csv('examples/ex5.csv', na_values=sentinels)
    print(df)


# # pandas 파일 파싱 함수
#
# read_csv 파일, URL 또는 파일과 유사한 객체로부터 구분된 데이터를 읽어 온다.
# 데이터 구분자는 쉼표(,)를 기본으로 한다.
# read_table 파일, URL 또는 파일과 유사한 객체로부터 구분된 데이터를 읽어 온다.
# 데이터 구분자는 탭('\t')을 기본으로 한다.
# read_fwf 고정폭 컬럼 형식에서 데이터를 읽어 온다 (구분자가 없는 데이터).
# read_clipboard 클립보드에 있는 데이터를 읽어 온다.
# read_excel 엑셀 파일에서 표 형식의 데이터를 읽어 온다.
# read_hdf pandas에서 저장한 HDF5 파일에서 데이터를 읽어 온다.
# read_html HTML 문서 내의 모든 테이블의 데이터를 읽어 온다.
# read_json JSON 문자열에서 데이터를 읽어 온다.
# read_sql SQL 쿼리 결과를 pandas의 DataFrame 형식으로 읽어 온다

# # read_csv와 read_table 함수 인자
#
# path 파일 시스템에서의 위치, URL, 파일 객체를 나타내는 문자열
# sep 또는 delimiter 필드를 구분하기 위해 사용할 연속된 문자나 정규 표현식
# header 컬럼 이름으로 사용할 로우 번호, 기본값은 0이며, 헤더가 없을 경우에는
# None으로 지정할 수 있다.
# index_col 색인으로 사용할 컬럼 번호나 이름, 계층적 색인을 지정할 경우 리스트를 넘
# 길 수 있다.
# names 컬럼 이름으로 사용할 리스트. header=None과 함께 사용한다.
# skiprows 파일의 시작부터 무시할 행의 수 또는 무시할 로우 번호가 담긴 리스트
# na_values NA 값으로 처리할 값들의 목록
# comment 주석으로 분류되어 파싱하지 않을 문자 혹은 문자열
# thousands 숫자를 천 단위로 끊을 때 사용할 ',' 나 '.' 같은 구분자
