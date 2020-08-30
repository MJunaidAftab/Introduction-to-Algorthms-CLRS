#!/usr/bin/env python
# coding: utf-8

# We present partial solutions to problems in the textbook. Most of the time, we write pseudocode to solve a given algorithmic problem.

# # Section 2.2

# ## 2.2.1
# 
# $\Theta ( n^3 ).$
# 
# ## 2.2.2

# In[16]:


#We implement the SELECTION SORT algorithm

def Selection_Sort(A):
    
    n = len(A)
    
    for index in range(len(A)-1):
        
        counter = index
        
        for j in range(index + 1, len(A)):
            
            if A[j] < A[counter]:
                
                counter = j
        
        A[index], A[counter] = A[counter], A[index]
        print(A)
        print('-------------------------------------------')
        
    return A    


# In[17]:


#We illusrate the selection sort algorithm
A = [31, 41, 10, 8, 99, 25, 5, 9, 44, 25]
sorted_array = Selection_Sort(A)
#print(sorted_array)


# For a discussion of the time complexity of the algorithm, see the Google Drive.

# # Section 2.3

# ## 2.3.2

# We first write the MERGE function which merges two sorted sequences. The functons takes as input an array, A, and three indicies, p,q and r, such that p is less than oe equal to q and q is less than r. The time complexity of this alogirthm is of order $\Theta ( n  ),$ where $n = r - p + 1$.

# In[18]:


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
    #elements in the lists l and R and putting the smaller element in the corresponding
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
    
    return A        


# In[19]:


#We now implement the MERGE-SORT algorithm.

import math

def Merge_Sort(A,p,r):
    
    if p == r:
        
        return A
    
    if p < r:
        
        q = math.floor((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merged_List = Merge(A,p,q,r)
    
    return Merged_List


# In[20]:


#We now analyze the merge sort algorithm.
A = [1,7,9,3]
B = Merge_Sort(A,0,3)
print(B)


# ## 2.3.4
# 
# We implement insertion sort recursively.

# In[21]:


def Insertion_Sort_Recursive(A):
    #Here n is the length of the array
    n = len(A)
    
    if n == 1:
        
        return A
    
    else:
        
        new_array = A[0:n-1]
        last_element = A[n-1]
        sorted_new_array = Insertion_Sort_Recursive(new_array)
        
        #We now 'merge' the sorted subarray A[1,...,n-1] and the one element subarray A[n]
        
        i = n - 2
        sorted_new_array.insert(i + 1, '')
       
        while i >=0 and sorted_new_array[i] > last_element:
        
            sorted_new_array[i + 1] = sorted_new_array[i]
            i = i - 1
        
        sorted_new_array[i+1] = last_element
        
        return sorted_new_array        


# In[9]:


#We test this algorthim now
B = [5,55,3,1,77,55,4,8,33,21]
D = Insertion_Sort_Recursive(B)
print(D)


# The recursion relation for this algorthm is given by,
# $$
# T(n) = T(n-1) + \Theta (n).
# $$
# The solution is $\Theta(n^2)$. Make a recursion tree.

# ## 2.3.5
# 
# We implement the binary search algorthim. We implicitly assume that the sequence is sorted.

# In[52]:


def Binary_Search(S,start,end,v):
    
    #We first sort A using merge sort
    n = end-start+1 #This is the length of A over which we are searching
    
    A = Merge_Sort(S,start,end)   
    
    if n == 1:
        
        Boolean = None
        index = None
        
        if A[start] == v:
            
            index = start
            Boolean = True
            return index,Boolean
        
        else:
            
            Boolean = False
            index = None 
            return index,Boolean
    
    else:
        middle = math.floor((start+end)/2)
        
        if A[middle] == v:
            index = middle
            Boolean = True
            return index,Boolean
        
        elif A[middle] > v:
            index,Boolean = Binary_Search(A,start,middle-1,v)
            return index,Boolean
     
        else:
            index,Boolean =  Binary_Search(A,middle + 1,end,v)
            return index,Boolean
        
#Here the index returned is in the new sorted list        


# In[44]:


#We test this algorthim now
A = [33,22,12,44,122,9822992,3,1,9,3,66,3]
n = len(A)
Binary_Search(A,0,n-1,122)


# The recursion relation for the binary searc algorthm is given by,
# $$
# T(n) = T(n/2) + \Theta (1).
# $$
# The solution is $\Theta(\lg n)$ by the master method.

# ## 2.3.7

# In[12]:


def Binary_Element_As_Sum_In_Set(A,start,end,x):
    #We take the bases cases to be 2 and 3 so we don't get down to the case where's there's only
    #one element in the subdivided set
    n = end - start + 1 #Here we are worried about the number of elements in the set and not the indicies! Hence the +1
    Boolean = None
    
    if n == 2:
        if x == A[start] + A[start + 1]:
            Boolean = True
            return Boolean
        else:
            Boolean = False
            return Boolean
        
    elif n == 3:
        if x == A[start] + A[end] or x == A[start] + A[start + 1] or x == A[start + 1] + A[end]:
            Boolean = True
            return Boolean
        else:
            Boolean = False
            return Boolean
        
    else:
        middle = math.floor((start + end)/2)
        Boolean1 = Binary_Element_As_Sum_In_Set(A,start,middle,x)
        Boolean2 = Binary_Element_As_Sum_In_Set(A,middle+1,end,x)
        
        if Boolean1 == True or Boolean2 == True:
            Boolean = True
            return Boolean
        
        else:
            #We now add elements from the two half sets and see if x is in one of those sets
            for i in range(start,middle + 1):
                for j in range(middle + 1, end + 1):
                    if x == A[i] + A[j]:
                        Boolean = True
                        return Boolean
                    
            Boolean = False
            return Boolean


# In[13]:


#We test this algorthim now
A = [1,3,11,55,77,10]
Binary_Element_As_Sum_In_Set(A,0,5,22)


# <font color='red'>THIS IS WRONG!!! We iterated over both the sub-lists using two for loops, which would give a quadratic time complecity. The trick here is to first SORT the list. Sort the list using merge sort. For each element in the list, x, do a binary search for s - x. If it exisits, good; if not, move ahead.  </font>
# 
# We implement the algorithm correctly below.

# In[50]:


def sum_in_set(S,x):
    
    #We first sort the set S using merge sort
    n = len(S)
    
    Sorted_S = Merge_Sort(S,0,n-1)
    
    #Now for each element s in Sorted_S, we check whether s - x is in Sorted_S using binary search
    
    for s in Sorted_S:
        
        index, Boolean = Binary_Search(Sorted_S,0,n-1,x-s)
        
        if Boolean == True:
            
            return s, x-s
        
    Boolean = False
    
    return Boolean


# In[56]:


S = [6,2,3,4,5,1,54]
x = 55
print(sum_in_set(S,x))

