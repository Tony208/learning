#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_6
   Description :  菲波那切数列，又称黄金分割数列，值得是这样一个数列：0,1，1,2，3,5,8,13,21,34.......
   Author :       kai.chang01
   date:         2017/11/26 20:19
-------------------------------------------------
'''

# def fib(n):
#     a,b=1,1
#     for i in range(n-1):
#         a,b=b,a+b
#     return  a
# print fib(10)


# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print fib(10)

# def fib(n):
#     if n==1:
#         return [1]
#     if n==2:
#         return [1,1]
#     fibs=[1,1]
#     for i in range(2,n):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print fib(10)

# n= int(raw_input("第几个数："))
# f = (1/(5**0.5)*(((1+(5**0.5))/2))**n-((1-(5**0.5))/2)**n)
#
# l=[1]
# for i in range(1,n+1):
#     f=((l/(5**0.5))*(((l+(5**0.5))/2))**i-((l-(5**0.5))/2)**i)
#     l.append(int(f))

# def Fib(n):
#     a,b=0,1
#     while n:
#         a,b,n = b,a+b,n-1
#         print a
# Fib(7)

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b
#         a,b= b,a+b
#         n+=1
# max = int(input('input max num:'))
# for n in fib(max):
#     print n

# list =[]
# a=1
# list.append(a)
# b=1
# list.append(b)
# for i in range(1,20):
#     c = list[i-1]+list[i]
#     list.append(c)
# print list

# l = [0,1]
# for i in range(10):
#     l.append(reduce(lambda x,y:x+y,l[-1:-3:-1]))
# print l

# fe_list=[0,1]
# for i in range(1,11):
#     fe_list.append(sum(fe_list[(i-1):(i+1)]))
# print fe_list
