#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    Learning1
   Description :
   Author :      tony
   date:         2017/12/13 19:22
-------------------------------------------------
'''

from bs4  import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import htmllib

URL='http://gz.ganji.com/fang1/'  #爬取的目标地址
ADDR='http://gz.ganji.com/' #赶集首页

if __name__ == '__main__':
    start_page = 1 #开始爬取的页面
    end_page = 10#结束爬取的页面
    price = 7 #价格
    with open('ganji.csv','wb') as f: #创建一个csv文件  wb 读写模式      不需要关闭文件
        #等价于 f = open('ganji.csv,'wb') 需要关闭文件
        # '天通苑一区','天通苑','7000'
        csv_writer = csv.writer(f,delimiter=',')
        print('start.........')
        while start_page<=end_page:
            start_page+=1
            print ('get:{0}'.format(URL.format(start_page= start_page, price = price)))
            reponse = requests.get(URL.format(start_page=start_page,price=price))
            html = BeautifulSoup(reponse.text,'html.parser')  #第一个参数是要抓取的html文本，第二个是使用哪种解析器
            house_list = html.select('.f-list>.f-list-item>.f-list-item-wrap')#获取房源信息
            if not house_list:
                break
            for house in house_list:
                house_title=house.select('title>a')[0].string.encode('UTF-8')
                housr_addr = house.select('address>.area>a')[-1].string.encode('UTF-8')
                housr_price=house.select('info>.price>num')[0].string.encode('UTF-8')
                house_url=urljoin(ADDR,house.select('title>a')[0]['href'])
                csv.writer.writerow([house_title,housr_addr,housr_price,house_url])
        print ('end...............')
