#!/usr/bin/env python
# coding: utf-8

# ##### Q1 

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath


# In[ ]:


#Part-A

up=7
down=1

int1= np.random.randint(down, up)
int2= np.random.randint(down, up)
print(int1, int2)


# In[ ]:


#Part-B

up=7
down=1
N=1000000
counter=0

for i in range(N):
    int1= np.random.randint(down, up)
    int2= np.random.randint(down, up)
    if(int1==6 and int2==6):
        counter+=1
        
        
prob=counter/N

print(prob)
    
#The answer is close to 1/36

