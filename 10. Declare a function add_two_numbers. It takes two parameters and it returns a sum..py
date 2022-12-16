#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 10. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_num(a,b):#function for addition of two numbers.......
    sum=a+b;
    return sum; #return value........which is sum
num1=int(input("input the number one: "))#input from user for num1........
num2=int(input("input the number one :"))#input from user for num2........

print("The sum is",add_num(num1,num2))#call the function.....and getting the final result of input which is given by user.......

