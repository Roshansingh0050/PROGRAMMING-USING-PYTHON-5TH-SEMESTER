#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Insert multiple IT companies at once to the set it_companies


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.update(['Wipro','ISRO','VI']) # successfully ...!! Inserted multiple it companies to it_companies by using update() method...

print(it_companies) # Printing updated set it_companies.....!!! after adding multiple companies......

