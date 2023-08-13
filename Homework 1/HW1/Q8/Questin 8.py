#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def getMadelung(L):
    V=0
    for i in range(-L,L):
        for j in range(-L,L):
            for k in range(-L,L):
                p=(i!=0 or j!=0 or k!=0)
                Atom=(i+j+k)
                if(Atom%2==1):
                    sign=-1
                else:
                    sign=1
                if(p):
                    k=math.sqrt(i**2+k**2+j**2)
                    V+=sign*(1/k)
    return V

Num=int(input())
getMadelung(Num)
                
                

