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
import tables
import sqlite3

if __name__ == '__main__':
    print('file :', __file__)
    # TODO

    # # pickle read, write
    # data = pd.read_csv('examples/ex1.csv')
    # print(data)
    # data.to_pickle('examples/ex1_pickle')
    #
    # fp = pd.read_pickle('examples/ex1_pickle')
    # print(fp)

    # # HDF5
    # df = pd.DataFrame({'b':np.random.randn(200)})
    # # print(df)
    #
    # store = pd.HDFStore('mydata.h5')
    # print(store)
    # # store['obj1'] = df
    # # store['obj1_col'] = df['b']
    # # print(store['obj1'])
    # # print(store['obj1_col'])
    #
    # df = pd.DataFrame({'d':np.random.randn(200)})
    #
    # store = pd.HDFStore('mydata.h5')
    # store.put('obj2', df, format='table')
    # print(store)
    # print(store.select('obj2', where=['index >= 10 and index <= 15']))
    # store.close()
    # with pd.HDFStore('mydata.h5') as store:
    #     print(store)
    #     print(store.select('obj2', where=['index >= 10 and index <= 15']))

    # # excel
    # fp = pd.read_pickle('examples/ex1_pickle')
    # fp.to_hdf('mydata.h5', 'obj3', format='table')
    # with pd.HDFStore('mydata.h5') as store:
    #     print(store)
    #     print(store.select('obj3'))
    # xlsx = pd.ExcelFile('examples/ex1.xlsx')
    # data = pd.read_excel(xlsx, 'Sheet1')
    # print(data)
    # data = pd.read_csv('examples/ex1.csv')
    # writer = pd.ExcelWriter('examples/ex3.xlsx')
    # data.to_excel(writer, 'Sheet1')
    # writer.save()

    # # Sqlite
    # query1 = """CREATE TABLE test
    #         (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"""
    # query2 = """DROP TABLE test"""
    # conn = sqlite3.connect('mydata.sqlite')
    # conn.execute(query2)
    # conn.commit()

    # cursor = conn.execute("SELECT * FROM test;")
    # rows = cursor.fetchall()
    # print(rows)

    # data = [
    #         ('atlanta', 'georgia', 1.25, 6),
    #         ('tallahassee', 'florida', 2.6, 3),
    #         ('sacramento', 'califonia', 1.7, 5)
    # ]
    # stmt = "INSERT INTO test VALUES(?,?,?,?);"
    # conn.executemany(stmt, data)
    # conn.commit()

