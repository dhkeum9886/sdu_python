# -*- coding: utf-8 -*-
# 소프트웨어공학과_2020620001_금동환.py

'''
Python 3.7.4
학과: 소프트웨어공학과
학번: 2020610001
이름: 금동환
'''

import os


def main():
    if False is os.path.isfile('./oddlines.txt') or False is os.path.isfile('./evenlines.txt'):
        return
    if os.path.exists('./output.txt'):
        os.remove('./output.txt')

    f_odd = open('./oddlines.txt', 'r', encoding='utf-8')
    f_even = open('./evenlines.txt', 'r', encoding='utf-8')
    f_out = open('./output.txt', 'w', encoding='utf-8')
    while True:
        line_odd = f_odd.readline()
        if not line_odd: break
        f_out.write(line_odd)
        line_even = f_even.readline()
        if not line_even: break
        f_out.write(line_even)
    f_out.close()
    f_even.close()
    f_odd.close()


if __name__ == '__main__':
    main()
