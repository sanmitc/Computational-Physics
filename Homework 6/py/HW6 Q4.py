#!/usr/bin/env python
# coding: utf-8

# # Q4

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


#defining the functions
w=1

def funcx(vec, t):
    x=vec[0]
    y=vec[1]
    return y

def funcy(vec, t):
    x=vec[0]
    y=vec[1]
    return -w**2*x

def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t)])


# In[3]:


#defining RK for vectors
def RK_4(x, t, func, h):
    f=func(x,t)
    k1=h*f
    k2=h*func(x+k1/2, t+h/2)
    k3=h*func(x+k2/2, t+h/2)
    k4=h*func(x+k3, t+h)
    x= x + (k1+2*k2+2*k3+k4)/6
    t= t + h
    return [x,t]


# In[11]:


h=0.01

time=[0]
X1=[1]
X1_dash=[0]

t=0
x=1
y=0

vec=np.array([x,y])

while(t<=50):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X1.append(vec[0])
    X1_dash.append(vec[1])
    time.append(t)


# In[12]:


plt.figure(figsize=(8,8))
plt.plot(time, X1)
plt.xlabel("time")
plt.ylabel("x")
plt.title('SHO')


# In[15]:


#now making initial condition x=2

h=0.01

time=[0]
X2=[2]
X2_dash=[0]

t=0
x=2
y=0

vec=np.array([x,y])

while(t<=50):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X2.append(vec[0])
    X2_dash.append(vec[1])
    time.append(t)


# In[16]:


plt.figure(figsize=(8,8))
plt.plot(time, X1, label='x(0)=1')
plt.plot(time, X2, label='x(0)=2')
plt.xlabel("time")
plt.ylabel("x")
plt.title('SHO')
plt.legend()


#as seen from the graph, period remains same.


# In[22]:


#defining the functions
w=1

def funcx(vec, t):
    x=vec[0]
    y=vec[1]
    return y

def funcy(vec, t):
    x=vec[0]
    y=vec[1]
    return -w**2*x**3

def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t)])


# In[25]:


h=0.01

time=[0]
X=[1]
X_dash=[0]

t=0
x=1
y=0

vec=np.array([x,y])

while(t<=50):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X.append(vec[0])
    X_dash.append(vec[1])
    time.append(t)


# In[26]:


plt.figure(figsize=(8,8))
plt.plot(time, X)
plt.xlabel("time")
plt.ylabel("x")
plt.title('SHO')


# In[28]:


h=0.01

time=[0]
Xn=[2]
Xn_dash=[0]

t=0
x=2
y=0

vec=np.array([x,y])

while(t<=50):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    Xn.append(vec[0])
    Xn_dash.append(vec[1])
    time.append(t)


# In[33]:


plt.figure(figsize=(8,8))
plt.plot(time, X, label='x(0)=1')
plt.plot(time, Xn, label='x(0)=2')
plt.xlabel("time")
plt.ylabel("x")
plt.title('SHO')
plt.legend()

#amplitude increases


# In[50]:


plt.figure(figsize=(8,8))
plt.plot(X, X_dash, label='x(0)=1')
plt.plot(Xn, Xn_dash, label='x(0)=2')
plt.xlabel("X")
plt.ylabel("X'")
plt.title('SHO')
plt.legend()

#phase space plot


# In[35]:


#defining the functions
w=1

def funcx(vec, t):
    x=vec[0]
    y=vec[1]
    return y

def funcy(vec, t, mu, w):
    x=vec[0]
    y=vec[1]
    return -w**2*x + mu*(1-x**2)*y


# In[43]:


h=0.01

mu=1
w=1
def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])


time=[0]
X1=[1]
X1_dash=[0]

t=0
x=1
y=0

vec=np.array([x,y])
mu=1
w=1
def f(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])

while(t<=20):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X1.append(vec[0])
    X1_dash.append(vec[1])
    time.append(t)


# In[44]:


h=0.01

mu=1
w=1
def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])


time=[0]
X2=[1]
X2_dash=[0]

t=0
x=1
y=0

vec=np.array([x,y])
mu=2
w=1
def f(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])

while(t<=20):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X2.append(vec[0])
    X2_dash.append(vec[1])
    time.append(t)


# In[45]:


h=0.01

mu=1
w=1
def func(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])


time=[0]
X3=[1]
X3_dash=[0]

t=0
x=1
y=0

vec=np.array([x,y])
mu=4
w=1
def f(vec,t):
    return np.array([funcx(vec,t), funcy(vec, t, mu, w)])

while(t<=20):
    vec=RK_4(vec, t, func, h)[0]
    t=RK_4(vec, t, func, h)[1]
    X3.append(vec[0])
    X3_dash.append(vec[1])
    time.append(t)


# In[47]:


plt.figure(figsize=(8,8))
plt.plot(time, X1, label='mu=1')
plt.plot(time, X2, label='mu=2')
plt.plot(time, X3, label='mu=4')
plt.xlabel("time")
plt.ylabel("x")
plt.title('SHO')
plt.legend()


# In[51]:


#interesting phase plot
plt.figure(figsize=(8,8))
plt.plot(X1, X1_dash, label='mu=1')
plt.plot(X2, X2_dash, label='mu=2')
plt.plot(X3, X3_dash, label='mu=4')
plt.xlabel("X")
plt.ylabel("X'")
plt.title('SHO')
plt.legend()

