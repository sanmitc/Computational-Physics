#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from numpy.random import uniform as unif
import random


# ##### Part-A

# In[4]:


def Energy(array, J):
    row=array.shape[0]
    col=array.shape[1]
    suum=0
    for i in range(row-1):
        suum+=np.dot(array[i], array[i+1])
    for j in range(col-1):
        suum+=np.dot(array[:,i], array[:,i+1])
    return -J*suum


# ##### Part-B,C

# In[ ]:


#G: Number of grids
#k_b: Boltzmann Constant
#T: Temperature
#J: Ising model constant
#N: The number of Monte-Carlo steps


#I created a 21x21 grid where the inner 20x20 grid is a matrix of values 1, and -1, chosen randomly for 
#each coordinate. The outer entries are still 0. 
T=1
k_b=1
G=20
J=1
arr=np.zeros([G+1, G+1])
for i in range(1,G):
    for j in range(1,G):
        arr[i][j]=random.choice([-1,1])
M=np.sum(arr)

y=[M]
N=1000000
x=np.arange(0,N+1)
for k in range(N):
    i = np.random.randint(1,G)
    j = np.random.randint(1,G)
    E_int=-arr[i][j]*(arr[i][j-1]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j])
    if(E_int>=0):
        arr[i][j]*=-1
    if(E_int<0):
        beta=1/(k_b*T)
        prob=math.exp(beta*E_int*2)
        sample=int(1/prob)
        ran=unif(0,sample)
        if(ran>=1):
            arr[i][j]*=-1
    M=M+2*arr[i][j]
    y.append(M)
    
y=np.array(y)  


plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("Magnetisation")
plt.title("Magentisation Profile Over time")


# ##### Part-D

# In[ ]:


plt.figure(figsize=(10,10))
plt.imshow(arr[1:G,1:G], cmap="hot")
plt.colorbar()
plt.show()


# $\textbf{So, what is happening?}$
# 
# Here we can see in the saved pictures that sometimes the built up magnetization is positive or sometimes is it negative, it comes from the fact that the process is randomised and +1 and -1 in this case is symmetric. 
# 
# Let us say:
# The random point that was chosen first was surrounded by positive points, so it got converted to positive if it was negative. This case went on the back of a cascasding effect. Increasing the number of +1's. Somewhere the random picker encountered an area sorrounded by negatives. This again gave rise to conversion of positives into negatives which overpowered the previous action. So, we see periodic fluctuations in the magnetisation. It goes to high positive zone and then goes to highly negative zone. But it settles down in a bias(either positive/negative) in the end. It complete depends upon the environment of the random points that being chosen by the random choosing.

# ##### Part-E

# In[ ]:


T=2
k_b=1
G=20
J=1
arr=np.zeros([G+1, G+1])
for i in range(1,G):
    for j in range(1,G):
        arr[i][j]=random.choice([-1,1])
M=np.sum(arr)

y=[M]
N=1000000
x=np.arange(0,N+1)
for k in range(N):
    i = np.random.randint(1,G)
    j = np.random.randint(1,G)
    E_int=-arr[i][j]*(arr[i][j-1]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j])
    if(E_int>=0):
        arr[i][j]*=-1
    if(E_int<0):
        beta=1/(k_b*T)
        prob=math.exp(beta*E_int*2)
        sample=int(1/prob)
        ran=unif(0,sample)
        if(ran>=1):
            arr[i][j]*=-1
    M=M+2*arr[i][j]
    y.append(M)
    
y=np.array(y)  


plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("Magnetisation")
plt.title("Magentisation Profile Over time")


# In[ ]:


T=3
k_b=1
G=20
J=1
arr=np.zeros([G+1, G+1])
for i in range(1,G):
    for j in range(1,G):
        arr[i][j]=random.choice([-1,1])
M=np.sum(arr)

y=[M]
N=1000000
x=np.arange(0,N+1)
for k in range(N):
    i = np.random.randint(1,G)
    j = np.random.randint(1,G)
    E_int=-arr[i][j]*(arr[i][j-1]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j])
    if(E_int>=0):
        arr[i][j]*=-1
    if(E_int<0):
        beta=1/(k_b*T)
        prob=math.exp(beta*E_int*2)
        sample=int(1/prob)
        ran=unif(0,sample)
        if(ran>=1):
            arr[i][j]*=-1
    M=M+2*arr[i][j]
    y.append(M)
    
y=np.array(y)  


plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("Magnetisation")
plt.title("Magentisation Profile Over time")


# A visible change which is observed is that the rapid fluctuations of the system has decreased a lot as the temperature has been increased. 
# 
# The probability of a lower energy state going to a higher energuy state is $e^{-\Delta E/(kT)}$, for T=1, it is significant. The high energy state goes to the low energy state with probability 1. But, the reverse also happens more when the temperature is low. This effectively amounts to more fluctuations. Which is seen in T=1, it has decreased as T has increased.

# In[ ]:




