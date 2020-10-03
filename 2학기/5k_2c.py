# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
    # uniqarr = np.unique(names)
    # print(np.unique(names))     # 유니크값을 구함. with numpy
    # print(sorted(set(names)))   # 유니크값을 구함. with native python
                                    # set 은 중복이 제거


    values = abs(np.random.randn(10))
    # print(values)
    values = values*10
    # print(values)
    values = np.sort(values)
    # print(values)
    values = np.ceil(values)
    print(values)

    print(np.in1d(values, [2,3,4]))     # 첫번째 배열의 원소가 두번째 배열의 원소를 포함하는지 불리언 배열 반환


    # 집합 메서드
#  unique(x) 배열 x에서 중복된 원소를 제거한 뒤 정렬하여 반환한다.
# intersect1d(x, y) 배열 x와 y에 공통적으로 존재하는 원소를 정렬하여 반환한다.
# union1d(x, y) 두 배열의 합집합을 반환한다.
# in1d(x, y) x의 원소가 y의 원소에 포함되는지를 나타내는 블리언 배열을 반환한다.
# setdiff1d(x, y) 두 배열의 차집합을 반환한다.
# setxor1d(x, y) 한 배열에는 포함되지만 두 배열 모두에는 포함되지 않는 원소들의 집합인 대칭 차집합을 반환한다.



    # arr = np.random.randn(5, 4)
    # print(arr)

    # print(arr.mean())   # 전체 평균
    # print(np.mean(arr)) # 전체 평균
    #
    # print(arr.sum())    # 합
    # print(np.sum(arr))  # 합

    # print(arr.sum(axis=1))  # axis=1 컬럼에서 합
    # print(arr.sum(axis=0))  # axis=0 로우에서 합

    # arr = np.arange(0, 9, 1)
    # arr = abs(np.random.randn(9))
    # # print(arr)
    # # print(arr.cumsum())
    # arr = arr.reshape(3, 3)
    # print(arr)
    # print(arr.dtype)
    # print(arr.cumsum())
    # print(arr.cumsum(axis=1))   #컬럼
    # print(arr.cumsum(axis=0))   #로우
    # print(arr.cumprod())
    # print(arr.cumprod(axis=1))  #컬럼
    # print(arr.cumprod(axis=0))  #로우

    # arr = np.random.randn(9)
    # print(arr)
    # print((arr > 0).sum())   # 양의 원소의 갯수
    # arr = np.where(arr > 0, True, False)
    # print(arr)
    # print(arr.any())    # 하나이상의 메서드가 True 체크
    # print(arr.all())    # 모든 메서드가 True 체크


    # arr = np.random.randn(5, 3)
    # print(arr)
    #
    # arr0 = np.sort(arr, axis=0)
    # print(arr0)
    #
    # arr1 = np.sort(arr, axis=1)
    # print(arr1)

    # arr = abs(np.random.randn(100)) * 10
    # print(arr)
    # arr = np.sort(arr)
    # print(arr)
    #
    # ret = arr[int(0.05 * len(arr))] # 5% 분위수 # 정렬하면 구하는게 가능
    # print(ret)

# 수학 통계 메서드
# sum 배열 전체 혹은 특정 축에 대한 모든 원소의 합을 계산한다.
# mean 산술 평균을 구한다.
# std, var 각각 표준편차(std)와 분산(var)을 구한다.
# min, max 각각 최소값(mix)과 최대값(max)을 구한다.

####### 중요
# argmin, argmax 각각 최소값을 가지는 원소의 색인값(argmin)과 최대값을 가지는 원소의
# 색인값(argmax)을 구한다.
#######

# cumsum 각 원소의 누적합
# cumprod 각 원소의 누적곱