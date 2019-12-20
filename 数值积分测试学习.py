# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:57:09 2019

@author: zhangfan
"""

import numpy,pylab

x=numpy.arange(0,3,0.001)

y=x**2

s=0
for i in range(len(x)):
    s=s+y[i]*0.001
    
s1=0
for i in range(len(x)-1):
    s1=s1+y[i+1]*0.001
    
s2=0
for i in range(len(x)-1):
    s2=s2+(y[i]+y[i+1])*0.001/2
    
print(s,s1,s2,1/3*3**3)



    
