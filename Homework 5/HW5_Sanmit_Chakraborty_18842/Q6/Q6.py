#!/usr/bin/env python
# coding: utf-8

# As there is a $1/\sqrt{x}$ term in the numerator which blows up at 0. We have to get rid of this term. So we need to divide by $1/\sqrt{x}$, Now, the normalisation constant in this case will be, 
# $$N=\int_0^1 \frac{dx}{\sqrt{x}}= 2$$ which essentially means the distribution will be:
# 
# $$w(x)=\frac{1}{2\sqrt{x}}$$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from numpy.random import uniform as unif


# In[2]:


# func: functional form
#w: weight factor
#xmin: lower x-bound
#xmax: higher x-bound
#N: number of points

def func(x):
    return 1/(math.sqrt(x)*(math.exp(x)+1))

def w(x):
    return 1/(2*math.sqrt(x)) 

#as the orginal function func diverges at x=0, we take 4 to be the upper limit or ymax. It is just a 
#dummy number chosen based on intuition and convenience. 
def w_mean(func, w, xmin, xmax, ymin, ymax, N):
    i=0
    suum=0
    while(i<N):
        xi=unif(xmin, xmax)
        yi=unif(ymin, ymax)
        if(yi>w(xi)):
            pass
        if(yi<=w(xi)):
            suum+= func(xi)/w(xi)
            i=i+1
    return suum/N

N=1000000
xmin=0
xmax=1
ymin=0
ymax=4

print(w_mean(func, w, xmin, xmax, ymin, ymax, N))
#We get a value of 0.83 which is quite near to that of 0.84

