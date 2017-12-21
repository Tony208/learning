#!/usr/bin/env python
# coding: UTF-8
'''
-------------------------------------------------
   File Name:    example_3
   Description : 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
   Author :       kai.chang01
   date:         2017/11/26 10:35
-------------------------------------------------
'''
# for i in range(1,85):
#     if 168%i ==0:
#         j=168/i
#         if i>j and (i+j)%2 == 0 and (i-j)%2 ==0:
#             m=(i+j)/2
#             n=(i-j)/2
#             x=n*n -100
#             x=m*m-100-168
#             print x

# for x  in range(1,13):
#     a = 84/x- x/2
#     if int(a) == a:
#         n = a**2 - 100
#         print n

# for i in  range(1,85):
#     if 168%i == 0:
#         j = 168/i
#         if i>j:
#             m=(i+j)/2
#             n=(i-j)/2
#             if m*m - 268 == n*n -100 and (n*n-100)%1 == 0:
#                 print ('x=',m*n-268)


# for m in range(168):
#     for n in range(m):
#         if (m + n) * (m - n) == 168:
#             x = n ** 2 - 100
#             print "符合条件的整数有：", x

# i=1
# while ((i+1)*(i+1)-i*i) <= 168:
#     i +=1
# for j in range(1,i):
#     for k in range(1,i):
#         if(k*k-j*j) == 168:
#             print k*k-268

# arr1 =[14,28,42,84]
# arr2 =[12,6,4,2]
# for i in range(0,4):
#     m = (arr1[i]+arr2[i])/2
#     n = (arr1[i]-arr2[2])/2
#     x = n*n -100
#     print x


# x1= map(lambda  i:i**2-100,range(1,100))
# x2 = map(lambda i:i**2-100-168,range(1,100))
# print(set(list(x1)) & set(list(x2)))

# t = []
# for m in range(168):
#     for n in range(m):
#         if m**2-n**2 ==168:
#             x = n**2 -100
#             t.append(x)
# print "符合条件的整数有：",t

# for i in range(1, 17):
#     for x in range(1, 168):
#         if 168 - (i ** 2 + 2 * x * i) == 0:
#             print x ** 2 - 100
