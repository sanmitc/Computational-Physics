#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
#part a
def binomial(n,k):
    if(k==0):
        return 1
    else:
        prod1=1
        prod2=1
        for i in range(1,k+1):
            prod1*=(n-i+1)
            prod2*=i
        result=prod1/prod2
    return int(result)


            


# In[ ]:


#part b
Num=20
for i in range(1,Num+1):
    print('\n')
    for j in range(0,i+1):
        a=binomial(i,j)
        print(a, end=" ")


# In[ ]:


#part c

def prob(n,k):
    den=2**n
    p=binomial(n,k)/den
    return p

n=100
k=60
ans1=prob(n,k)

ans2=0
for i in range(60,101):
    ans2+=prob(100,i)

print("probability of 60 heads:", ans1)
print("probability of 60 or more heads", ans2)

