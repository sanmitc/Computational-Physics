#!/usr/bin/env python
# coding: utf-8

# # Q6

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath


# In[2]:


def c_fft(x):
    if(len(x)==1):
    res=x[0]
    else:
    N=len(x)
    x_o=c_fft(x[1::2])
    x_e=c_fft(x[::2])
    expo=[np.exp((-2*math.pi*1j*i)/N) for i in range(N)]
    arr1=x_e+np.divide(x_o, expo[:(N+1)//2])
    arr2=x_e+np.divide(x_o, expo[(N+1)//2:])
    res=np.concatenate([arr1, arr2])
    return res


def c_ifft(x):
    if(len(x)==1):
    res=x[0]
    else:
        N=len(x)
        x_o=c_ifft(x[1::2])
        x_e=c_ifft(x[::2])
        expo=[cmath.exp((-2*math.pi*1j*i)/N) for i in range(N)]
        arr1=x_e+np.divide(x_o, expo[:int(N/2)+1])
        arr2=x_e+np.divide(x_e, expo[int(N/2)+1:])
        res=np.concatenate([arr1, arr2])
    return res


# In[3]:


x=np.random.rand(1000)


# In[4]:


print(c_fft(x))


# In[ ]:




