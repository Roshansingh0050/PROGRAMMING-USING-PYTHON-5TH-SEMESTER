#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 11.Area of a circle is calculated as follows: area = π x r x r. Write a function that
# calculates area_of_circle.

from math import pi # from math module we are importing pi which works or equals to π .....
r = float(input ("Input the radius of the circle : ")) # getting user input value as radius....we're going to find the area of the circle by the radius....
# it will take radius as float data type. for example - 3.4
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) # printing the area of the circle with mentioned strings....

