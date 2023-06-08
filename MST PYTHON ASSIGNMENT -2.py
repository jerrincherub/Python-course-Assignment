#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.Write an interactive Python Program to implement following “Guess Game”


# In[2]:


import random
n = random.randrange(1,10)
guess = int(input("Enter any number between 1 and 10: "))
while n!= guess:
    if guess < n:
        print("Too low! try again")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high! try again")
        guess = int(input("Enter number again: "))
    else:
      break
print("Congratulation! You guessed the number correctly!")


# In[ ]:


2.Write a program to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N.


# In[9]:


N = int(input("Enter a number: "))

factorial = 1

if N < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif N == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,N + 1):
       factorial = factorial*i
   print("The factorial of",N,"is",factorial)


# In[ ]:


Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.Given L, N, W and H as input, write a program to print appropriate text as output.


# In[2]:


L=int(input("Enter the length of the photo "))
N=int(input("Enter the number of photos to upload "))
while N>0:
  W=int(input("Enter the width of the photo "))
  H=int(input("Enter the Height of the photo ")) 

  if  W<L or H<L:   
    print("UPLOAD ANOTHER")
  elif W>=L and  H>=L and W==H:
     print("ACCEPTED")
  elif W>=L and  H>=L and W!=H:   
    print("CROP IT")    
  N= N-1
     


# In[ ]:




