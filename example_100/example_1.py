#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    example_100
   Description : 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
   程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
   Author :       kai.chang01
   date:         2017/11/24 19:18
-------------------------------------------------
'''
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                print i,j,k
'''
'''
d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and(i!=k) and (j!=k):
               d.append([i,j,k])
print "总数量：",len(d)
print d
'''
'''
#将for循环和if语句综合成一句，直接打印出结果
list_num=[1,2,3,4]
d=[i*100+j*10+k for i in list_num for j in list_num for k in list_num if
   (i!=j) and (i!=k) and (j!=k)]
print d
print len(d)
'''
'''
#参考方法(设置最大，最小值)：
line=[]
for i in range(123,433):
    a = i%10
    a = i%10
    b = (i%100)//10
    c = (i%1000)//100
    if a!=b and a!=c and b!=c and 0<a<5 and 0<b<5 and 0<c<5:
        print i
        line.append(i)
print('the total is:',len(line))
'''
'''
#用集合去除重复元素
import pprint
list_num=['1','2','3','4']
list_result=[]
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i+j+k))==3:
                list_result+=[int(i+j+k)]
print("能组成%d个互不形同且无重复数字的三位数："%len(list_result))
pprint.pprint(list_result)
'''
'''

#python自带函数
from itertools import permutations
for i in permutations([1,2,3,4],3):
    print i
 '''
'''
from itertools import permutations
for i in permutations([1,2,3,4],3):
    k = ''
    for j in range(0,len(i)):
        k = k+str(i[j])
    print (int(k))
'''
'''
from itertools import  permutations
t = 0
for i in permutations('1234',3):
    print (''.join(i))
    t+=1
print("不重复的数量有:%s"%t)
'''
'''
#位运算
#从 00 01 10  到  11 10 01
for num in range(6,58):
    a = num >> 4&3
    b = num >> 2&3
    c = num & 3
    if(a^b) and (b^c) and (c^a):
        print a+1,b+1,c+1
'''
'''
#考虑减少冗余判断和循环，做如下优化；
for i in range(1,5):
    for j in range(1,5):
        if(j==i):
            continue;
        for k in range(1,5):
            if(k==i or k==j):
                continue
            print(i,j,k)
'''
'''
list_num=[1,2,3,4]
list = [i*100+j*10+k for i in list_num for j in list_num for k in list_num
        if (i!=j) and (i!=k) and (j!=k)]
d=len(list)
print('1,2,3,4能组成%d个互补形同而无重复数字的三位数。'%d)
print ('他们个是：%s' %list)
'''
'''
#直接用列表推导式
[(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if(x!=y)and(x!=z)and(y!=z)]
'''
'''
d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                d.append(int(str(i)+str(j)+str(k)))
print d
print len(d)
'''