#!/usr/bin/env python
# coding: utf-8

# ## Lesson 9 - Command Line Parameters

# In[ ]:


## this is my calculator

def add(n1,n2):
    return n1+n2

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

print("Result:",add(x,y))

