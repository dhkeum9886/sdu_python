# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv, qr
from random import normalvariate
import time

if __name__ == '__main__':
    print('file :', __file__)
    # TODO
    N = 1000000

    # 시드값
    np.random.seed(1234)                    # 시드값 전역 지정
    rng = np.random.RandomState(1234)       # 격리된 난수 시드값 지정정
    print(rng)



    # 정규 분포로 난수 생성
    # N = 1000000
    # start = time.time()
    # samples = [normalvariate(0,1) for _ in range(N)]    # pytho native
    # # print(samples)
    # print(time.time() - start)  # 시간 측정
    #
    # start = time.time()
    # sample = np.random.normal(size=N)                   # pytho native
    # # print(samples)
    # print(time.time() - start)  # 시간 측정



    # 정규 분포로 난수 생성
    # sample = np.random.normal(size=(100,100))   # np 정규분포로 난수 생성
    # print(sample)
    #
    # plt.title("np.random.normal(size=(100,100))")
    # plt.imshow(sample, cmap = plt.cm.gray)
    # plt.colorbar()
    # plt.show()


# 난수 생성
# seed  난수 생성기의  시드를  지정한다.
# permutation  순서를  임의로  바꾸거나  임의의  순열을  반환한다.
# shuffle  리스트나  배열의  순서를  뒤섞는다.
# rand  균등분포에서  표본을  추출한다.
# randint  주어진  최소 / 최대  범위 안에서  임의의  난수를  추출한다.
# randn  표준편차가  1 이고  평균값이  0 인  정규분포에서  표본을  추출한다.
# binomial  이항분포에서  표본을  추출한다.
# normal  정규분포(가우시안  분포)에서  표본을  추출한다.
# beta  베타분포에서  표본을  추출한다.
# chisquare  카이제곱분포에서  표본을  추출한다.
# gamma  감마분포에서  표본을  추출한다.
# uniform  균등[0, 1)분포에서  표본을  추출한다.










    # # save
    # arr = np.arange(10)
    # print(arr)
    # np.save('./numpy_binary', arr)
    #
    # # load
    # arr = np.load('./numpy_binary.npy') # ext .npy
    # print(arr)


    # # 압축 save
    # arr = np.arange(10)
    # np.savez('./numpy_binary', a=arr, b=arr)
    #
    # # 압축 load
    # arch = np.load('./numpy_binary.npz') # ext .npz
    # print(arch['a'])    # 키값 지정
    # print(arch['b'])    # 키값 지정


    # # 압축 save # 압축이 잘되는 형식
    # arr = np.arange(10)
    # np.savez_compressed('./numpy_binary', a=arr, b=arr) # 압축이 잘되는 형식에 더 효육적
    #
    # # 압축 load   # 로드는 동일
    # arch = np.load('./numpy_binary.npz') # ext .npz
    # print(arch['a'])    # 키값 지정
    # print(arch['b'])    # 키값 지정



    # x = abs(np.random.randn(6)) * 10
    # y = abs(np.random.randn(6)) * 10
    # x = np.sort(x).reshape(2, 3)
    # y = np.sort(y).reshape(3, 2)
    # x = np.ceil(x)
    # y = np.ceil(y)
    #
    # print(x)
    # print(y)
    #
    # print(x.dot(y))     #배열 곱 결과는 동일
    # print(np.dot(x, y)) #배열 곱
    # print(x @ y)        #배열 곱

    # X = np.random.randn(5, 5) * 10
    # X = np.ceil(X)
    # print(X)
    # print(X.T)          # 전치행렬
    #
    # mat = X.T.dot(X)    # 전치행렬을 곱한
    # print(mat)
    #
    # Inv = inv(mat)      # 역행렬
    # print(Inv)
    # print(mat.dot(inv(mat)))
    #
    # q, r = qr(mat)      # qr 분해
    # print(q)
    # print(r)

# 선형대수
# diag 정사각 행렬의 대각/비대각 원소를 1차원 배열로 반환하거나, 1차원 배열을
# 대각선 원소로 하고 나머지는 0으로 채운 단위행렬을 반환한다.
# dot 행렬 곱셈
# trace 행렬의 대각선 원소의 합을 구한다.
# det 행렬식을 계산한다.
# eig 정사각 행렬의 고유값과 고유벡터를 계산한다.
# inv 정사각 행렬의 역행렬을 계산한다.
# pinv 정사각 행렬의 무어-펜로즈 유사역원 역행렬을 구한다.
# qr QR 분해를 계산한다.
# svd 특이값 분해(SVD)를 계산한다.
# solve A가 정사각 행렬일 때 Ax = b를 만족하는 x를 구한다.
# lstsq Ax = b를 만족하는 최소제곱해를 구한다.