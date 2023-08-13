#!/usr/bin/env python
# coding: utf-8

# # Question 3
# 
# 

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,c):
    return 1-np.exp(-c*x)

#initial guess is facilitated by plotting the graph
x=np.linspace(-0.5,3,600)

y=np.zeros(600)
for i in range(600):
    y[i]=x[i]-f(x[i],2)

plt.plot(x,y)
plt.plot(x, np.zeros(len(x)))



# Primary guess is that the root is near 0.7, but the derivative of the function near 0.7 is not less than 1 in absolute value. So, we carry out a relaxation method. 
# 
# $$x=rf(x) = r(x-1+e^{-cx})$$
# where r is a small number let us say -0.5 to make the limit converge.
# 
# 

# 

# In[7]:


#part a
import numpy as np 
import math

def f(x,c,r):
    return x+r*(x-1+math.exp(-c*x))

def root(f, r,tolerance,c,guess):
    f_1=f(guess, c ,r)
    f_2=f(f_1, c, r)
    while(f_2-f_1>tolerance):
        f_1=f_2
        f_2=f(f_1,c,r)
    print('The final root is:')
    return (f_2)
#printinf all of the intermediate step also.
print(root(f,-0.5,1e-10,2,0.01))


# In[8]:


#part b
import matplotlib.pyplot as plt

c=np.linspace(0,3,100)

sol=np.zeros(len(c))

for i in range(len(c)):
    sol[i]=root(f,-0.5,1e-10, c[i], 0.01)

plt.plot(c,sol)


# There are many accelarations available, such as Anderson Accelaration which is related to solving the fixed point iteration in a matrix formalism. The method is a full fledged multi-dimensional optimisation problem. In this case, I am going to use a more simpler method which is Steffenson's method which does not calculate in a multidimension but accelarates the process by calculting mulltiple steps at once. It calculates:
# 
# $$p_{next}=p_n - \frac{(p_{n+1}-p_n)^2}{p_{n+2}-2p_{n+1}+p_n}$$
# where we have to start from 3 initial points. 

# In[9]:


import numpy as np 
import math

def f(x,c,r):
    return x+r*(x-1+math.exp(-c*x))

def root_stf(f, r,tol,c,guess1, guess2, guess3):
    f1=f(guess1, c, r)
    f2=f(guess2, c, r)
    f3=f(guess3, c, r)

    while(f3-f2>tol):
        f= f1 - ((f2-f1)**2)/(f3-2*f2+f1)
        f1=f2
        f2=f3
        f3=f
        print(f)
    return f

print(root_stf(f,0.03,1e-10,2, 0.09, 0.15, 0.2))


# In[ ]:




