# -*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  :

import numpy as np

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'bob'])
    data = np.random.randn(7, 4)
    print('--------------------')
    print(names)
    print('--------------------')
    print(data)
    print('--------------------')

    cond = names == 'bob'
    print(data[cond])
    print(data[~cond])
