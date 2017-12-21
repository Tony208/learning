#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_9
   Description : 暂停一秒输出
   Author :       kai.chang01
   date:         2017/11/26 21:22
-------------------------------------------------
'''
# import time
#
# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print key, value
#     time.sleep(5)  # 暂停1秒

import time
l=[1,2,3,4]
for i in range(len(l)):
    print l[i]
    time.sleep(1) #暂停1秒
