# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # data = np.random.randn(2,3)  # 2행 3열 의 2차원 배열
    # print(data)
    # print('\r\ndata * ', data * 10)
    # print('\r\ndata + ', data * data)
    # print('\r\ndata shape', data.shape)
    # print('\r\ndata dtype', data.dtype)
    #
    # data1 = [6, 7.5, 8, 9, 1]
    # arr1 = np.array(data1)
    #
    # print(arr1)
    # print(type(arr1))
    # print('\r\ndata shape', arr1.shape)
    # print('\r\ndata dtype', arr1.dtype)
    #
    # data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    # arr2 = np.array(data2)
    # print(arr2)
    # print(type(arr2))
    # print('\r\ndata dim', arr2.ndim)  # 데이터의 차원수
    # print('\r\ndata shape', arr2.shape)  # 데이터의 각 차원의 크기 확인
    # print('\r\ndata dtype', arr2.dtype)  # 데이터 타입
    #
    # np_arr2 = np.empty((3, 6), dtype=np.float64)  # 초기화되지 않은 배열 생성
    # print(np_arr2)
    # np_arr1 = np.zeros((3, 6), dtype=np.float64)  # 0 으로 초기화된 배열 생성
    # print(np_arr1)
    # np_arr3 = np.ones((3, 6), dtype=np.float64)  # 1 으로 초기화된 배열 생성
    # print(np_arr3)
    #
    # arr = np.random.randn(2, 3)
    # print(arr.dtype)
    # print(arr)
    # arr = arr.astype(np.int32)  # 형변환
    # print(arr.dtype)
    # print(arr)
    # arr = arr.astype(np.string_)  # 형변환
    # print(arr.dtype)
    # print(arr)
    # arr = arr.astype(np.dtype('u4'))  # 형변환
    # print(arr.dtype)
    # print(arr)
    # arr = arr.astype(np.dtype('S'))  # 형변환
    # print(arr.dtype)
    # print(arr)

    int_array = np.arange(10)
    print(int_array)
    print(int_array.dtype)

    calibers = np.array(np.random.randn(10).astype('f'))
    print(calibers)
    print(calibers.dtype)

    int_array = int_array.astype(calibers.dtype)
    print(int_array)
    print(int_array.dtype)
