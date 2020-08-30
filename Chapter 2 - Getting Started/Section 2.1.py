#!/usr/bin/env python
# coding: utf-8

# We present partial solutions to problems in the textbook. Most of the time, we write pseudocode to solve a given algorithmic problem.

# ## 2.1.1 & 2.1.2

# In[25]:


def Insertion_Sort_Decreasing(A):
    
    length_array = len(A)
    
    for j in range(1,length_array):
        
        key = A[j]
        #We now insert A[j] into the correct place in the sequence
        
        i = j - 1
        
        #Simply change the < sign to the > sign to sort it in increasing order
        while i>=0 and A[i] < key:
            
            A[i + 1] = A[i]
            i = i - 1
            print(A)
            
        A[i + 1] = key
        print('Iteration number' + ' ' + str(j) + ' ' +  'has ended')
        print('---------------------------------')
    
    sorted_array = A
    return sorted_array


# In[26]:


#Let's test the insertion sort algorthim 

A = [31,41,59,26,41,58]
sorted_array =  Insertion_Sort_Decreasing(A)
print(sorted_array)


# ## 2.1.3

# In[47]:


def linear_search(A,v):
    boolean = None
    
    for index in range(len(A)):
        
        if A[index] == v:
            boolean = True
            print('Entry number' + ' ' + str(index + 1) + ' ' + 'contains the desired element.' + 
                  'The index is listed below.')
            return index
    
    boolean = False
    print('The list does not contain the desired element.')
    return boolean


# In[49]:


#We test the linear search algorithm

A = [31,41,59,26,41,58]

linear_search(A,10)

print('-----------------------------------------------------')

linear_search(A,31)


# The loop invariant in this code is:
# 
# At the start of each iteration of the for loop, the subbarray, $$A[0, ... , index - 1],$$ does not contain the desired element.

# ## 2.1.5

# In[245]:


#We define a function that computes the sum of two integers in binary form

def binary_sum(a,b):
    #Both integrs a and b are given in binary form. We implicitly assume that the lengths of the integers are
    # also the same.
    #We first convert b into integer form.
    
    n = len(a) #which is equal to len(b)
    b_int = 0
    
    for index in range(n):
        if int(b[index]) == 1:
            b_int = b_int + 2**(n - index)
    
    #We now add a to b_int and make a new variable c.
    #We iteratiively add the integer 1 to the binary a by looping over the length of a.
    #The idea is that at each iteration, we replace the first zero entry from the left by
    # a 1 and the other entries to the right of it (which are 1) by zero
    
    c = '0' + a
    
    #we firsr convert this string to a list
    
    temp_list = []
    
    for index in range(len(c)):
        
        temp_list.append(int(c[index]))
    
    for index in range(b_int):
        
        for i in range(len(temp_list)-1,-1,-1):
            
            if temp_list[i] == 0:
                
                temp_list[i] = 1
                
                if i != len(temp_list)-1:
                
                    for j in range(i + 1,len(temp_list),1):
                    
                        temp_list[j] = 0

                break
    
    c_updated = ' '
    
    for index in range(len(temp_list)):
        
        c_updated = c_updated + str(temp_list[index]) 
    
    return c_updated         


# In[246]:


#we test the binary sum algorithm

sum = binary_sum('11110','00001')
print(sum)


# In[ ]:




