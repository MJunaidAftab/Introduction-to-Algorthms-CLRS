#!/usr/bin/env python
# coding: utf-8

# ## 2-1
# 
# a and b. Insertion sort sorts $n/k$  lists of length $k$. For insertion sort, if the length of the list is $m$, the time complexity of the algorithm is $\Theta (m^2)$. Hence each list is sorted in $\Theta (k^2)$ time. Since there are a total of $n/k$ lists, the time complexity of the algorithm is $n/k \; \Theta (k^2) = \Theta (n/k)$.
# 
# For simplicity, assume that $n/k$ is a power of 2. So we have $n/k$ sublists, each of length $k$. First split the array of $n$ elements into $n/k$ arrays each of length $k$. We now compute $D(n)$, the cost of making this division. This should be $\Theta (1)$. We now compute $C(n)$ the cost of merging the solutions of the sub-divided problems. This amounts to merging using the standard mechanism to merge 2 sublists at a time. <font color='red'>This is where it gets tricky.</font> Collate the $n/k$ sublists into a single list. This should take $\Theta (1)$ time. Now divide this list till you end up with a 2 lists each. Now recursively merge these lists till you get back to the top. This is modelled by the recurrence relation $S(x) = S(x/2) + \Theta(n)$, where $x = n/k$, the number of lists. <font color='red'>Note that at each step we do a TOTAL of n comparison for the different number of merges that need to be done at each level!</font>
# 
# The recurrence relation is given by 
# 
# $$
# T(n) = \underbrace{T(k) + ... + T(k)}_{\text{$n/k$ times}} + S(n/k).
# $$
# 
# The solution, by repeated iteration is,
# 
# $$
# \begin{align}
# T(n) & = \underbrace{T(k) + ... + T(k)}_{\text{$n/k$ times}} + S(n/k), \\
#      & = n/k \Theta (k^2) + S(n/k), \\
#      & = \Theta (nk) + S(n/k), \\
#      & = \Theta (nk) + S(n/2k) + \Theta(n), \\
#      & = \Theta (nk) + S(n/4k) + \Theta (n), \\
#      & = \Theta (nk) + \underbrace{\Theta(n) + ... + \Theta(n)}_{\text{$\lg(n/k)$ times}}, \\
#      & = \Theta (nk) + \Theta(n\lg(n/k)), \\
#      & = \Theta (nk + n\lg(n/k)).
# \end{align}
# $$
# 
# 
# 
# c. Standard merge sort runs in $\Theta (n \lg n)$ time. To have the modified algorithm have the same running time as standard merge sort, we'd need to have $\Theta (n \lg n) = \Theta (n\lg(n/k))$, which is equivalent to the condition,
# 
# $$
# \lim_{n \rightarrow \infty} \frac{nk(n) + n\lg(n/k(n))}{n \lg n} = \lim_{n \rightarrow \infty} \frac{k(n) + \lg(n/k(n))}{\lg n} 
# = \lim_{n \rightarrow \infty} \frac{k(n) + \lg n - \lg k(n)}{\lg n} = \lim_{n \rightarrow \infty} 1 + \frac{k(n)}{\lg n}  - \frac{\lg k(n)}{\lg n},
# $$
# 
# to be finite and neither $0$ nor $+ \infty$. A sufficient condition is that $k(n) = \Theta ( \lg n)$ or $o(\lg n)$ for that matter.

# ## 2-2

# In[3]:


def Bubble_Sort(A):
    n = len(A)
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                
    return A 

A = [1,8,3,5777,7,15, 44,69,78,15]
print(Bubble_Sort(A))


# The loop invaraint is:
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

# ## 2-3

# In[12]:


def Horners_Rule(A):
    #A contains the list of coefficients
    y = 0
    for i in range(n,-1,-1):
        y = A[i] + x*y


# The running time is $\Theta (n)$.

# In[14]:


def Naive_Horner(A):
    y = 0
    for i in range(0,n+1):
        z = A[i]
        for j in range(0,i):
            z = z*x
        y = y + z


# The running time of the algorithm is $\Theta(n^2)$. We skip the verification of this algirthim.

# ## 2-4
# 
# a. The inversions are (1, 5), (2, 5), (3, 4), (3,5), (4,5).
# 
# b. The array $[n, n-1, n-2, ... , 3, 2, 1]$ has the most inversions. It has a total of $n(n-1)/2$ inversions.
# 
# c. The running time of insertion sort is of the order of magnitude (read: big theta) of the number of inversions in the input array. The reason is that the time complexity of insertion sort is determined by i) the number of items in the list and ii) the number of adjacent inverted elements in one of the multiple subarrays we consider while placing each element in its right place in the list. But that's what exactly measures the number of inversions in an array. Hence, we expect to be $\Theta$ of each other.
# 
# d. <font color='red'>Given the relationship found in c, we can find the number of permutations in an efficient way by recalling that we improve on the insertion sort algortihm using merge sort.</font>

# In[2]:


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
    
    #!!!!! 
    #Instead of iterating over the both the lists which would give us a quadratic time complexity, we instead
    #use the scheme used to write the merge routine of the MERGE-SORT algorithm. We'll merge these lists into our
    #original list, A, and compute inversions as we go along.
    
    ### Consider the example of two lists with zero inversions Take the lists to be
    
    # 6 7 8 9 10 ... 1 2 3 4 5
    # When we run merge sort, we first compare 6 and 1 and put 1 in the right place. But note 6 > 1 so we 
    # increment the variable inversions by 1. But note 6 is less than all other variables in the first list 
    # so instead we increment by 5 (n1). More generally:
    
    # if the length of the first list is n1, and we have found an inverted element at index i (i = 0, ... , n1) 
    # in the first list, increment the inversion number by n1 - i.
    
    # After putting 1 in place, we compare 6 with 2, 3, 4 and 5 and increment
    #inversions by 5, 5, 5, 5. This procedure is captured by the description above which is iterative in
    #description.
    
    # 1 2 3 4 5 _ _ _ _ _
    
    #We now simply overwrite the the first and NO additional inversions need to be accounted for. More generally,
    
    #When one sublist has been exhausted, we need not update the inversion number anymore.
    
    # Consider the example:
    # 5 7 8 9 10 ... 1 2 3 4 6
    
    # We now 5 have > 1, 2, 3, 4, so we make the first four entries of A to be 1, 2, 3, 4 resp. and increase inversions by
    # 5, 5, 5, 5 (n1). 
    
    #BUT NOW NOTE: we have 5 < 6. We update the list A to partially look like 1, 2, 3, 4, 5 and DON't increase
    #the inversion number at all. More generally:
    
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


# In[45]:


#We now implement the MERGE-INVERSIONS algorithm.

import math

def Merge_Inversions(A,p,r):

    n = r - p + 1 #n is greater than or equal to 1
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
        Temp_Inversions = Merge_Number_Of_Inverstions(A,p,q,r,Inversions_Left,Inversions_Right)
    
        Inversions = Inversions + Temp_Inversions
    
        return Inversions


# In[50]:


A = [4,7,5,1,10,6,17]
n = len(A)
print(Merge_Inversions(A,0,n-1))


# We only added a constant time operation, so we're good. The run time complexity is still $ \ ( \Theta n \lg n )$.
