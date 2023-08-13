#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Catalan(n):
    C=1
    m=0
    while(C<n):
        print(int(C))
        C=((4*m+2)*C)/(m+2)
        m+=1
        
s=float(input())
Catalan(s)

