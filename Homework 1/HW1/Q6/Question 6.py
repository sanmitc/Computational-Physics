#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def find(l,v):
    L=l*v
    G=6.67e-11
    M=1.9891e30
    vel=((2*G*M)/L)-v
    ape=(L/vel)
    e=1-(l/ape)
    a=(ape+l)/2
    time=math.sqrt((4*((math.pi)**2)*(a**3))/(G*M))
    T=time/(3600*24)
    print("The distance from sun in apehelion is:", ape)
    print("velocity at apehelion is", vel)
    print("The orbital period in years is:", T)
    print("The eccentricity is:", e)
  
print("give l_1 value as given in assignment")
l=float(input())
print("give v_1 value as given in assignment")
v=float(input())
find(l,v)


# In[ ]:




