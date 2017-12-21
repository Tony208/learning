#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_4
   Description : 输入某年某月某日，判断这一天是这一年的第几天
   Author :       kai.chang01
   date:         2017/11/26 11:22
-------------------------------------------------
'''
# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month < 12:
#     sum = months[month - 1]
# else:
#     print 'data error'
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print 'it is th %dth day.' % sum

# year = int(raw_input("年：\n"))
# month = int(raw_input("月：\n"))
# day = int(raw_input("日：\n"))
# month1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]  # 闰年
# month2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]  # 平年
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     Dth = month1[month - 1] + day
# else:
#     Dth = month2[month - 1] + day
# print "是该年的第%d天"%Dth


# p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年
# p = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年
# year = int(raw_input("年：\n"))
# month = int(raw_input("月：\n"))
# day = int(raw_input("日：\n"))
# arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# sum = day
# for i in range(0, month - 1):
#     sum += arr[i]
# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print "这是今年的第%d天" % sum
#     else:
#         sum = sum + 1
#         print "这是今年的第%d天" % sum
# else:
#     print "这是今年的第%d天" % sum

# p = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]  # 平年
# w = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]  # 闰年
# year = int(raw_input("年：\n"))
# month = int(raw_input("月：\n"))
# day = int(raw_input("日：\n"))
# if year%100 ==0:
#     if year%400 ==0:
#         d=w
#     else:
#         d=p
# else:
#     if year%4 ==0:
#         d=w
#     else:
#         d=p
# days=sum(d[0:month-1])+day
# print "%d,%d,%d是%d年的第%s天。"%(year,month,day,year,days)

import time
D=raw_input("请输入年份，格式如XXXX-XX-XX：")
d=time.strptime(D,'%Y-%m-%d').tm_yday
print "the {} day of this year!".format(d)
