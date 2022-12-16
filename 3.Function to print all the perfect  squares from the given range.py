#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a function that takes the number n and returns a list of all the perfect squares
# between 0 and n. A perfect square is a number s such that k2 = s for some integer k. For
# example, get perfect should return the list [0, 1, 4, 9, 16, 25, 36] def get_perfect_squares(n):

# Function to print all the perfect
# # squares from the given range

def perfectSquares(l, r): # creating function and taking two parameters ....to find out the perfect square from the given range.....!

	# For every element from the range
	for i in range(l, r + 1):

		# If current element is
		# a perfect square
		if (i**(.5) == int(i**(.5))):
			print(i, end=" ")

# Driver code
l = 2     # here we declared value in the l variable....
r = 24    # here we declared value in the r variable....

perfectSquares(l, r) # now we call the funtion by passing two parameters.....that we given or mentioned above

