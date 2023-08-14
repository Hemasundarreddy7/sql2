#!/usr/bin/env python
# coding: utf-8

# In[7]:


marks=[23,7,90,45,65,2,77]
marks.sort()
print(marks)


# In[8]:


marks=[23,7,90,45,65,2,77]
marks.sort(reverse=True)
print(marks)


# In[14]:


list1=["hii","hello","yoo"]
list1[1]


# In[16]:


list1.append("how r u")
print(list1)


# In[21]:


list1.insert(2,"who")
print(list1)


# In[23]:


list2=[24,4,56,76,53]
max(list2)
min(list2)


# # sort and negative indexing

# In[27]:


list2.sort()
print(list2)
text="hii there"
text[::-1]


# In[33]:


#counting 
list2=[24,4,56,76,53]
len(list2)


# In[34]:


marks=[23,7,90,45,65,2,77]
marks.sort(reverse=True)
print(marks)


# In[36]:


#clear the list
list2=[24,4,56,76,53]
list2.clear()
print(list2)


# In[37]:


text="hii there"
text[3:]


# # membership

# In[38]:


nums=[1,3,4,32,67,84,34]
item=32
item in nums


# In[39]:


nums=[1,3,4,32,67,84,34]
item=322
item in nums


# In[41]:


nums=[1,3,4,32,67,84,34]
for i in nums:
    print(i)


# # counting a perticular element

# In[42]:


nums=[1,3,4,32,67,84,34,3,3,56,3]
nums.count(3)


# # extend a list and return index

# In[45]:


list1=["engineering_books","stories_books"]
list2=["business_books","logical_books"]
list1.extend(list2)
print(list1)
list1.index("logical_books")


# # insert and del at specific position

# In[47]:


list1=is["engineering_books","stories_books"]
list1.insert(1,"thinkbig_books")
print(list1)


# In[52]:


list1=["engineering_books","stories_books"]
list1.remove("engineering_books")
print(list1)


# # reversing a list

# In[57]:


l=[23,43,78,90,54,3]
l.reverse()
print(l)


# In[70]:


v=[30,45,80,7,12]
v.sort(reverse=True)
print("sorted list=:",v)
v.reverse()
print("revesed list is:",v)


# In[66]:


v=[30,45,80,7,12]
v[::-1]


# In[67]:


l2=[15,2,6,8,12]
l2[::-1]


# In[72]:


l2=[15,2,6,8,12]
l2.sort(reverse=True)
l2


# In[82]:


list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list3)
list3[-3:-1]


# In[ ]:




