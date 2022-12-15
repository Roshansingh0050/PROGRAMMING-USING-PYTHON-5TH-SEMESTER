#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon'] # list contain some fruits....as you can see 

a = str(input("Enter the name of fruit to know exist or not :")) # taking user input ..... to know fruit is present in the list or not....

if a in fruits:
    print("That fruit already exist in the list...")  # using if else statement to know the existance of the fruit .....
else:
    print("Not Exist.....!!")
    
print(fruits) # after check.....printing the list of fruits.....
    
        
a = str(input("Add the fruit if not exist in the list :")) # adding fruits to the list....
fruits.append(a)
print("Successfully added...!!")
print(fruits) # after successfully added....printing the updated & modified list of fruits......


    


# In[ ]:




