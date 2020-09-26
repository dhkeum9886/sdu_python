# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # arr = np.array([ [1,2,3,4] , [5,6,7,8]])
    #
    # print('벡터화1', arr)        # 벡터화, for 루트 없이 데이터를 일괄 처리.
    # print('벡터화2', arr * arr)  # 벡터화, for 루트 없이 데이터를 일괄 처리.
    # print('벡터화3', arr + arr)  # 벡터화, for 루트 없이 데이터를 일괄 처리.
    # print('벡터화4', arr - arr)  # 벡터화, for 루트 없이 데이터를 일괄 처리.
    #
    # print('벡터화5', 1/ arr)  # 벡터화, for 루트 없이 데이터를 일괄 처리.
    #
    # print('벡터화6', arr ** 0.5)  # 벡터화, for 루트 없이 데이터를 일괄 처리.

    # arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    # arr2 = np.array([[9, 0, 1, 2], [3, 4, 5, 6]])
    # arr3 = arr1 > arr2
    # arr4 = np.array(arr1 > arr2).astype(np.uint32)
    # arr5 = np.array(arr1 > arr2).astype(np.string_)
    # print(arr3)
    # print(arr4)
    # print(arr5)

    arr1d = np.arange(27)       # 0~ 26 으로 채워진 1차원 배열
    print(arr1d)

    arr3d = arr1d.reshape((3,3,3))  # 3차월 배열로 변환


    # print(arr3d)
    # arr_temp = arr3d[0].copy()  # 0번 면의 깊은 복사 temp
    # print(arr_temp)
    # arr3d[0] = 0        # 0번 면을 0 으로 채움.
    # print(arr3d)
    # arr3d[0] = arr_temp # 0번 면에 복사본을 다시 채움.
    # print(arr3d)

    # print (arr3d[:2])
    print(arr3d[:, 1:2, 1:2])
