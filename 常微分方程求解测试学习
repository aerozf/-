# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:50:52 2019

@author: zhangfan
"""
import numpy

start=111111100  #求解起始值
end=111112100   #求解终止值
h=1.5    #步长
x=numpy.arange(start,end,h)
yy=1/3*x**3     #以求解y'=x^2为例，此处yy为实际已知的常微分方程的解
s=yy[0]   #初值

####################################################################
'''线性单步法'''
####################################################################

'''一级一阶R-K方法（欧拉法）'''
s=yy[0]
y=[]   #用来存放数值计算得到的值
for i in range(len(x)):
    y.append(s)
    s=s+h*(x[i])**2
    #print(y)
y=numpy.array(y)
eps1=[]  #用来存放误差
for i in range(len(y)):
  eps1.append(yy[i]-y[i])

'''二级二阶R-K方法'''
s=yy[0]
y=[]
for i in range(len(x)):
    y.append(s)
    k1=(x[i])**2
    k2=(x[i]+h)**2
    s=s+h*(k1+k2)/2
    #print(y)
y=numpy.array(y)
eps2=[]
for i in range(len(y)):
  eps2.append(yy[i]-y[i])
    
    
'''三级三阶R-K方法'''
s=yy[0]
y=[]
for i in range(len(x)):
    y.append(s)
    k1=(x[i])**2
    k2=(x[i]+h/3)**2
    k3=(x[i]+2*h/3)**2
    s=s+h*(k1+3*k3)/4
    #print(y)
y=numpy.array(y)
eps3=[]
for i in range(len(y)):
  eps3.append(yy[i]-y[i])    
    
'''四级四阶R-K方法'''
s=yy[0]
y=[]
for i in range(len(x)):
    y.append(s)
    k1=(x[i])**2
    k2=(x[i]+h/2)**2
    k3=(x[i]+h/2)**2
    k4=(x[i]+h)**2
    s=s+h*(k1+2*k2+2*k3+k4)/6
    #print(y)
y=numpy.array(y)
eps4=[]
for i in range(len(y)):
    eps4.append(yy[i]-y[i])    
    
    
    
    
    
    
####################################################################
'''线性多步法'''
####################################################################

'''三步显式Adams方法'''
s=yy[0]
y=[]
for i in range(2):
    y.append(s)
    k1=(x[i])**2
    k2=(x[i]+h/3)**2
    k3=(x[i]+2*h/3)**2
    s=s+h*(k1+3*k3)/4
for i in range(len(x)-2):
    y.append(s)
    s=y[i+2]+h/12*(23*x[i+2]**2-16*x[i+1]**2+5*x[i]**2)
y=numpy.array(y)
eps5=[]
for i in range(len(y)):
    eps5.append(yy[i]-y[i])  
    
    
'''四步显式Adams方法'''
s=yy[0]
y=[]
for i in range(3):
    y.append(s)
    k1=(x[i])**2
    k2=(x[i]+h/2)**2
    k3=(x[i]+h/2)**2
    k4=(x[i]+h)**2
    s=s+h*(k1+2*k2+2*k3+k4)/6
for i in range(len(x)-3):
    y.append(s)
    s=y[i+3]+h/24*(55*x[i+3]**2-59*x[i+2]**2+37*x[i+1]**2-9*x[i]**2)
y=numpy.array(y)
eps6=[]
for i in range(len(y)):
    eps6.append(yy[i]-y[i])  
    
