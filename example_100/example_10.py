#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_10
   Description : 暂停一秒输出，并格式化当前日期
   Author :       kai.chang01
   date:         2017/11/26 21:28
-------------------------------------------------
'''
# import  time
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time.sleep(1)
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


import time,datetime
time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))
