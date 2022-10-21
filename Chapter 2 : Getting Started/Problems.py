#!/usr/bin/env python
# coding: utf-8

# # Problems
# 
# ## Problem 1
# 
# ### Part a
# 
# Recall that for insertion sort if the length of the list is $m$, the time complexity of the algorithm is $\Theta (m^2)$ in worst-case. If we sort sorts $n/k$  lists of length $k$ using insertion sort, each list is sorted in time $\Theta (k^2)$ in worst-case. Since there are a total of $n/k$ lists, the time complexity of the algorithm is $n/k \; \Theta (k^2) = \Theta (n/k)$ in worst-case.
# 
# ### Part b
# 
# We have $n/k$ sorted sublists each of length $k$. To merge these $n/k$ sorted sublists to a single sorted list of length $n$, we take $2$ sublists at a time and continue to merge them. This will involve in $ \Theta ( \lg(n / k)  )$ merge steps. We compare a total of $n$ elements in each step. Therefore, the worst-case time $ \Theta (n \lg(n / k))$.
# 
# ### Part c
# 
# Using the arguments above, the solution to this recurrence relation is,
# 
# $$
# T(n) = \Theta (nk + n\lg(n/k)).
# $$
# 
# Standard merge sort runs in $\Theta (n \lg n)$ time. To have the modified algorithm have the same running time as standard merge sort, we'd need to have $\Theta (n \lg n) = \Theta (nk + n\lg(n/k))$, which is equivalent to the condition,
# 
# $$
# \lim_{n \rightarrow \infty} \frac{nk(n) + n\lg(n/k(n))}{n \lg n} = \lim_{n \rightarrow \infty} \frac{k(n) + \lg(n/k(n))}{\lg n} 
# = \lim_{n \rightarrow \infty} \frac{k(n) + \lg n - \lg k(n)}{\lg n} = \lim_{n \rightarrow \infty} 1 + \frac{k(n)}{\lg n}  - \frac{\lg k(n)}{\lg n},
# $$
# 
# to be finite and neither $0$ nor $+ \infty$. A sufficient condition is that $k(n) = \Theta ( \lg n)$ or $o(\lg n)$ for that matter.
# 
# ### Part d
# 
# Choose $k$ be the largest length of sublist on which insertion sort is faster than merge sort.
# 
# # Problem 2

# In[1]:


def Bubble_Sort(A):
    
    n = len(A)
    
    for i in range(0,n-1):
        
        for j in range(n-1,i,-1):
            
            if A[j] < A[j-1]:
                
                A[j], A[j-1] = A[j-1], A[j]
                
    return A


# **Loop Invariant:**
# 
# At the start of each of the round of the outer iteration, the subarray $A[i,...,n]$ consists of the elements originally in  $A[i,...,n]$ before entering the loop but possibly in a different order. Additionally, $A[1,...,i-1]$ is correctly sorted with the largest element in ths list being the smallest element from the list  $A[i,...,n]$ obtained from the PREVIOUS iteration.
# 
# The time complexity of this algorithm is given by the expression (here we use the pseudocode written in the book),
# 
# $$
# T(n) = \Theta \Bigg (  \sum_{i = 1}^{n-1} \sum_{j = i + 1}^{n} t_{ij} \Bigg ) = \Theta \Bigg (  \sum_{i = 1}^{n-1} \sum_{j = i + 1}^{n} t_{ij} \Bigg ),
# $$
# 
# where $t_{ij}$ is either $0$ or $1$ depeding on whether the if statement is executed. We analyze the worst case running time of the algorithm. We get.
# 
# $$
# \begin{align}
# T(n) & = O \Bigg ( \sum_{i = 1}^{n-1} \sum_{j = i + 1}^{n} 1 \Bigg ), \\
#      & = O \Bigg ( \sum_{i = 1}^{n-1} n - i \Bigg ), \\
#      & = O \Bigg ( \sum_{k = 1}^{n-1} k \Bigg ), \\
#      & = O \Bigg ( \sum_{k = 1}^{n - 1} k \Bigg ), \\
#      & = O ( n^2 ).
# \end{align}
# $$

# # Problem 3
# 
# ### Part a

# In[12]:


def Horners_Rule(A):
    
    #A contains the list of coefficients
    
    y = 0
    
    for i in range(n,-1,-1):
        y = A[i] + x*y


# The running time is $\Theta (n)$.
# 
# ### Part b

# In[2]:


def Naive_Horner(A):
    
    y = 0
    
    for i in range(0,n+1):
        
        z = A[i]
        
        for j in range(0,i):
            
            z = z*x
        
        y = y + z


# The running time of the algorithm is $\Theta(n^2)$.

# # Problem 4
# 
# ### Part a
# 
# The inversions are $(1, 5), (2, 5), (3, 4), (3,5), (4,5)$.
# 
# ### Part b
# 
# The array $[n, n-1, n-2, ... , 3, 2, 1]$ has the most inversions. It has a total of $n(n-1)/2$ inversions.
# 
# ### Part c
# 
# The running time of insertion sort is of the order of magnitude of the number of inversions in the input array. The reason is that the time complexity of insertion sort is determined by i) the number of items in the list and ii) the number of adjacent inverted elements in one of the multiple subarrays we consider while placing each element in its right place in the list. But that's what exactly measures the number of inversions in an array.
# 
# ### Part d

# In[5]:


def Merge_Number_Of_Inversions(A,p,q,r,Inversions_Left,Inversions_Right):
    
    n1 = q - p + 1
    n2 = r - q
    
    Inv_L = Inversions_Left
    Inv_R = Inversions_Right
    
    Inversions = Inv_L + Inv_R
    
    #We first populate two lists that contain the subsequences A[p,...,q] and A[q+1,...,r] for which we have
    #computed the number of inversions AND SORTED
    
    L = []
    R = []
    
    for index in range(n1):
        L.append(A[index + p])
        
    for index in range(n2):
        R.append(A[index + q + 1])
    
    #We now compute the number of inversions by taking pairs of indicies such that elements with the first 
    #index come from the first (L) list and elements from the second list come from the second (R) list.
    #if $L[i] < L[j]$ we don't increase the inversion number.
       
    
    i = 0
    j = 0
    
    for k in range(p,r+1):
        
        if i > n1-1:
            A[k] = R[j]
            j = j + 1
        
        elif j > n2-1:
            A[k] = L[i]
            i = i + 1
            
        elif L[i] > R[j]:
            A[k] = R[j]
            j = j + 1
            Inversions = Inversions + (n1 - i)
            
        else:
            A[k] = L[i]
            i = i + 1             
    
    return Inversions


# In[8]:


#We now implement the MERGE-INVERSIONS algorithm.

import math

def Merge_Inversions(A,p,r):

    n = r - p + 1
    Inversions = 0
    
    if n == 1:
        
        Inversions = 0
        
        return Inversions
    
    if n == 2:
        
        if A[p] > A[p+1]:
            
            Inversions = 1
            A[p], A[p+1] = A[p+1], A[p]
            
            return Inversions
        
        else:
            
            Inversions = 0
        
            return Inversions
        
    else:
    
        q = math.floor((p+r)/2)
        Inversions_Left = Merge_Inversions(A,p,q)
        Inversions_Right = Merge_Inversions(A,q+1,r)
        Temp_Inversions = Merge_Number_Of_Inversions(A,p,q,r,Inversions_Left,Inversions_Right)
    
        Inversions = Inversions + Temp_Inversions
    
        return Inversions


# We only added a constant time operation, so we're good. The run time complexity is still $ \Theta ( n \lg n )$.
