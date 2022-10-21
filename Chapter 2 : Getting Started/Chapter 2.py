#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# # Section 2.1
# 
# ## Problem 1
# 
# We first implement the insertion sort algorithm that sorts a list in ascending order. We then test the algorithm on the list $[31,41,59,26,41,58]$.

# In[2]:


def Insertion_Sort(array):
    
    length = len(array)
    
    for j in range(1,length):
        
        key = A[j]
        
        #We now insert A[j] into the correct place in the sequence
        
        i = j - 1
        
        while i>=0 and array[i] > key:
            
            array[i + 1] = array[i]
            i = i - 1
            
        array[i + 1] = key
        
        print('Iteration #' + ' ' + str(j) + ' ' +  'has ended. The current array is:', array)
    
    sorted_array = A
    
    return sorted_array

#Let's now test the insertion sort algorthim 

A = [31,41,59,26,41,58]
sorted_array =  Insertion_Sort(A)


# ## Problem 2
# 
# 
# **Loop Invariant**: At the start of iteration  $j$  of the loop, the variable answer should contain the sum of the numbers from the subarray $A[1,...,j-1]$.
# 
# **Initialization**: At the start of the first iterstion, the sum of the numbers in an empty array is 0, and this is what answer has been set to.
# 
# **Maintenance**: Assume that the loop invariant holds at the start of iteration  $j$ . Then it must be that answer contains the sum of numbers in subarray  $A[1,...,j-1]$ . In the body of the loop we add  $A[j]$  to answer. Thus at the start of iteration  $j+1$ , answer will contain the sum of numbers in  $A[1,j]$, which is what we needed to prove.
# 
# **Termination**: When the for-loop terminates, the loop invariant gives: The variable answer contains the sum of all numbers in subarray $A[1,...,n]$. This is exactly the value that the algorithm should output, and which it then outputs. Therefore the algorithm is correct.
# 
# 
# 
# ## Problem 3
# 
# The insertion sort algorithm that sorts a list in descending order is given by chanding the inequality sign in the condition for the while loop. 
# 
# ## Problem 4
# 
# We first implement the linear search algorithm that that finds an element in a list.

# In[3]:


def linear_search(A,v):
    
    i = 0
    n = len(A)
    check = A[i]
    
    while i <= n-1 and check != v:
        
        i = i + 1
        
        if i <= n-2:
            
            check = A[i]
    
    if i == n:
        
        print('The list does not contain the desired element.')
        
        return None 
        
    else:
        
        print('Entry number ' + str(i + 1) + ' contains the desired element.')
        
        return i


# **Loop Invariant**: At the start of each iteration of the for loop, the sub-array, $A[1, ... , i-1]$, does not contain the desired element.
# 
# **Initialization**: At the start of the first iterstion, the sub-array $A[1,0]$ is empty. Therefore, the loop invariant is trivially satisfied.
# 
# **Maintenance**: Assume that the loop invariant holds at the start of iteration  $j$ . Then it must be that the subarray  $A[1,...,j-1]$ does not contain the desired element. In the body of the loop, we check if $A[i]$ contains the desired element. Assume the loop doesn't terminate. At the start of iteration $j+1$ since the loop has not been terminated, we must have that $A[j]$ wasn't the desired element. Hence $A[1,...,j]$ doesn't contain the desired element.
# 
# **Termination**: The loop terminates if either the algorithm finds an index $j$ such that $A[j]$ is the desired element or the algorithm hasn't found the element and it has reached the end of the array. In either case, our algorithm does exactly what was required, which means the algorithm is correct.

# ## Problem 4
# 
# We implement an algorithm that adds two numbers in binary form.

# In[3]:


def binary_sum(a,b):
    
    #Both integrs a and b are given in binary form. We first make the lengths of a and b the same
    
    n = len(a)
    m = len(b)
    
    if n < m:
        s
        a = '0'*(m-n) + a
        
    elif m < n:
        
        b = '0'*(n-m) + b
        
    #We now add the two numbers.
    
    c = ''
    carry = '0'
    
    for i in range(len(a)-1,-1,-1):
        
        if int(a[i]) + int(b[i]) == 0:
            
            c = carry + c
            
            if carry == '1':
            
                carry = '0'
                
        elif int(a[i]) + int(b[i]) == 1:
            
            carry = str(int(1 + int(carry)) % 2)
            c = carry + c
            carry = str(int(1 + int(carry)) % 2)
            
        
        elif int(a[i]) + int(b[i]) == 2:
            
            c = carry + c
            
            if carry == '0':
            
                carry = '1'

    c = carry + c
    
    return c


