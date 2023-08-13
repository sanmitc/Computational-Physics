#!/usr/bin/env python
# coding: utf-8

# In[2]:


#question 16
import numpy as np
import math
import matplotlib.pyplot as plt



r=np.linspace(1,4,300)
y=[1/2]*300
for k in range(2000): 
    for j in range(300):
        y[j]=r[j]*y[j]*(1-y[j])
    if(k>1000):
        plt.scatter(r,y,0.1)
plt.xlabel('r')
plt.ylabel('x')
plt.title('deterministic chaos')
plt.show()


# In[5]:


#for values of r giving converging output after certain amount of iterations

n=np.linspace(1,2001,2000)
y=[1/2]
r=2.5
y_new=0
for i in range(1999):
    y_new=r*y[i]*(1-y[i])
    y.append(y_new)
    
plt.plot(n,y)
    


# In[8]:


#for values of r giving converging output after certain amount of iterations
#less number of iterations given to clearly depict the behaviour of the function

n=np.linspace(1,2001,2000)
y=[1/2]
r=3.2
y_new=0
for i in range(1999):
    y_new=r*y[i]*(1-y[i])
    y.append(y_new)
    
plt.plot(n[0:10],y[0:10])
    


# In[11]:


#for values of r giving converging output after certain amount of iterations

n=np.linspace(1,2001,2000)
y=[1/2]
r=3.52
y_new=0
for i in range(1999):
    y_new=r*y[i]*(1-y[i])
    y.append(y_new)
    
plt.plot(n[0:40],y[0:40])
#It jumps between 4 values


# In[13]:


n=np.linspace(1,2001,2000)
y=[1/2]
r=3.7
y_new=0
for i in range(1999):
    y_new=r*y[i]*(1-y[i])
    y.append(y_new)
    
plt.plot(n[0:40],y[0:40])
#Chaos


# In[17]:


#question 16
import numpy as np
import math
import matplotlib.pyplot as plt



r=np.linspace(3.5,3.6,50)
y=[1/2]*50
for k in range(2000): 
    for j in range(50):
        y[j]=r[j]*y[j]*(1-y[j])
    if(k>1000):
        plt.scatter(r,y,0.1)
plt.xlabel('r')
plt.ylabel('x')
plt.title('deterministic chaos')
plt.show()

#The edge of chaos is nearly 3.575


# In[ ]:




