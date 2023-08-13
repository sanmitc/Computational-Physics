#!/usr/bin/env python
# coding: utf-8

# # Question 2:

# Part a:

# In[ ]:


import numpy as np 
import math

def f(x):
    return x*(x-1)

def derivative(f,x, delta):
    return (f(x+delta)-f(x))/delta

print('result from derivative function is:', derivative(f,1,1e-2))

print("analytical result is: 1")


# There is a an approximate 1% difference between the true analytical value and the calcualated value.

# **Part-B**

# In[ ]:


print(' The results as delta is lowered is:')
print(derivative(f,1,1e-4))
print(derivative(f,1,1e-6))
print(derivative(f,1,1e-8))
print(derivative(f,1,1e-10))
print(derivative(f,1,1e-12))
print(derivative(f,1,1e-14))


# The error goes down till $10^{-8}$ but then increases, the cause being round off error, the difference between $f(x+\delta)$ and $f(x)$, does not decrease as much as is expected because it is rounded of, but $\delta$, decreases, which increases the quotient.