# # Section 2.2
# 
# ## Problem 1
# 
# The function $n^3/1000 - 100n^2 - 100n + 3$ belongs to the complexity class $\Theta ( n^3 ).$
# 
# ## Problem 2
# 
# We implement the **SELECTION SORT** algorithm. We search for elements using a linear search. We then test the algorithm on the list $[31,41,59,26,41,58]$.

# In[4]:


def Selection_Sort(array):
    
    length = len(array)
    
    for i in range(length-1):
        
        counter = i
        
        for j in range(i + 1, length):
            
            if array[j] < array[counter]:
                
                counter = j
        
        array[i], array[counter] = array[counter], array[i]
        
        print('Iteration #' + ' ' + str(i + 1) + ' ' +  'has ended. The current array is:', array)
        
    sorted_array = array
    
    return sorted_array


# In[5]:


#Let's now test the selection sort algorthim 

A = [31,41,59,26,41,58]
sorted_array = Selection_Sort(A)


# **Loop Invariant**: At the start of each iteration of the for loop, the subbarray, $A[0, ... , index - 1],$ contains the first $index$ elements in ascending order.
# 
# The best case running-time is $\Theta ( n )$ when the array is already sorted. The worst case running time is $\Theta ( n^2 )$ when the array is in reverse order.
# 
# ## Problem 3
# 
# Best case: $\Theta ( 1 )$,
# Worst case: $\Theta ( n )$, and
# Average case: $\Theta ( n )$.
# 
# ## Problem 4
# 
# We can modify any algorithm to have a best case time complexity by adding a special case. If the input matches this special case, return the pre-computed answer.
# 
# # Section 2.3
# 
# We first implement the MergeSort algorithm. 

# In[7]:


def Merge(A,p,q,r):
    
    n1 = q - p + 1
    n2 = r - q
    
    #We first populate two lists that contain the sorted subsequences A[p,...,q] and A[q+1,...,r]
    
    L = []
    R = []
    
    for index in range(n1):
        
        L.append(A[index + p])
        
    for index in range(n2):
        
        R.append(A[index + q + 1])
    
    #We now overwrite the A[p,..,q,...r] section of the list by comparing the 'top-most'
    #elements in the lists L and R and putting the smaller element in the corresponding
    #entry in A. If one of the list is fully exposed/no longer available, we simply put the 
    #remaining list's elements in the corresponding positions in A.
    
    i = 0
    j = 0
    
    for k in range(p,r+1):
        
        if i > n1-1:
            A[k] = R[j]
            j = j + 1
        
        elif j > n2-1:
            A[k] = L[i]
            i = i + 1
            
        elif L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
            
        else:
            A[k] = R[j]
            j = j + 1 
    
    sorted_array = A
    
    return sorted_array

#We now implement the MERGE-SORT algorithm.

def Merge_Sort(A,p,r):
    
    if p == r:
        
        return A
    
    if p < r:
        
        q = math.floor((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        sorted_array = Merge(A,p,q,r)
    
    return sorted_array


# ## Problem 6
# 
# 
# We implement the binary search algorthim.

# In[55]:


def Binary_Search(S,start,end,v):
    
    #We first sort A using merge sort
    n = end-start+1 
    A = Merge_Sort(S,start,end)   
    
    if n == 1:
        
        index = None
        
        if A[start] == v:
            
            index = start
            print('Entry number ' + str(index + 1) + ' contains the desired element.')
            return index
        
        else:
            
            print('The list does not contain the desired element.')
            return index
    
    else:
       
        middle = math.floor((start+end)/2)
        
        if A[middle] == v:
            
            index = middle
            print('Entry number ' + str(index + 1) + ' contains the desired element.')
            return index
        
        elif A[middle] > v:
            
            index  = Binary_Search(A,start,middle-1,v)
            return index
     
        else:
            index =  Binary_Search(A,middle + 1,end,v)
            return middle+index     


# The recursion relation for the binary search algorthm is given by,
# $$
# T(n) = T(n/2) + \Theta (1).
# $$
# The solution is $\Theta(\lg n)$ by the master method.

# ## Problem 8

# In[23]:


def sum_in_set(S,x):
    
    #We first sort the set S using merge sort
    n = len(S)
    Sorted_S = Merge_Sort(S,0,n-1)
    
    #Now for each element s in Sorted_S, we check whether s - x is in Sorted_S using binary search
    
    for s in Sorted_S:
        
        index = Binary_Search(Sorted_S,0,n-1,x-s)
        
        if index != None:
            
            print('The set contains the integers', s, 'and', x-s, 'that sum to', x)
            return s, x-s
    
    print('The set does not contain two integers that sum to', x)
    
    return None

