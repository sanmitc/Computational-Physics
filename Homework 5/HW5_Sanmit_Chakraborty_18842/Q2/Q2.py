#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
import random


# In[ ]:


t_Bi=46*60
t_Tl=2.2*60
t_Pb=3.3*60
particle=10000
time=20000

n_Bi=particle
Bi213=[particle]

n_Tl=0
Tl209=[0]

n_Pb=0
Pb209=[0]

n_Bi209=0
Bi209=[0]

for i in range(1,time):
    #Pb-209
    P_Pb=1-2**(-i/t_Pb)
    N_Pb=int(1/P_Pb)
    decay=0
    for j in range(n_Pb):
        x=np.random.uniform(0,N_Pb)
        if(x<=1):
            decay+=1
    n_Pb-=decay
    n_Bi209+=decay
    
    #Tl-209
    P_Tl=1-2**(-i/t_Tl)
    N_Tl=int(1/P_Tl)
    decay=0
    for k in range(n_Tl):
        x=np.random.uniform(0,N_Tl)
        if(x<=1):
            decay+=1
    n_Tl-=decay
    n_Pb+=decay
    
    #Bi-213
    P_Bi=1-2**(-i/t_Bi)
    N_Bi=int(1/P_Bi)
    decay_Pb=0
    decay_Tl=0
    for l in range(n_Bi):
        x=np.random.uniform(0,N_Bi)
        decay=1
        if(x<=1):
            decay+=1
            y=np.random.uniform(0,100)
            if(y<2.09):
                decay_Tl+=1
            else:
                decay_Pb+=1
    n_Bi-=(decay_Pb+decay_Tl)
    n_Pb+=decay_Pb
    n_Tl+=decay_Tl
    
    Tl209.append(n_Tl)
    Pb209.append(n_Pb)
    Bi209.append(n_Bi209)
    Bi213.append(n_Bi)


# In[ ]:


t=np.arange(0, time, 1)

plt.figure(figsize=(10,10))
plt.plot(t, Bi213, label='Bi213')
plt.plot(t, Pb209, label='Pb209')
plt.plot(t, Bi209, label='Bi209')
plt.plot(t, Tl209, label='Tl209')
plt.legend()
plt.xlim(0,1000)
plt.xlabel('time(s)')
plt.ylabel('no, of particles')
plt.title('radio-active decay profile')
plt.show()

