#!/usr/bin/env python
# coding: utf-8

# # Question 8

# From the motion of moon we have: $$\frac{GMm}{R^2}=m\omega^2R$$
# which gives us : $\omega=\frac{GM}{R^3}$.
# 
# On the other hand, the $\omega$ of moon and the satelite must be the same, and the equation of motion of the moon reads: (mass of satelite is s)
# 
# $$\frac{GMs}{r^2}- \frac{Gms}{(R-r)^2}=s\omega^2r$$
# $$\implies \frac{m}{(R-r)^2} = M[r^{-2} - \frac{r}{R^3}]$$
# 
# Now, we make it uniform by taking $m/M =s$, $r/R=x$, modifying the equatoin as:
# $$s=\frac{R^2(1-x)^2(1-x^3))}{r^2}=\frac{(1-x)^2(1-x^3)}{x^2}$$
# This can be further re-arranged as:
# $$sx^2= (1-2x+x^2)(1-x^3)= (1-2x+x^2+x^3-2x^4+x^5)$$
# $$\implies x^5 -2x^4 +x^3 +(1-s) x^2 -2x +1=0$$
# which is nothing but a 5th order polynomial.
# 
# 

# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt

m=7.348e22
M=5.974e24
R=3.844e8

s=m/M


def func(s,x):
    return x**5 -2*x**4 + x**3 +(1-s)*x**2 -2*x +1

#by physical definition x_solution must be within 0 and 1.

x=np.linspace(0.8, 1.2,1000)
y=[]
for i in range(len(x)):
    y.append(f(s,x[i]))

plt.plot(x,y)
plt.plot(x,np.zeros(len(x)))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-0.02,0.02)

#if s=0 then we have 3 repeated roots at 1, but a small s of the order 1e-2 will break this, that is why ylim is taken to be very small,
# to show the minor variation in t axis and the x.linspace is also small because the deviation between 2 roots is small.


# In[ ]:


def secant(f, guess1, guess2, tol):
    x_1=f(guess1)
    x_2=f(guess2)
    f1=f(x_1)
    while(f(x_2)>tol):
        f2=f(x_2)
        x_new=(x_1*f2-x_2*f1)/(f2-f1)
        x_1=x_2
        x_2=x_new
        f1=f2
    return x_1

def f(x):
    return func(s,x)
L1=(secant(f, 0.834, 0.835, 1e-10))
print(secant(f, 0.834, 0.835, 1e-10))
r=L1*R
r="{:.5e}".format(r)
print(r)


