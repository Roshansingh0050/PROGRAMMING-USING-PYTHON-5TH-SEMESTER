#!/usr/bin/env python
# coding: utf-8

# In[134]:


# Change the dictionary to a list of tuples using items() method

student = {"First name":"Roshan", "Last name":"Singh","Gender":"Male","Age":20,"Marital status":"Single","Skills":"Programming","Address":"New Delhi"}

changingintotuple = list(student.items()) # changing the dictionary into tuple by using list method & as well as by using itmes() methods....

print(changingintotuple) # Printing the elements into list style.....as you can see the output :


# In[ ]:


# Convert a Dictionary into a List of Tuples Using list()
sample_dict = {'john': 30, 'nik': 32, 'datagy': 40}
list_of_tuples = list(sample_dict.items())
print(list_of_tuples)
# Returns: [('john', 30), ('nik', 32), ('datagy', 40)]

