#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def RT(E,V):
    k_1=math.sqrt(E)
    k_2=math.sqrt((E-V))
    R=((k_1-k_2)/(k_1+k_2))**2
    T=(4*k_1*k_2)/((k_1+k_2)**2)
    print(R,T)
    o=R+T
    print(o)
       
RT(10, 9)

