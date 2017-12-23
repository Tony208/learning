#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
-------------------------------------------------
   File Name:    用PIL(Python Imaging Library)生成验证的脚本
   Description : 用PIL生成验证的脚本，防止暴力破解，爬虫模拟登陆以及各种键盘钩子进行登录
                验证码的干扰机制：
                    1、背景或者线条起到干扰作用
                    2、文字进行扭曲
                RGB色彩值：
                    通过对红。绿，蓝 ，这三个值范围（0~255） 1600万中颜色  (255,255,255)灰色
                    (255,255,255,0.1) 第四个参数  一般为透明度值
                图片的扭曲方式：
                    水平：
                     缩放
                     倾斜
                     位移
                    垂直：
                     缩放
                     倾斜
                     位移
                PIL的安装：pip insall PIL
   Author :      tony
   date:         2017/12/13 19:22
-------------------------------------------------
'''
import  random  #随机模块，可以生成随机数
from PIL import Image,ImageDraw,ImageFont,ImageFilter
#Image  负责处理图片      #ImageDraw 负责处理画笔        #ImageFont 负责处理字体            #ImageFilter 负责处理滤镜
# 项目步骤：
# 1、定义一张图片
img = Image.new("RGB",(150,50),(255,255,255))    # 第一个参数：代表我么采用RGB颜色模式    第二个参数：代表图片大小   第三个参数：具体的图片颜色
# 2、创建画笔
draw = ImageDraw.Draw(img)
# # 3、绘制线条和点
# #  绘制线
for i in range(random.randint(1,10)):
    draw.line(
        #绘制线条时有个特色：每条线有两个点：每个点靠x,y两个值来确定位置
        [
            (random.randint(1,150),random.randint(1,150)),
            (random.randint(1,150),random.randint(1,150)),
        ],
        fill =(0,0,0)
    )
#   #   绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1,150),
            random.randint(1,150)
        ],
        fill = (0,0,0)
    )
# 4、绘制我们的文字
# 我们的文字是随机生成的   我们的文字个数是一定的
# 定义我们要生成随机数的字母和数字
font_list = list("abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789")
c_chars = "".join(random.sample(font_list,4))
# random.sample 在指定的列表中随机的取出指定个元素
#绘制字体  需要先定制一下字体
font = ImageFont.truetype("simsun.ttc",26)  #20位字体大小
draw.text((5,5),c_chars,font=font,fill="green")
#参数1：代表文字的位置，距离上和左的距离
#参数2：代表文字的内容
#参数3：代表字体
#参数4：字体颜色
# 5、定义扭曲的参数
params = [1-float(random.randint(1,2))/100,  #扭曲程度
          0,
          0,
          0,
          1-float(random.randint(1,2))/100,
          float(random.randint(1,2))/500,
          0.001,
          float(random.randint(1,1))/500.
          ]
# 6、使用滤镜 添加滤镜
img = img.transform((150,50),Image.PERSPECTIVE,params)  #参数1：扭曲范围  参数2：扭曲样式  参数3：扭曲的参数
#  进行扭曲
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.show()










