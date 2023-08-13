#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath


#N is the number of walks and L is the grid size.
def randomwalk(N,L):
    x=[50]
    y=[50]
    i=50
    j=50
    
    for k in range(N):
        p=np.random.randint(0,4)
        if(p==0):
            i+=1
        if(p==1):
            i-=1
        if(p==2):
            j+=1
        if(p==3):
            j-=1
        i*=np.sign(i)
        j*=np.sign(j)
        if(i>(L-1)):
            i=2*L-2-i
        if(j>(L-1)):
            j=2*L-2-j
        x.append(i)
        y.append(j)
    return x,y
        
N=1000000
L=101
x,y = randomwalk(N,L)
            


# In[2]:


plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.title('randomwalk')
plt.show()


# Here we can see that each grid has almost equal probability of being approached. This essentially means the number of steps is so large that the particle visits every corner with almost equal probability. 

# In[3]:


#What about 10000 steps only?

N=10000
L=101
x,y = randomwalk(N,L)
plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.title('randomwalk')
plt.show()


# In[ ]:




