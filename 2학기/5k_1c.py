# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('file :', __file__)
    # TODO


    # 단한 유니버셜 함수
    # arr = np.arange(10)
    # print(arr)
    # print(np.sqrt(arr))     # 제곱근
    # print(np.exp(arr))      # 지수


    # 이항 유니버셜 함수
    # x = np.random.randn(8)
    # y = np.random.randn(8)
    # print(x)
    # print(y)
    #
    # print(np.maximum(x, y))
    # print(np.minimum(x, y))


    # arr = np.random.randn(7)*5
    # print(arr)
    #
    # remainder, whole_part = np.modf(arr)    # divmod 의 벡터화 버전.
    #                                         # 분수를 받아서 몫과 나머지를 리턴
    # print(remainder)
    # print(whole_part)


    # points = np.arange(-5, 5, 0.01) # -5 부터 4.99 까지 0.01씩 증가하는 값의 배열
    # print(points)
    # print(points.size)
    #
    # xs, ys = np.meshgrid(points, points)
    # print(ys)
    # print(ys.size)
    #
    # z = np.sqrt(xs**2 + ys**2)
    # print(z)
    # print(z.shape)
    #
    # plt.title("image plot of $\sqrt{x^2 + y^2} for a grid of values")
    # plt.imshow(z, cmap = plt.cm.gray)
    # plt.colorbar()
    # plt.show()


    # xarr = np.arange(1.1, 1.6, 0.1)
    # print(xarr)
    # yarr = np.arange(2.1, 2.6, 0.1)
    # print(yarr)
    # cond = np.array([True, False, True, True, False])
    # print(cond)
    #
    # # zarr = zip(xarr, yarr, cond)
    # # for obj in zarr:
    # #     print(obj)
    #
    # result = [ (x if c else y) for x, y, c in zip(xarr, yarr, cond) ]
    # print(result)


    arr = np.random.randn(4, 4)
    print(arr)
    print(np.where(arr > 0, 2, -2))
    print(np.where(arr > 0, 2, arr))
    print(np.where(arr > 0, True, False))

# 단항 유니버설 함수
# abs, fabs 각 원소의 절대값을 구한다.
# sqrt 각 원소의 제곱근을 구한다. arr**0.5와 동일하다.
# square 각 원소의 제곱을 구한다. arr**2와 동일하다.
# exp 각 원소에서 지수 e x 을 계산한다.
# log, log10, log2, log1p 각각 자연로그, 로그10, 로그2, 로그(1+x)
# sign 각 원소의 부호를 계산한다. 1(양수), 0(영), -1(음수)
# ceil 각 원소의 소수자리를 올린다.
# floor 각 원소의 소수자리를 내린다.
# rint 각 원소의 소수자리를 반올림한다.
# modf 각 원소의 몫과 나머지를 각각의 배열로 반환한다.
# cos, cosh, sin, sinh, tan, tanh 일반 삼각함수와 쌍곡삼각함수

# 이항 유니버설 함수
# add 두 배열에서 같은 위치의 원소끼리 더한다.
# subtract 첫 번째 배열의 원소에서 두 번째 배열의 원소를 뺀다.
# multiply 배열의 원소끼리 곱한다.
# divide, floor_divide 첫 번째 배열의 원소를 두 번째 배열의 원소로 나눈다.
# floor_divide 첫 번째 배열의 원소를 두 번째 배열의 원소로 나눈다. 몫만 취함
# power 첫 번째 배열의 원소를 두 번째 배열의 원소만큼 제곱한다.
# maximum, fmax 각 배열의 두 원소 중 큰 값을 반환한다.
# fmax nan 각 배열의 두 원소 중 큰 값을 반환한다. nan 값을 무시한다.
# minimum, fmin 각 배열의 두 원소 중 작은 값을 반환한다.
# fmax nan 각 배열의 두 원소 중 작은 값을 반환한다. nan 값을 무시한다.
# mod 첫 번째 배열의 원소를 두 번째 배열의 원소로 나눈 나머지
# copysign 첫 번째 배열 원소의 부호를 두 번째 배열 원소의 부호로 바꿈
# greater, greater_equal, less,
# less_equal, equal, not_equal
# 두 배열에서 같은 위치의 원소간 비교 연산 결과를 블리언 배열
# 로 반환한다.
# logical_and, logical_or,
# logical_xor
# 두 배열에서 같은 위치의 원소간 논리 연산 결과를 블리언 배열
# 로 반환한다.
