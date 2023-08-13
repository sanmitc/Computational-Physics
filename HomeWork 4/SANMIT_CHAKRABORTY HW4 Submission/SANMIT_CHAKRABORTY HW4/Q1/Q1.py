#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:


#part a
def square(x, N, val):
  if(x<N/2):
    return val
  if(x>= N/2):
    return -val

  

#defining a sequence of values
N=1000
val=5


def f(x):
  return square(x, N, val)



x_ft=ft(f, N)

x=np.linspace(0, N, N+1)
f=[f(y) for y in x]


plt.figure(figsize=(10,10))
plt.plot(x, x_ft)
plt.xlabel('coefficient number')
plt.ylabel('amplitude')
plt.title('Fourier de-composition for square wave')
plt.show()




# In[ ]:


#What is happening in the edges? The soluid colour suggests rapid oscillation. We confirm that by changing the x range.


plt.figure(figsize=(10,10))
plt.plot(x, x_ft)
plt.xlabel('coefficient number')
plt.ylabel('amplitude')
plt.xlim(0, 50)
plt.title('Fourier de-composition for square wave')
plt.show()


# In[ ]:


#part-b



def fs(x):
  return x

N=1000
x2_ft=ft(fs,N)

plt.figure(figsize=(10,10))
plt.plot(x, x2_ft)
plt.xlabel('coefficient number')
plt.ylabel('amplitude')
plt.title('Fourier de-composition for saw-tooth wave')
plt.show()




# In[ ]:




def f_ms(x, M, N):
  return math.sin(math.pi*x/N)*math.sin(M*math.pi*x/N)

M=20
N=1000

def f3(x):
  return f_ms(x, M, N)


x3_ft=ft(f3, N)


plt.figure(figsize=(10,10))
plt.plot(x, x3_ft)
plt.xlabel('coefficient number')
plt.ylabel('amplitude')
plt.title('Fourier de-composition for modulated sine wave')
plt.show()


# **Comments:** We can see in all the cases, the graph is symmetric across the midpoint, i.e. x=500 , as taught in the class. The larger coefficients are all concentrated in the numbers near to 1000 and 0, sugestuing that a relatively small number of fourier waves coming from first few coefficients are enough to specify the curve to a considerable degree. 
