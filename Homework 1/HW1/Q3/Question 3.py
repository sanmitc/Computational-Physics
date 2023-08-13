#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

#Here the convention is taken to be -pi to +pi

def Polar(x,y):
    theta=0
    r=math.sqrt(x**2+y**2)
    if(x!=0):
        if(x>0 and y>0):
            theta=(180/math.pi)*(math.atan(y/x))
        if(x>0 and y<0):
            theta=(180/math.pi)*(math.atan(y/x))
        if(x<0 and y>0):
            theta=(180/math.pi)*(math.atan(y/x))+180
        if(x<0 and y<0):
            theta=(180/math.pi)*(math.atan(y/x))-180
    else:
        if(y>0):
            theta=90
        else:
            theta=-90
    return [r,theta]

print('x value')
x=float(input())
print('y value')
y=float(input())
print("r is:", Polar(x,y)[0])
print("theta is:", Polar(x,y)[1])

