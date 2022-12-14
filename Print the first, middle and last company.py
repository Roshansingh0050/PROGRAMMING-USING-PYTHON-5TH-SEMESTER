#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Print the first, middle and last company

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0]) # Printing the first company....


# printing the middle company.....
def mid_company(it_companies):
    length = len(it_companies) #finding list length.....
    
    middle = length//2 # Finding middle index of list
    
    print(it_companies[middle]) #printing the middle company of this list
    
mid_company(it_companies) #Function call to find middle company of this list....


# printing the last company.....
print(it_companies[-1])




    

