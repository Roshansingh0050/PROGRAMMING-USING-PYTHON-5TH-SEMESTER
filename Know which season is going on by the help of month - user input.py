#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. March, April or May, the season is Spring.
# June, July or August, the season is Summer

a1 = "september"
a2 = "october"   # Declaring month of autumn........
a3 = "november"

w1 = "december"
w2 = "january"   # Declaring month of winter........
w3 = "february"

s1 = "march"
s2 = "april"    # Declaring month of spring
s3 = "may"

su1 = "june" 
su2 = "july"    # Declaring month of summer.......
su3 = "august"

a = input("enter the month :")

if  a == a1:
    print("This is season of Autumn...!!")
elif a == a2:
    print("This is season of Autumn...!!")
elif a == a3:
    print("This is season of Autumn...!!")
    
elif a == w1:
    print("This is season of Winter...!!")
elif a == w2:
    print("This is season of Winter...!!")
elif a == w3:
    print("This is season of Winter...!!")
    
elif a == s1:
    print("This is season of Spring...!!")
elif a == s2:
    print("This is season of Spring...!!")
elif a == s3:
    print("This is season of Spring...!!")
    
elif a == su1:
    print("This is season of Summer...!!")
elif a == su2:
    print("This is season of Summer...!!")
elif a == su3:
    print("This is season of Summer...!!")

else:
    print("Unable to Reach....!!!")





