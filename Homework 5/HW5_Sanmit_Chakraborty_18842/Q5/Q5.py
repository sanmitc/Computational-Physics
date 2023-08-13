#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from numpy.random import uniform as unf
from numpy.random import rand


#D is dimension, N is the number of points, the later indices are the bounds

def I(D, N, xmin, xmax, ymin, ymax):
    sum=0
    for i in range(N):
        x=unf(-1,1,10)
        y=unf(-1,1,10)
        if(np.dot(x,y)<1):
            sum+=1
    return (2**D/N)*(sum)


xmin=-1
xmax=1
ymin=-1
ymax=1
D=10
N=1000000

print(I(D,N,xmin, xmax, ymin, ymax))

