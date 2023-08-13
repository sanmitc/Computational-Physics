#!/usr/bin/env python
# coding: utf-8

# # Question 4

# ### Part A
# 
# We have, $\frac{dx}{dt}= \frac{dy}{dt}=0$, which means:
# $$-x+ay+x^2y= 0$$
# $$b-ay-x^2y=0$$
# adding these 2 equations we get: 
# $$x=b$$
# And, putting this in the equation 2 we have:
# $$b=(a+b^2)y \implies y =\frac{b}{a+b^2}$$

# The first equation can be writen as: 
# $$x= ay+x^2y \implies x=(a+x^2)y$$
# $$b-(a+x^2)y=0 \implies y=\frac{b}{a+x^2}$$
# 

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D


x=np.linspace(-2.5,2.5,100)
y=np.linspace(-2.5,2.5,100)
X,Y=np.meshgrid(x,y)

a=1
b=2
Z1= X-(a+X**2)*Y
Z2=Y-b/(a+X**2)
Z3=X-X

figure=plt.figure(figsize=(15, 15))
img= figure.add_subplot(111, projection='3d')
img.plot_surface(X, Y, Z1, cmap='plasma', alpha=0.5)
img.plot_surface(X, Y, Z3, cmap='Oranges', alpha=0.4)
img.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.7)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




