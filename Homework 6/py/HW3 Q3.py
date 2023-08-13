#!/usr/bin/env python
# coding: utf-8

# # Q3

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[3]:


#defining the functions
sigma=10
r=28
b=8/3

def funcx(vec, t):
    x=vec[0]
    y=vec[1]
    z=vec[2]
    return sigma*(y-x)

def funcy(vec, t):
    x=vec[0]
    y=vec[1]
    z=vec[2]
    return r*x -y -x*z

def funcz(vec, t):
    x=vec[0]
    y=vec[1]
    z=vec[2]
    return x*y - b*z


def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t), funcz(vec, t)])


# In[10]:


def RK_4(x, t, func, h):
    f=func(x,t)
    k1=h*f
    k2=h*func(x+k1/2, t+h/2)
    k3=h*func(x+k2/2, t+h/2)
    k4=h*func(x+k3, t+h)
    x= x + (k1+2*k2+2*k3+k4)/6
    t= t + h
    return [x,t]


# In[11]:


h=0.01

time=[0]
X=[0]
Y=[1]
Z=[0]

t=0
x=0
y=1
z=0

vec=np.array([x,y,x])

while(t<=50):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X.append(vec[0])
    Y.append(vec[1])
    Z.append(vec[2])
    time.append(t)


# In[12]:


plt.figure(figsize=(8,8))
plt.plot(time,Y)
plt.xlabel("time")
plt.ylabel("y")
plt.title('deterministic chaos')


# In[13]:


plt.figure(figsize=(8,8))
plt.plot(X,Z)
plt.xlabel("X")
plt.ylabel("Z")
plt.title('strange attractor')


# In[ ]:




