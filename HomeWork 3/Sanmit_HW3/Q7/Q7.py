#!/usr/bin/env python
# coding: utf-8

# # Question 7

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return 924*(x**6) - 2772*(x**5) + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

x=np.linspace(0,1,200)
y=[]
for i in range(len(x)):
    y.append(f(x[i]))


plt.plot(x,y)
plt.plot(x, np.zeros(len(x)))
plt.xlabel('x')
plt.ylabel('f(x)')


# The roots are symmetric across 0.5 from inspection. The roots are approx: 0.03, 0.16, 0.4, 0.6, 0.84, 0.97. 
# 
# We can also define the derivative as we have a closed form of the function:
# 
# $$f'(x)=5544x^5 + 13860x^4 + 12600x^3 - 5040x^2 +840x -42$$

# In[ ]:


def f(x):
    return 924*(x**6) - 2772*(x**5) + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

def d_f(x):
    return 5544*x**5-13860*x**4+12600*x**3-5040*x**2+840*x-42

#starting guesses are 0.01, 0.2, 0.42, 0.58, 0.8, 0.99

def newton(f, guess, tol):
    x=guess
    while(np.abs(f(x))>tol):
        x=x-f(x)/d_f(x)
    return x

x=np.linspace(0,1,200)
y=[]
d_y=[]
for i in range(len(x)):
    y.append(f(x[i]))
    d_y.append(d_f(x[i]))

r=[]
r.append(newton(f, 0.01, 1e-6))
r.append(newton(f, 0.2, 1e-6))
r.append(newton(f, 0.42, 1e-6))
r.append(newton(f, 0.58, 1e-6))
r.append(newton(f, 0.8, 1e-6))
r.append(newton(f, 0.99, 1e-6))

print(r)

