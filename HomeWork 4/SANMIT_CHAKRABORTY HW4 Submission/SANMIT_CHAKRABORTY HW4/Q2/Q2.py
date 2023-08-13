#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Question 2

# In[2]:


import numpy as np 
import math
import cmath
import matplotlib.pyplot as plt


# In[3]:


D=np.loadtxt('sunspots.txt')

x=[D[i][0] for i in range(len(D))]
y=[D[i][1] for i in range(len(D))]

print(x)
print(y)


# In[4]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.xlabel('serial no. of months')
plt.ylabel('no of sunspots')
plt.title('variation of sunspots over months')

plt.show()


# In[5]:


from matplotlib.axis import YTick
#part b

#generalised DFT function: 
#inputs, function form and N.

fft_y=np.fft.fft(y)
ft_y=[(np.abs(z))**2 for z in fft_y]


plt.figure(figsize=(10,10))
plt.plot(x[1:], ft_y[1:])
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude squared of the coefficients')
plt.title('fourier decomposition of sunspot data')
plt.show()


# In[ ]:


#Let us examine the coefficient which is getting the peak.

plt.figure(figsize=(10,10))
plt.plot(x[1:], ft_y[1:])
plt.xlim(0, 100)
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude squared of the coefficients')
plt.title('fourier decomposition of sunspot data')
plt.show()


# This means that the maximum coefficient amplitude is achieved at the 24th coefficient. The period thus being approximately N/24= 3142/24=131 months. which matches with the graph when we notice that there is approximately 24 peaks in the whole graph of 3142 months, equally distanced more or less. 
