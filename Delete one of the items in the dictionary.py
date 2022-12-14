#!/usr/bin/env python
# coding: utf-8

# In[113]:


# Delete one of the items in the dictionary
student = {"First name":"Roshan", "Last name":"Singh","Gender":"Male","Age":20,"Marital status":"Single","Skills":"Programming","Address":"New Delhi"}

student.pop("Gender") # Deleting one of the items in this dictionary ....which is Gender 
                      # key(Gender)& it's value are removed from this dictionary....
    
    
print(student) # printing the dictionary after deleting ..... Gender

