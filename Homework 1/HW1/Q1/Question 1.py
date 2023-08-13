#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib as plt
import math


# In[3]:


#Part-a: writing the function to find the time for any general height
def findtime(h,g):
    t=math.sqrt((2*h)/g)
    print(t)
    
g=9.81
print("enter the height in m:")
h=float(input())
findtime(h,g)


# In[4]:


#part b
g=9.81
findtime(100,g)


# In[ ]:




