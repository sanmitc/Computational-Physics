#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
def B_E(A,Z):
    a_1=15.67
    a_2=17.23
    a_3=0.75
    a_4=93.2
    if(A%2==1):
        a_5=0.0
    elif(A%2==0 and Z%2==0):
        a_5=12.0
    else:
        a_5=-12.0
    E=a_1*A -a_2*(A**(2/3))-a_3*(Z**2)*(A**(-1/3))-a_4*((A-2*Z)**2/A)+a_5*(A**(-1/2))
    return E
print("Mass Number:")
A=int(input())

print("Atomic Number:")
Z=int(input())

Energy=B_E(A,Z)
print("Binding energy", Energy)

per_n= (Energy/float(A))
print("Bindin energy per numcleon", per_n)


# In[3]:


#part c

Z=int(input())

def max_E_A(Z):
    A=Z
    max_E=0
    for i in range(Z, 3*Z+1):
        if(max_E>=(B_E(i,Z)/i)):
            pass
        else:
            max_E=(B_E(i,Z)/i)
            A=i
    print("maximum binding energy per nucleon:", max_E)
    print("the mass number is:", A)
max_E_A(Z)


# In[4]:


#part d
print('Pleae enter 100. ')
Num=int(input())

def max_E_A(Z):
    A=Z
    max_E=0
    for i in range(Z, 3*Z+1):
        if(max_E>=(B_E(i,Z)/i)):
            pass
        else:
            max_E=(B_E(i,Z)/i)
            A=i
    return [A,max_E]

def get_max(Num):
    Z=0
    max=0
    ar=[]
    A=0
    for i in range(1,101):
        if(max>=max_E_A(i)[1]):
            A=max_E_A(i)[0]
            ar.append(A)
            pass
        else:
            max=max_E_A(i)[1]
            ar.append(max_E_A(i)[0])
            Z=i
    return [Z,ar]
        
Z_max=get_max(Num)[0]
ar=get_max(Num)[1]
print('The appropriate z is:', Z_max)
print('all the stable values of A is:', ar)


# In[ ]:




