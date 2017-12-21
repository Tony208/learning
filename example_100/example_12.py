#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_12
   Description : 判断100-200之间有多少个素数，并输出所有素数。
   Author :       kai.chang01
   date:         2017/11/26 21:41
-------------------------------------------------
'''
# l=[]
# for i in range(101,200):
#     for j in range(2,i-1):
#         if (i%j==0):
#             break
#     else:
#             l.append(i)
# print l
# print ('总数为：%d')%len(l)

# h =0
# leap = 1
# from math import  sqrt
# from sys import stdout
# for m in range(101,201):
#     k = int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m%i ==0:
#             leap=0
#             break
#     if leap==1:
#         print '%-4d' %m
#         h+=1
#         if h%10 ==0:
#             print ''
#     leap=1
# print 'The total is %d'% h

# from math import sqrt
# count=0
# pn=1
# for i in range(101,201):
#     k = int(sqrt(i))
#     for j in range(2,k+1):
#         if i%j==0:
#             pn=0
#             break
#     if pn==1:
#         count +=1
#         print i
#     pn = 1
# print "total number is %d" %count


# import  math
# m = range(101,201)
# p=m[:]
# for i in range(101,201):
#     for j in range(2,int(math.sqrt(i)+1)):
#         if i%j==0:
#             p.remove(i)
#             break
# print p
# print("101至201之间的素数一共有%d个" %len(p))

# import math
# def sushu():
#     result = []
#     for i in range(101,201):
#         flag = True
#         for j in range(2,int(math.sqrt(i)+1)):
#             if i%j ==0:
#                 flag=False
#                 continue
#         if flag == True:
#             result.append(i)
#     print result
# sushu()

# from math import sqrt
# l=[]
# for x in range(101,201):
#     l.append(x)
#     for i in range(2,int(sqrt(x)+1)):
#         if x%i ==0:
#             l.pop()
#             break
# n=len(l)
# print '总数为：%d个'%n
# print '101至201之间的素数为',l

def a(n):
    L = []
    for i in range(2,n-1):
        L.append(n%i)
    if 0 not in L:
        return True
print filter(a,range(101,200))




