#!/usr/bin/env python
# coding: utf-8

# In[1]:


#part a
import math
def findHeight(T):
    G=6.67e-11
    M=5.9722e24
    R=6378.1e3
    h=((G*M*T**2)/(4*(math.pi)**2))**(1/3)-R
    h=h/1000
    return h

#part b
print("the height required for revolving in 1 day in km:", findHeight(86400)),
print("the height required for revolving in 90 minutes in km:", findHeight(5400)),
print("the height required for revolving in 45 minutes in km:", findHeight(2700))
      


# In[2]:


G=6.67e-11
M=5.9722e24
R=6378.1e3
T=math.sqrt((4*R**3*math.pi**2)/(G*M))
print(T/3600,"hours or", T/60, "minutes")


# In[3]:


print("The new height isin km",findHeight(23.93*3600))
p=findHeight(86400)-findHeight(23.93*3600)
print("Change in height in km", findHeight(86400)-findHeight(23.93*3600))


# In[ ]:




