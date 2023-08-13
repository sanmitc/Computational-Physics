#!/usr/bin/env python
# coding: utf-8

# # Q9

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[12]:


def func(x,v,t):
    return (v**2 - x -5)
    


# In[13]:


h=1e-3

X=[1]
V=[0]
T=[0]

x=1
v=0
t=0
v=v+(h/2)*func(x,v,t)
while(t<=50):
    x=x+h*v
    v=v+h*func(x,v,t)
    t+=h
    X.append(x)
    V.append(v)
    T.append(t)


# In[14]:


plt.figure(figsize=(8,8))
plt.plot(T,X)
plt.xlabel("time(s)")
plt.ylabel("X")
plt.title('trajectory(m)')


# In[ ]:




