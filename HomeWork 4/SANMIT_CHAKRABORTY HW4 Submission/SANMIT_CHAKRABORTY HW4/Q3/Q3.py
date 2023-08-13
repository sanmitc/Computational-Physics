#!/usr/bin/env python
# coding: utf-8

# # Question 3
# 
# 

# In[1]:


import numpy as np 
import math
import cmath
import matplotlib.pyplot as plt


# In[2]:


x=np.loadtxt('trumpet.txt')

print(x)


# In[18]:


import matplotlib.pyplot as plt

N=len(x)

plt.figure(figsize=(10,10))

print(x)
plt.plot(np.linspace(0, N-1, N), x)
plt.xlabel('time scale')
plt.xlim(50000, 50500)
plt.ylabel('tone of music')
plt.title('trumptet music profile')

plt.show()

#we took a small snapshot because the frequency is high and plotting the whole graph is not going to show clearly.


# In[19]:


from matplotlib.axis import YTick
#part b

#generalised DFT function: 
#inputs, function form and N.
#ft_tr for fourier transform of trumpet.

fft_tr=np.fft.rfft(x)
ft_tr=[(np.abs(z)) for z in fft_tr]


plt.figure(figsize=(10,10))
plt.plot(np.arange(0,10000,1), ft_tr[:10000])
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude of the coefficients')
plt.title('fourier decomposition of trumpet')
plt.show()


# In[ ]:


#highest peak around 2400


plt.figure(figsize=(10,10))
plt.plot(np.arange(0,10000,1), ft_tr[:10000])
plt.xlim(2300, 2400)
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude of the coefficients')
plt.title('fourier decomposition of trumpet')
plt.show()


# The frequency is 2370/100000=1 beat/42.2 timeframes which translates to  round 1040 Hz.

# In[8]:


from google.colab import files

f=files.upload()


# In[9]:


x=np.loadtxt('piano.txt')

print(x)


# In[14]:


import matplotlib.pyplot as plt

N=len(x)

plt.figure(figsize=(10,10))
plt.plot(np.linspace(0, N-1, N), x)
plt.xlabel('time scale')
plt.xlim(50000, 50500)
plt.ylabel('tone of music')
plt.title('piano music profile')

plt.show()

#we took a small snapshot because t


# In[13]:



#part b

#generalised DFT function: 
#inputs, function form and N.
#ft_pi for fourier transform of piano

fft_pi=np.fft.fft(x)
ft_pi=np.abs(fft_pi)


plt.figure(figsize=(10,10))
plt.plot(np.arange(0,10000,1), ft_pi[:10000])
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude of the coefficients')
plt.title('fourier decomposition of piano')
plt.show()


# In[12]:


#highest peak around 2400


plt.figure(figsize=(10,10))
plt.plot(np.arange(0,10000,1), ft_pi[:10000])
plt.xlim(1000, 1500)
plt.xlabel('no. of coefficients')
plt.ylabel('magnitude of the coefficients')
plt.title('fourier decomposition of trumpet')
plt.show()


# Here, the frequency is nearly, 530 Hz.
# 
# CLearly, both are playing C4

# In[ ]:




