#!/usr/bin/env python
# coding: utf-8

# In[1]:


#defining the function
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from numpy import random as rn


def func(x):
    return math.sin(1/(x*(2-x)))**2
    
#we take 2x1 grid here as done in the class.Area=2

def M_C1(func, xmin, xmax, ymin, ymax, N):
    counter=0
    for i in range(N):
        y=rn.uniform(ymin, ymax)
        x=rn.uniform(xmin, xmax)
        if(y<func(x)):
            counter+=1
    area=(ymax-ymin)*(xmax-xmin)
    return area*(counter/N)

def M_C1_err(func, xmin, xmax, ymin, ymax, N):
    I=M_C1(func, xmin, xmax, ymin, ymax, N)
    A=(xmax-xmin)*(ymax-ymin)
    return math.sqrt(I*(A-I)/N)

print(M_C1(func, 0, 2, 0 , 1, 100000))
print(M_C1_err(func, 0, 2, 0, 1, 100000))

#error
    


# In[2]:


def M_C2(f, xmin, xmax, N):
    suum=0
    for i in range(N):
        x=rn.uniform(xmin, xmax)
        suum+=f(x)
    return (xmax-xmin)*suum/N

def M_C2_err(f, xmin, xmax, N):
    suum=0
    sqr=0
    for i in range(N):
        x=rn.uniform(xmin, xmax)
        suum+=f(x)
        sqr+=f(x)**2
    var=-suum**2/N**2+sqr/N
    return (xmax-xmin)*math.sqrt(var/N)

xmin=0
xmax=2
N=1000000

print(M_C2(func, xmin, xmax, N))
print(M_C2_err(func, xmin, xmax, N))
    

