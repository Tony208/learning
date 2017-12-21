#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    examp_5
   Description : 输入3个整数x,y,z. 请把这三个数从小到达输出
   Author :       kai.chang01
   date:         2017/11/26 12:58
-------------------------------------------------
# '''
# l=[]
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l

# x=int(raw_input("x:"))
# y=int(raw_input("y:"))
# z=int(raw_input("z:"))
# a={"x":x,"y":y,"z":z}
# for w in sorted(a,key=a.get):
#     print w,a[w]

# a=[1,3,5,2,4,5,7]
# n=len(a)
# for i in range(0,n):
#     for j in range(i,n):
#         if(a[i]>=a[j]):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print a


# x=raw_input("int1:")
# y=raw_input("int2:")
# Max = max(x,y)
# Min=min(x,y)
# z=raw_input("int3:")
# if z>Max:
#     print Min,Max,z
# elif z<Min:
#     print z,Min.Max
# else:
#     print Min,z,Max

# x = int(input("x="))
# y = int(input("y="))
# z = int(input("z="))
# num=[x,y,z]
# num.sort()
# print '这三个数从小到大的顺序为：',num
# runm = [x,y,z]
# runm.sort(reverse=True)
# print "这三个数从大道小的顺序为：",runm

# D = raw_input("请输入三个数字，格式如 'a,b,c,'：")
# li=D.split(",")
# li2=[int(i) for i in li]
# li2.sort()
# print li2


# while 1:
#     try:
#         x = int(raw_input("plz input x:"))
#         y = int(raw_input("plz input y:"))
#         z = int(raw_input("plz input z:"))
#         list1= [x,y,z]
#         print(sorted(list1))
#         break
#     except:
#         print("请输入整数：")

# a = int(raw_input("请输入："))
# b = int(raw_input("请输入："))
# c = int(raw_input("请输入："))
# if a > b and a > c:
#     x = a
#     a = c
# elif b > a and b > c:
#     x = b
#     b = c
# else:
#     x = c
# if a > b:
#     print b, a, x
# else:
#     print a, b, x


# x = int(raw_input("请输入x："))
# y = int(raw_input("请输入y："))
# z = int(raw_input("请输入z："))
# arr = [x, y, z]
# for i in range(0, 3):
#     for o in range(0, 3):
#         for p in range(0, 3):
#             if arr[i] > arr[o] > arr[p]:
#                 print arr[i], arr[o], arr[p]


# x=int(input("请输入一个整数x：\n"))
# y = int(input("请输入一个整数y：\n"))
# z=int(input("请输入一个整数z：\n"))
# if(x>y):
#     x,y=y,x
# if(y>z):
#     y,z=z,y
# print((x,y,z))

# elements = (4, 3, 5, 2, 6, 1, 7)
# print("正序排列：{}".format(sorted(elements)))
# print("倒叙排列：{}".format(list(reversed(sorted(elements)))))

# l = [int(i) for i in raw_input("请输入：").split()]
# l.sort()
# print l


# a = [int(i) for i in raw_input("请输入：").split()]
# m = len(a)
# while m != 1:
#     for i in range(m - 1):
#         if a[i] > a[i - 1]:
#             x = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = x
#     m -= 1
# print a
