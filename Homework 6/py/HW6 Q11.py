#!/usr/bin/env python
# coding: utf-8

# # Q11

# THe schrodinger equation is given by:
# $$-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + V \psi =E \psi$$
# 
# defining $v=\frac{d\psi}{dx}$, we have :
# $$-\frac{\hbar^2}{2m} \frac{dv}{dt}= (E-V)\psi$$

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[15]:


def funcv(x, t):
    return (-2*m/(hbar**2))*(E-(V_0*x**2)/(a**2))*x


# In[16]:


a=1e-11
h=a*1e-4
V_0=50*(1.6e-22)
m=9.1e-31
hbar=6.626e-34/(2*math.pi)

psi=0
phi=1 #set to random value
x=-10*a
vec=[psi, phi]
psi_f=[]
E_ev=[]

for i in range(10000, 90000, 500):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-22)
    phi+=(h/2)*funcv(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv(psi, x)
        x+=h
    psi_f.append(psi)
    E_ev.append(i)
    


# In[17]:


plt.figure(figsize=(8,8))
plt.plot(E_ev, psi_f)
plt.plot(E_ev, np.zeros(len(E_ev)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# In[18]:


plt.figure(figsize=(8,8))
plt.plot(E_ev, psi_f)
plt.plot(E_ev, np.zeros(len(E_ev)))
plt.xlim(83000, 85000)
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# ### Guess solutions: 10.9, 38, 85 eV
# 
# Let us investigate to get more accurate solutions

# In[20]:


psi_f1=[]
E_ev1=[]

for i in range(10000, 11000, 5):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-22)
    phi+=(h/2)*funcv(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv(psi, x)
        x+=h
    psi_f1.append(psi)
    E_ev1.append(i)


# In[21]:


plt.figure(figsize=(8,8))
plt.plot(E_ev1, psi_f1)
plt.plot(E_ev1, np.zeros(len(E_ev1)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# In[25]:


E_ev2=[]
psi_f2=[]
for i in range(37500, 38500, 5):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-22)
    phi+=(h/2)*funcv(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv(psi, x)
        x+=h
    psi_f2.append(psi)
    E_ev2.append(i)


# In[33]:


plt.close()
plt.figure(figsize=(8,8))
plt.plot(E_ev2, psi_f2)
plt.plot(E_ev2, np.zeros(len(E_ev2)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# In[27]:


psi_f=[]
E_ev=[]
for i in range(84500, 85500, 5):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-22)
    phi+=(h/2)*funcv(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv(psi, x)
        x+=h
    psi_f.append(psi)
    E_ev.append(i)


# In[28]:


plt.figure(figsize=(8,8))
plt.plot(E_ev, psi_f)
plt.plot(E_ev, np.zeros(len(E_ev)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# The more accurate solutions are 10.9, 38.1, 85 eV.

# In[2]:


def funcv1(x, t):
    return (-2*m/(hbar**2))*(E-(V_0*x**4)/(a**4))*x


# In[3]:


a=1e-11
h=a*1e-4
V_0=50*(1.6e-26)
m=9.1e-31
hbar=6.626e-34/(2*math.pi)

psi=0
phi=1 #set to random value
x=-10*a
vec=[psi, phi]
psi_f1=[]
E_ev1=[]

for i in range(int(1e7), int(9e8), int(2e7)):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-26)
    phi+=(h/2)*funcv1(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv1(psi, x)
        x+=h
    psi_f1.append(psi)
    E_ev1.append(i)


# In[4]:


plt.figure(figsize=(8,8))
plt.plot(E_ev1, psi_f1)
plt.plot(E_ev1, np.zeros(len(E_ev1)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# Preliminary guesses are: 10, 40, 85 eV

# In[5]:


psi=0
phi=1 #set to random value
x=-10*a
vec=[psi, phi]
psi_f1=[]
E_ev1=[]

for i in range(int(8e7), int(1.2e8), int(1e6)):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-26)
    phi+=(h/2)*funcv1(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv1(psi, x)
        x+=h
    psi_f1.append(psi)
    E_ev1.append(i)


# In[6]:


plt.figure(figsize=(8,8))
plt.plot(E_ev1, psi_f1)
plt.plot(E_ev1, np.zeros(len(E_ev1)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# In[7]:


psi=0
phi=1 #set to random value
x=-10*a
vec=[psi, phi]
psi_f1=[]
E_ev1=[]

for i in range(int(37e7), int(38e7), int(0.5e6)):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-26)
    phi+=(h/2)*funcv1(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv1(psi, x)
        x+=h
    psi_f1.append(psi)
    E_ev1.append(i)


# In[8]:


plt.figure(figsize=(8,8))
plt.plot(E_ev1, psi_f1)
plt.plot(E_ev1, np.zeros(len(E_ev1)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# In[11]:


psi=0
phi=1 #set to random value
x=-10*a
vec=[psi, phi]
psi_f1=[]
E_ev1=[]

for i in range(int(84e7), int(85e7), int(0.5e6)):
    psi=0
    phi=1 #set to random value
    x=-10*a
    E=i*(1.6e-26)
    phi+=(h/2)*funcv1(psi,x)
    while(x<=10*a):
        psi+=h*phi
        phi+=h*funcv1(psi, x)
        x+=h
    psi_f1.append(psi)
    E_ev1.append(i)


# In[12]:


plt.figure(figsize=(8,8))
plt.plot(E_ev1, psi_f1)
plt.plot(E_ev1, np.zeros(len(E_ev1)))
plt.xlabel('Energy scale')
plt.ylabel('psi final value')
plt.title('graph for determination of allowed energies')


# The solutions are: 9.5, 37.7, 84.8 eV

# In[ ]:


a=1e-11
h=a*1e-2
V_0=50*(1.6e-22)
m=9.1e-31
hbar=6.626e-34/(2*math.pi)

psi_1=[]
psi_2=[]
psi_3=[]
X=[]

psi=0
phi=1 #set to random value
vec=[psi, phi]
x=-10*a
E=9.5*(1.6e-19)
phi+=(h/2)*funcv1(psi,x)
while(x<=5*a):
    psi+=h*phi
    phi+=h*funcv1(psi, x)
    x+=h
    if(x>-5*a):
        psi_1.append(psi)
        X.append(x)
    
psi=0
phi=1 #set to random value
vec=[psi, phi]
x=-10*a
E=37.7*(1.6e-19)
phi+=(h/2)*funcv1(psi,x)
while(x<=5*a):
    psi+=h*phi
    phi+=h*funcv1(psi, x)
    if(x>-5*a):
        psi_2.append(psi)
        X.append(x)
    
psi=0
phi=1 #set to random value
vec=[psi, phi]
x=-10*a
E=84.8*(1.6e-19)
phi+=(h/2)*funcv1(psi,x)
while(x<=5*a):
    psi+=h*phi
    phi+=h*funcv1(psi, x)
    if(x>-5*a):
        psi_3.append(psi)
        X.append(x)


# In[ ]:


plt.figure(figsize=(8,8))
plt.plot(X, psi_1, label='ground state')
plt.plot(X, psi_2, label='1st excited state')
plt.plot(X, psi_3, label='2nd excited state')
plt.xlabel('X')
plt.ylabel('wave function')
plt.title('anharmonic potential wave functions')
plt.legend() 


# In[ ]:


#normalisation

def int_trap(psi,h):
    sum=0
    for i in range(1,N):
        sum+=(h/2)*(psi[i-1]+psi[i])
    return sum
    

