#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import matplotlib.pyplot as plt
import math

finesse=1000
itr=100
x_max=2
x_min=-2
y_max=2
y_min=-2


import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

x=np.linspace(x_min,x_max,finesse)
y=np.linspace(x_min,x_max,finesse)
#[X,Y]=np.meshgrid(x,y)
def norm(x,y):
    return math.sqrt(x**2+y**2)
def colour(c,n):
    color=1
    z=0+0*1j
    for i in range(n):
        z=z**2+c
        if(norm(z.real,z.imag)>2):
            color=0
            break
    return color
    

z_0=np.zeros((finesse,finesse))

for i in range(finesse):
    for j in range(finesse):
        z=x[i]+y[j]*1j
        z_0[j][i]=colour(z,itr)
        
        
plt.contourf(x,y,z_0, cmap='Greys')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mandelbrot set')


# In[ ]:




