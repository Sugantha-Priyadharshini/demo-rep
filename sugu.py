
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


a=9
b=5
c=a+b
print(c)


# In[3]:


print c,"hello"


# In[4]:


print(c,"hello")


# In[5]:


print("hello \n" *3)


# In[18]:


import matplotlib.pyplot as plt
plt.plot([2,5,8,4,],[7,8,9,10],[9,6,5,4])
plt.title("garph")
plt.xlabel("xaxis")
plt.ylabel("yaxis")
plt.show()


# In[15]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16],'r^')
plt.axis([0, 6, 0, 20])
plt.show()


# In[32]:


import matplotlib.pyplot as plt
vr=[1,2,3,4]
var=[6.1,5.2,6.4,4.4]
plt.plot(vr,var,'r--')
plt.title("Height of the students")
plt.xlabel("Students")
plt.ylabel("Height")
plt.show()
plt.savefig('D:/su.png')

