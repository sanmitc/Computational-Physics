#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def prime(Num):
    arr=[2]
    for i in range(3,Num+1):
        k=int(math.sqrt(i))
        n=len(arr)
        counter=0
        for j in range(n):
            if(arr[j]>k):
                break
            elif(i%arr[j]==0):
                counter=1
                break
        if(counter==0):
            arr.append(i)
        #print(i, j)
    return arr

N=float(input())
N=int(N)
print("",prime(N))
print(len(prime(N)))

