#!/usr/bin/env python
# coding: utf-8

# In[56]:


price=int(input("enter price"))
tax=int(input("enter tax:"))
total=price+tax;
print("total=",total)


# In[57]:


price=int(input("enter price"))
tax=int(input("enter tax:"))
total=price+tax;
print("total=",total)


# In[58]:


is_student=True
in_class=True
in_ground=False
is_student and in_ground



# In[8]:


is_student=True
in_class=True
in_ground=False
is_student or in_ground


# In[9]:


x=[12,8,7,3]
y=[3,6,7,8]
z=x
print(x is z)
print(id(x))
print(id(y))
print(id(z))


# In[11]:


x=["hii","hello"]
y=["hii","hello"]
z=y
print(y is z)
print(x is not z)
print(x!=y)


# # membership operators

# In[12]:


word="hello"
print("e" not in word)
print("k" not in word)


# # bitwise operations

# In[13]:


print(bin(5))
print(bin(7))
print("10 & 11=",10&11)
print("10 | 11=",10|11)
print("10 ^ 11=",10^11)
print("~10=",~10)
print('10>>2=',10>>2)
print('10<<2=',10<<2)


# # if-else statement

# In[18]:


pas=33
marks=int(input("enter marks:"))
if(marks>pas):
    print("student passed the exam")
else:
    print("student failed")


# # class assignment(11-fri)

# In[28]:


service=int(input("enter years of service:"))
salary=int(input("enter the salary:"))
if(service>10):
    bonus=salary/10*100
elif(10<=service<=6):
    bonus=salary/8*100
else:
    bonus=salary/5*100


net=salary+bonus
print(net)


# # while loop

# In[33]:


n=int(input("enter n value:"))
sum=0
i=1
while(i<n):
    sum+=n 
    i=i+1
print("sum=",sum);


# # indexing and slicing

# In[38]:


text="hii there"
text[3:]


# In[39]:


text="hii there"
text[0:4]


# # reversing

# In[44]:


text="hii there"
text[::-1]


# In[48]:


text.replace("hii","hloo")
#replace hii with hloo
'hii there'
text.upper()
'hey hii'
text.upper()


# # list

# In[50]:


list1=["engineering_books","stories_books"]
list2=["business_books","logical_books"]
print("total books in library=",list1+list2);


# In[53]:


list1=["engineering_books","stories_books"]
list1.append("novels")
print(list1)


# # list sorting

# In[54]:


list1=[4,33,2,16,90,12,17]
ordered_list=sorted(list1)
print(ordered_list)


# In[ ]:




