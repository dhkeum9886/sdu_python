#-*- coding:utf-8 -*-
# @author       : dhkeum9886
# @description  : 


x=0
while x<10:
    x=x+1
    if x<5:
        continue
    print(x,end=',')
    if x>7:
        break

#
# if __name__ == '__main__':
#     print('file :', __file__)
#     # TODO