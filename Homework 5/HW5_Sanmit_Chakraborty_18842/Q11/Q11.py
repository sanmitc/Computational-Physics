#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# ##### Part-A,B

# In[ ]:


#for 101x101 grid
def diffusion_1(L):
    mid=int((L)/2)
    grid=np.zeros((L,L))
    new_particle=(grid[mid][mid+1] or grid[mid][mid-1] or grid[mid+1][mid] or grid[mid-1][mid])
    max_count=1000
    k=0
    i=mid
    j=mid
    terminate=0
    while(terminate==0):
        stop=0
        i=mid
        j=mid
        while(stop==0):
            p=np.random.randint(0,4)
            if(p==0):
                i+=1
            if(p==1):
                i-=1
            if(p==2):
                j+=1
            if(p==3):
                j-=1
            if(i==0 or i==L-1 or j==0 or j==L-1 or grid[i][j+1]==1 or grid[i][j-1]==1 or grid[i-1][j]==1 or grid[i+1][j]==1):
                grid[i][j]=1
                stop=1
        if(i==mid and j==mid):
            terminate=1
        k+=1
    return grid

L=101
x = diffusion_1(L)
plt.figure(figsize=(10,10))
plt.imshow(x)


# In[ ]:


#for 201x201 grid
def diffusion_1(L):
    mid=int((L)/2)
    grid=np.zeros((L,L))
    new_particle=(grid[mid][mid+1] or grid[mid][mid-1] or grid[mid+1][mid] or grid[mid-1][mid])
    max_count=1000
    k=0
    i=mid
    j=mid
    terminate=0
    while(terminate==0):
        stop=0
        i=mid
        j=mid
        while(stop==0):
            p=np.random.randint(0,4)
            if(p==0):
                i+=1
            if(p==1):
                i-=1
            if(p==2):
                j+=1
            if(p==3):
                j-=1
            if(i==0 or i==L-1 or j==0 or j==L-1 or grid[i][j+1]==1 or grid[i][j-1]==1 or grid[i-1][j]==1 or grid[i+1][j]==1):
                grid[i][j]=1
                stop=1
        if(i==mid and j==mid):
            terminate=1
        k+=1
    return grid

L=201
x = diffusion_1(L)
plt.figure(figsize=(10,10))
plt.imshow(x)


# In[ ]:


#with colour variation
def diffusion_1(L):
    mid=int((L)/2)
    grid=np.zeros((L,L))
    new_particle=(grid[mid][mid+1] or grid[mid][mid-1] or grid[mid+1][mid] or grid[mid-1][mid])
    max_count=1000
    k=1
    i=mid
    j=mid
    terminate=0
    while(terminate==0):
        stop=0
        i=mid
        j=mid
        while(stop==0):
            p=np.random.randint(0,4)
            if(p==0):
                i+=1
            if(p==1):
                i-=1
            if(p==2):
                j+=1
            if(p==3):
                j-=1
            if(i==0 or i==L-1 or j==0 or j==L-1 or grid[i][j+1]!=0 or grid[i][j-1]!=0 or grid[i-1][j]!=0 or grid[i+1][j]!=0):
                grid[i][j]=k
                stop=1
        if(i==mid and j==mid):
            terminate=1
        k+=1
    return grid

L=101
x = diffusion_1(L)
plt.figure(figsize=(10,10))
plt.imshow(x)
plt.colorbar()
            


# In[11]:


def diffusion_2(L):
    grid=np.zeros((L,L))
    #setting the middle anchored particle
    mid=int(L/2)
    grid[mid][mid]=1
    r=1
    half=int(mid/2)
    m=10000
    k=0
    out=0
    while(r<half+1):
        k+=1
        #initialise position of random particle
        theta=np.random.uniform(-math.pi, math.pi)
        i=mid+int(r*math.cos(theta))
        j=mid+int(r*math.sin(theta))
        stop=(grid[i][j+1]!=0 or grid[i][j-1]!=0 or grid[i-1][j]!=0 or grid[i+1][j]!=0)
        if(stop!=0):
            if(r==1):
                r+=1
            if(math.sqrt((i-mid)**2+(j-mid)**2)>r-1):
                r+=1
            pass
        else:#start evolution
            while(stop==0):
                if(math.sqrt((i-mid)**2+(j-mid)**2)>=2*r-1):
                    break
                p=np.random.randint(0,4)
                if(p==0):
                    i+=1
                if(p==1):
                    i-=1
                if(p==2):
                    j+=1
                if(p==3):
                    j-=1
                if(grid[i][j+1]!=0 or grid[i][j-1]!=0 or grid[i-1][j]!=0 or grid[i+1][j]!=0):
                    stop=1
                    grid[i][j]=k
                    if(math.sqrt((i-mid)**2+(j-mid)**2)>r):
                         r+=1
                    break
    return grid
                
        
    
L=101
grid1=(diffusion_2(L))
plt.figure(figsize=(10,10))
plt.imshow(grid1)
plt.colorbar()
plt.show()


# In[ ]:




