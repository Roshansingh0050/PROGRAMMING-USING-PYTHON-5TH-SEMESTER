#!/usr/bin/env python
# coding: utf-8

# In[79]:


# Remove the middle IT company or companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

len(it_companies)//2 # first we find out the middle index value to remove the middle it company from this list...
# so we successfully found the middle index value of this list which is 3.

it_companies.pop(3) # after finding the middle index value....now we can remove the middle company by using pop() method by passing index parameter to it..
#Successfully remove the middle company from this list which is apple.

print(it_companies) # As the result ... apple company is not exists in this list....

    


# In[ ]:




