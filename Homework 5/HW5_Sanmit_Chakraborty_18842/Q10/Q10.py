#!/usr/bin/env python
# coding: utf-8

# ##### Part-A
#  
#  The range of $\theta$ is 0 to $\pi$, the range of $\phi$ is 0 to $2\pi$. The probability distributions are normalised:
#  
#  $$\int_0^\pi \frac{d\theta sin\theta}{2}=-\frac{cos\theta}{2}|_0^\pi = - \frac{-1-1}{2}=1$$
#  $$\int_{0}^{2\pi}\frac{d\phi}{2\pi}=\frac{2\pi}{2\pi}=1$$

# ##### Part-B
# 
# $$z_\phi=\int_0^\phi \frac{d\phi}{2\pi}=\frac{\phi}{2\pi} \implies \phi=2\pi z_\phi$$
# $$z_\theta=\int_0^\theta \sin\theta/2 = (1-\cos\theta)/2 \implies \theta= \arccos(1-2z_\theta)$$

# In[3]:


#part-C
import random
import math
import numpy as np

#theta
z_t=np.random.uniform(0,1)
theta=math.acos(1-2*z_t)

#phi
z_p=np.random.uniform(0,1)
phi=2*math.pi*z_p

print(theta, phi)

