#!/usr/bin/env python
# coding: utf-8

# # Q2

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[11]:


#defining the functions
a=1
b=0.5
c=2

def funcx(vec, t):
    x=vec[0]
    y=vec[1]
    return a*x - b*x*y

def funcy(vec, t):
    x=vec[0]
    y=vec[1]
    return b*x*y - c*y

def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t)])


# In[12]:


#defining RK for vectors
def RK_4(x, t, func, h):
    f=func(x,t)
    k1=h*f
    k2=h*func(x+k1/2, t+h/2)
    k3=h*func(x+k2/2, t+h/2)
    k4=h*func(x+k3, t+h)
    x= x + (k1+2*k2+2*k3+k4)/6
    t= t + h
    return [x,t]


# In[20]:


h=0.01

time=[0]
rabbit=[2]
fox=[2]

t=0
r=2
f=2

vec=np.array([r, f])

while(t<=30):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    rabbit.append(vec[0])
    fox.append(vec[1])
    time.append(t)


# In[21]:


plt.figure(figsize=(8,8))
plt.plot(time,rabbit, label="rabbit")
plt.plot(time,fox, label="fox")
plt.xlabel("time")
plt.ylabel("Number in thousands")
plt.title('population dynamics')
plt.legend()


# If we want to see the location of maxima and minima we may solve the equations:
# 
# For rabbit the number is stationary when $y= \frac{\alpha}{\beta}=2$, which is evident also from the graph. Also, $\frac{dx}{dt}=x(\alpha - \beta y)$, thus, the change is greater than 0, when y<2, other wise it is less than 0
# 
# For fox the number is stationary when $x= \frac{\delta}{\beta}=4$, which is also visible from the graph. Also, Also, $\frac{dy}{dt}=y(x\beta - \delta )$. So, the change ios greater than 0 when x>4, otherwise it is less than 0.
# It is a periodic graph.
# 
# Physical intuition is:
# 
# First due to the small number of rabbits(<4000), foxes dying due to old age are more in number so fox population declines, this enhances the rabbit population which increases due to the lack of predators, once it crosses the threshold of 4, fox population starts to increase due to increased pray. Once fox population crosses 2000, the rabbit population decreaes due to more praying by foxes than birthrate. Once it goes below, 4000 again fox population starts to decline and it is a periodic graph in that sense because both return to 2 after a certain time.
# 
# Maximum rabbit population is around 7000
# minimum around 2000
# 
# Maximum fox population is around 4300
# minimum is around 715

# In[ ]:




