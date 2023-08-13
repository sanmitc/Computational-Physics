#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:



import numpy as np
import matplotlib.pyplot as plt
import math

#Put the coefficeints of the equation in this order
def roots1(a,b,c):
    D=math.sqrt(b**2-4*a*c)
    root1=(-b+D)/(2*a)
    root2=(-b-D)/(2*a)
    return [root1, root2]

print('the roots of the equations are(by 1st method)', roots1(0.001, 1000, 0.001))

def roots2(a,b,c):
    D=math.sqrt(b**2-4*a*c)
    root1=(2*c)/(-b-D)
    root2=(2*c)/(-b+D)
    return [root1, root2]

a=0.001
c=0.001
b=1000
print(math.sqrt)
print('the roots of the equations are(by 2nd method)', roots2(0.001, 1000, 0.001))


# Part c

# From the stucture of the equation we know that one root is very large in absolute terms and the other is very small. The correct roots are, both negative. In this case $D\approx b$, So, in the first case, -b+D case is inducing the round off error. So, we can say the second root in the 1st method is correct, but the 1st root is not. So, we take the 2nd root of the 1st method.
# 
# Similarly, the 1st root of teh second method is acceptable, because the denomicator has (-b-D) with no round off relative errors. Now, we have the roots as: (-999999.999999, -1.000000000001e-06). The new modified funciton should look like:
# 
# 

# In[ ]:


def roots(a,b,c):
    D=math.sqrt(b**2-4*a*c)
    if(b<0):
        root1=(-b+D)/(2*a)
        root2=(2*c)/(-b+D)
    else:
        root1=(-b-D)/(2*a)
        root2=(2*c)/(-b-D)

    return [root1, root2]



print('the roots of the equations are:', roots(0.001, 1000, 0.001))

#It satisfies the result

