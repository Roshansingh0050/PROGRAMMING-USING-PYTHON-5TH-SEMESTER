#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Delete the sets completely

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]


del it_companies # deleting it_companies by using del keyword....
del A # deleting set a
del B # deleting set b
del age # deleting set age....by using del keyword

print(it_companies)
print(A)
print(B)
print(age)   # as the result will be an error : name 'it_companies' is not defined
             # beacause all sets are deleted completely......




