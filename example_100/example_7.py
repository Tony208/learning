#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_7
   Description : 将一个列表的数据复制到另一个列表中
   Author :       kai.chang01
   date:         2017/11/26 20:45
-------------------------------------------------
'''

# a=[1,2,3]
# b=a[:]
# print b

# l=[1,2,3,4,5]
# p=[]
# for i in range(len(l)):
#     p.append(l[i])
# print p

# a=[1,2,3,4]
# b=[i for i in a]
# print b

# a=[1,2,3,4,5]
# b=list()
# for i in a:b.append(i)
# print b


# a=[1,2,3,4,5,6,7]
# b=a*1
# print b

# list1=[1,2,3]
# list2=[]
# list2.append(list1)
# print list2

# import copy
# a=[1,2,3,4,5]
# b=["A","B",a]
# c=b[:]
# print c
#
# a[0]=11
# print c
#
# c=copy.deepcopy(b)
# print c
# a[0]=111
# print c



a=[1,2,3]
b=a[:]
print b
a[0]=11
print b
a=[1,2,3]
b=a
print b
a[0]=22
print b


