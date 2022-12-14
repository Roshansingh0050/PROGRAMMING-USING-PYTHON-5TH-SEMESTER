#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Get the value of skills and check the data type, it should be a list

student = {"First name":"Roshan", "Last name":"Singh","Gender":"Male","Age":20,"Marital status":"Single","Skills":"Programming","Address":"New Delhi"}

print(student["Skills"]) # getting the value of skills........

a = student["Skills"] # Checking the data type ...... which is str = string......
type(a)
print(student) # Printing all the elements in the dictionary.....!!

