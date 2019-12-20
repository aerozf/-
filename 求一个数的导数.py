# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:17:01 2019

@author: zhangfan
"""

import numpy

x=numpy.arange(1,10,0.0001)

'''求导数函数
输入值第一项为公式，第二项为要求的x点
返回值第一项为函数值，第二项为导数值，第三项为二阶导数值
'''

#导数计算函数
def dao(y_,x0):
    x=numpy.array([x0-0.000001,x0,x0+0.000001])
    y=eval(y_)
    return [y[1],(y[2]-y[0])/0.000002,(y[2]+y[0]-2*y[1])/(0.000001)**2]
    
print(i,dao("x**3",2)) #计算y=x^3在x=2处的导数值


