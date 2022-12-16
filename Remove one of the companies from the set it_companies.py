#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Remove one of the companies from the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]


it_companies.remove("Apple") # Removing Apple company from the it_companies by using remove() method.....!!

print(it_companies) # print the it_companies after removing one of the companies from the it_companies (set)

