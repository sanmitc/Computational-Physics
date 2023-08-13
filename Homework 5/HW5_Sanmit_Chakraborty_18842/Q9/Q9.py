#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
from IPython import display
from matplotlib.animation import FuncAnimation, PillowWriter


# In[2]:


#Defining the Cooling schedule

def ExpoCooling(T_i, T_f, tau, t):
    cool=math.exp(-t/tau)
    return T_i*cool +T_f*(1-cool)    


# In[5]:


#Defining the variables:
#T_i: Initial Temperature
#T_f: Final Temperature'
#tau: Cooling rate parameter
#num: Number of dimers
#grid: grid where dimers going to stick
#size: size of the sqaure grid
size=50
T_i=5
T_f=1e-80
tau=500
num=0
num1=0
k_b=1
grid=np.zeros((size, size))
dimer=np.zeros((size, size)) #shows the existence of a polymer

#making the animation
fig=plt.figure()
metadata=dict(title='movie', artist='Sanmit')
move=PillowWriter(fps=30, metadata=metadata)

 #shows the existence of a polymer

max_count=5000

with move.saving(fig, "Q9.gif", 100):
    for i in range(max_count):
        j1=np.random.randint(0,50)
        k1=np.random.randint(0,50)
        pos=[]
        if(k1<49):
            pos.append('right')
        if(k1>0):
            pos.append('left')
        if(j1<49):
            pos.append('down')
        if(j1>0):
            pos.append('up')
        L=len(pos)
        p=np.random.randint(0,L)
        if(pos[p]=='right'):
            j2=j1
            k2=k1+1
        if(pos[p]=='left'):
            j2=j1
            k2=k1-1
        if(pos[p]=='down'):
            j2=j1+1
            k2=k1
        if(pos[p]=='up'):
            j2=j1-1
            k2=k1

        val1=grid[j1][k1]
        val2=grid[j2][k2]

        if(val1==val2):
            if(val1==0):
                grid[j1][k1]=num1+1
                grid[j2][k2]=num1+1
                dimer[j1][k1]=1
                dimer[j2][k2]=1
                num+=1
                num1+=1

            else:
                T=ExpoCooling(T_i, T_f, tau, i)
                prob=math.exp(-1/(k_b*T))
                if(prob<1e-180):
                    pass
                else:
                    N=int(1/prob)
                    var=np.random.uniform(0,N)
                    if(var<1):
                        grid[j1][k1]=0
                        grid[j2][k2]=0
                        num-=1
                        dimer[j1][k1]=0
                        dimer[j2][k2]=0
        if(i%25==0):
            plt.imshow(dimer)
            move.grab_frame()
            plt.clf()


print(num)


# We are only doing till 5000 runs because after that finding empty spot becomes pretty unprobable, abd code takes long time to run.
