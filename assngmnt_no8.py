#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no 1
#program to add two matrices
A =  [ [1, 1, 1],
     [1, 1, 1],    
     [1, 1, 1]]

B =   [[1, 2, 3],
      [4, 5, 6],   
      [7, 8, 9]]

sum = [[0, 0, 0],
      [0, 0, 0],   
      [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        sum[i][j] = A[i][j] + B[i][j]
        
for num in sum:
    print(num)


# In[2]:


#Answer no 2
#program to multiply two matrices
import numpy
matrix_1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix_2 = [[7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]]

result = numpy.dot(matrix_1 , matrix_2)
print(result)


# In[4]:


#Answer no 3
#program to transpoose matrices
num = 4
def transpose(A,B):
    for i in range(num):
        for j in range(num):
            B[i][j] = A[i][j]
            
A = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

B = A[:][:]
transpose(A,B)
print("result matrix is")
for i in range(num):
    for j in range(num):
        print(B[i][j]," ",end='')
    print()


# In[10]:


#Answer no 4
#program to sort words in alphabetic order
def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
     
      W[i]=W[i].lower() 
  S = sorted(W)
  print(' '.join(S))
 
S = "the Quick brown fox jumPs over the lazY Dog"
 

Func(S)


# In[11]:


#Answer no 5
#program to remove punctuation from string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!! , he said --- and went"
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
        
print(no_punct)


# In[ ]:




