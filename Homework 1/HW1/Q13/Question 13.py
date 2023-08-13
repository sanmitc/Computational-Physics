#!/usr/bin/env python
# coding: utf-8

# In[3]:


#part a
import matplotlib.pyplot as plt

t = []
ss = []

file=open(r"sunspots.txt")


for rows in file:
        rows=rows.split('\t')
        t.append(int(rows[0]))
        ss.append(float(rows[1].strip()))
        #print(rows[1])
        
        
plt.bar(t, ss,color='k')
plt.title('Time variation of sunspot occurence')
plt.xlabel('sunspot no.')
plt.ylabel('no. of month')
plt.show()


# In[4]:


#part b

import matplotlib.pyplot as plt

t_n = []
ss_n = []

file=open(r"sunspots.txt")

i=0
for rows in file:
    if(i>1000):
        break
    else:
        rows=rows.split('\t')
        t_n.append(int(rows[0]))
        ss_n.append(float(rows[1].strip()))
        i+=1
        #print(rows[1])
              
plt.bar(t_n, ss_n,color='k')
plt.title('Time variation of sunspot occurence')
plt.xlabel('sunspot no.')
plt.ylabel('no. of month')
plt.show()


# In[8]:


# part c
import statistics as stat

ss_mean=[]

for i in range(0,len(ss)):
    if(i>1000):
        break
    elif(i<5):
        ss_mean.append(stat.mean(ss_n[:i+6]))
    else:
        ss_mean.append(stat.mean(ss_n[i-5:i+6]))

plt.bar(t_n, ss_n,color='b')
plt.bar(t_n,ss_mean, color='g')
plt.title('Time variation of sunspot occurence(moving average)')
plt.xlabel('sunspot no.')
plt.ylabel('no. of month')
plt.show()


# In[ ]:




