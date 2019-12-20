# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:56:04 2019

@author: zhangfan
"""

Eps=1.0e-10  #精度


'''求解平方根算法函数'''
def Sqrt(x):
    eps=1.0
    x0=1.0
    x1=1.0
    while(eps>Eps):
        old=x1
        x1=(x0+x/x0)/2
        x0=x1
        eps=abs(x1-old)
    return x1

'''阶乘计算函数'''
def jie(x):
    s=1
    i=x
    while i>0:
        s=s*i
        i=i-1
    return s

'''exp计算函数'''
def exp(x):
    s=1
    i=1
    while i<18:
        s=s+power(x,i)/jie(i)
        i=i+1
    return s

'''次方函数'''
def power(x,t):
    s=1
    i=t
    while i>0:
        s=s*x
        i-=1
    return s

print(Sqrt(2)) #计算根号2的数值
