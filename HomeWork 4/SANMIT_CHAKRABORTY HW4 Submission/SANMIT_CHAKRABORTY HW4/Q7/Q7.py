#!/usr/bin/env python
# coding: utf-8

# # Q7

# The number of points on the screen is:
# $$N=\frac{dW}{\lambda f}= 400$$
# 
# But, the non zero values of y should be only confined to 40 values of the array, which will be padded by 180 zeroes before and after.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from numpy.fft import rfft, irfft, fft


# In[2]:


#y=sin((u\pi)/sw)


#sw is slit width

sw=20e-9
f=1
w=2e-4
W=2e-3
d=1e-1
lamda=5e-7

n=int((d*w)/(lamda*f))
N=(d*W)/(lamda*f)

def f(x, a):
    return np.abs(math.sin(a*x))

a=math.pi/sw
X=np.linspace(-w/2, w/2, n)
y=[f(x,a) for x in X]

pad=int((N-n)/2)
pad1=int((N+n)/2)

Y=np.zeros(int(N))
Y[:n]=y


Y_fft=fft(Y)

I=np.array([(W**2/N**2)*(np.abs(y)**2) for y in Y_fft])
I1=np.flip(I[:int(len(I)/2)])
I2=np.flip(I[int(len(I)/2):])

I=np.concatenate((I1, I2))



D=np.linspace(-5e-2, 5e-2, int(N))


plt.figure(figsize=(10,10))
plt.plot(D,I)
plt.xlabel('distance from cetral maxima in metres')
plt.ylabel('intensity')
plt.title('intensity profile')
plt.show()
plt.savefig('Intensity profile')

