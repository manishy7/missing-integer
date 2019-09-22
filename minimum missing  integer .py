#!/usr/bin/env python
# coding: utf-8

# In[14]:


A = 
q=len(A)
l=list()
A = list(dict.fromkeys(A))
for i in range(1,q+2):
    l.append(i)
print(l)
z=[i for i in A + l if i not in A or i not in l]
k=min(z)
if k>0:
    print(k)
elif k<=0:
    print(1)

    


# In[ ]:




