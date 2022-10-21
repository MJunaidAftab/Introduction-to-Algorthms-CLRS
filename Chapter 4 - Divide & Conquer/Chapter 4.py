#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import numpy as np


# # Section 4.1
# 
# ## Problem 1
# 
# Simply add additional rows and columns of zeros to ensure both the number of rows and columns are the same multiple of 2.
# 
# ## Problem 2
# 
# Let $A$ be a $kn \times n$ matrix and let $B$ be a $n \times kn$ times matrix ($ k \geq 1)$. Note that we can write the matrices in the following block form:
# 
# $$
# A 
# =
# \begin{bmatrix}
#            A_{1} \\
#            A_{2} \\
#            \vdots \\
#            A_{k}
# \end{bmatrix}
# ,
# \quad \quad 
# B =
# \begin{bmatrix}
# B_{1} & B_{2} & \cdots & B_{k}
# \end{bmatrix}
# $$
# 
# where each of the $2k$ matrices $A_i$ and $B_j$ are $n \times n$ matrices. 
# 
# First consider the case $A \times B$. Note that,
# 
# $$
# AB
# =
# \begin{bmatrix}
# A_{1} B_{1} & \cdots & A_{1}B_{k} \\
# \vdots & \ddots  & \vdots \\
# A_{k} B_{1} & \cdots & A_{k}B_{k} \\
# \end{bmatrix}
# $$
# 
# 
# 
# 
# Each of the $k^2$ matrices can be computed in time $\Theta ( n^{3} )$. Hence the running time of the algorithm is $ \Theta ( k^2 n^{3} )$.
# 
# Now consider the case $B \times A$. Note that,
# 
# $$
# BA = \sum_{i=1}^{k} A_i B_i
# $$
# 
# Each of the $k$ matrix multiplications take time $\Theta ( n^{3} )$. Hencr the running time of the algorithm is $ \Theta ( k n^{3} )$.
# 
# ## Problem 3
# 
# Since $3n^2$ elements are copied in this case, the recursion now becomes:
# 
# $$
# T(n) = 8T(n/2) + \Theta ( n^2 ).
# $$
# 
# Since $n^2 = \omega ( n^{\lg 8} ) = \omega ( n^{\lg 8} ) = \omega ( n^3 )$, the master theorem implies that the running time of the algorithm is still $\Theta ( n^3 )$.
# 
# ## Problem 4
# 
# We first implement code for the MATRIX-ADD-RECURSIVE Algorithm. The implementation of the algorithm assumes that the input matrices $A$ and $B$ are Numpy matrices. For simplicity, we assume that the matrices are square and have dimensions that are power of $2$.

# In[2]:


def Matrix_Add_Recursive(A,B):
    
    n = np.shape(A)[0]
    
    if n != np.shape(B)[0]:
        
        print("Oops! The matrices don't have the same dimensions.")
        return None
    
    if n == 1:
        
        C = A + B
        
        return C
    
    else:
        
        A11 = A[0:int(n/2),0:int(n/2)]
        A12 = A[0:int(n/2),int(n/2):n]
        A21 = A[int(n/2):n,0:int(n/2)]
        A22 = A[int(n/2):n,int(n/2):n]
        
        
        B11 = B[0:int(n/2),0:int(n/2)]
        B12 = B[0:int(n/2),int(n/2):n]
        B21 = B[int(n/2):n,0:int(n/2)]
        B22 = B[int(n/2):n,int(n/2):n]
        
        C11 = Matrix_Add_Recursive(A11,B11)
        C12 = Matrix_Add_Recursive(A12,B12)
        C21 = Matrix_Add_Recursive(A21,B21)
        C22 = Matrix_Add_Recursive(A22,B22)
        
        C = np.zeros((n,n))
        
        C[0:int(n/2),0:int(n/2)] = C11
        C[0:int(n/2),int(n/2):n] = C12
        C[int(n/2):n,0:int(n/2)] = C21
        C[int(n/2):n,int(n/2):n] = C22
        
        return C


# Assume that matrix partitioning uses $\Theta (1)$ index calculations, the recurrence describing the algorithm is:
# 
# $$
# T(n) = 4T(n/2) + \Theta (1).
# $$
# 
# Since $\Theta ( 1 ) = \omega ( n^{\lg 4} ) = \omega ( n^2 )$, the master theorem implies that the running time of the algorithm is $\Theta ( n^2 )$.
# 
# If we use $ \Theta ( n^2 ) $ time implement the partitioning instead of index calculations, the recurrence becomes:
# 
# $$
# T(n) = 4T(n/2) + \Theta (n^2).
# $$
# 
# Since $\Theta ( n ) = \Theta ( n^{\lg 4} ) = \Theta ( n^2 )$, the master theorem implies that the running time of the algorithm is $\Theta ( n^2 \lg n )$.

# # Section 4.2
# 
# ## Problems 1 and 2

# In[3]:


def Strassens_Algorithm(A,B,n):
    
    n = np.shape(A)[0]
    
    if n != np.shape(B)[0]:
        
        print("Oops! The matrices don't have the same dimensions.")
        return None
    
    C = np.zeros((n,n))
    
    
    if n == 1:
        
        C[:1,:1] = A[:1,:1]*B[:1,:1]
        
        return C
        
    else:
        
        m = int(n/2)
        
        A_11 = A[:m,:m]
        B_11 = B[:m,:m]
        
        A_12 = A[:m,m:n]
        B_12 = B[:m,m:n]
        
        A_21 = A[m:n,:]
        B_21 = B[m:n,:m]
        
        A_22 = A[m:n,m:n]
        B_22 = B[m:n,m:n]
        
        S_1 = B_12 - B_22
        S_2 = A_11 + A_12
        S_3 = A_21 + A_22
        S_4 = B_21 - B_11
        S_5 = A_11 + A_22
        S_6 = B_11 + B_22
        S_7 = A_12 - A_22
        S_8 = B_21 + B_22
        S_9 = A_11 - A_21
        S_10 = B_11 + B_12
        
        #We recursively multiply matrices now
        
        P_1 = Strassens_Algorithm(A_11,S_1,m)
        P_2 = Strassens_Algorithm(S_2,B_22,m)
        P_3 = Strassens_Algorithm(S_3,B_11,m)
        P_4 = Strassens_Algorithm(A_22,S_4,m)
        P_5 = Strassens_Algorithm(S_5,S_6,m)
        P_6 = Strassens_Algorithm(S_7,S_8,m)
        P_7 = Strassens_Algorithm(S_9,S_10,m)
        
        
        C[0:m,0:m] = P_5 + P_4 - P_2 + P_6 
        
        C[0:m,m:n] = P_1 + P_2
        
        C[m:n,0:m] = P_3 + P_4
        
        C[m:n,m:n] = P_5 + P_1 - P_3 - P_7
        
        return C  


# Here is the solution to the first problem now.

# In[4]:


n = 2

A = np.array([[1, 3], [7, 5]])
B = np.array([[6, 8], [4, 2]])
C = Strassens_Algorithm(A,B,n)

print(C)


# ## Problem 4.3
# 
# For simplicity, assume thet $n$ is a power of 3. In this case, we have that the recurrence relation is given by,
# 
# $$
# T(n) = kT(n/3) + \Theta ( n^2 ).
# $$
# 
# By the Master Theorem, the largest value of $k$ would be 21.
# 
# ## Problem 4.4
# 
# If we follow V. Pan's method of multiplying $68$ by $68$ matrices then, assuming that $n$ is a power of 68, the recurrence relation will be,
# 
# $$
# T(n) = 132,464T(n/68) + \Theta ( n^2 ).
# $$
# 
# Since $\log_{68} 132,464 \sim 2.79512$, by the Master Theorem, the solution to this recurrence relation is $\Theta ( n^{\log_{68} 132,464} ) \sim \Theta ( n^{2.79512} )$.
# 
# If we follow V. Pan's method of multiplying $70$ by $70$ matrices then, assuming that $n$ is a power of 70, the recurrence relation will be,
# 
# $$
# T(n) = 143,640T(n/70) + \Theta ( n^2 ).
# $$
# 
# Since $\log_{70} 143,640 \sim 2.79312$, by the Master Theorem, the solution to this recurrence relation is $\Theta ( n^{\log_{70} 143,640} ) \sim \Theta ( n^{2.79312} )$.
# 
# If we follow V. Pan's method of multiplying $72$ by $72$ matrices then, assuming that $n$ is a power of 72, the recurrence relation will be,
# 
# $$
# T(n) = 155,424T(n/72) + \Theta ( n^2 ).
# $$
# 
# Since $\log_{72} 155,424 \sim 2.79514$, by the Master Theorem, the solution to this recurrence relation is $\Theta ( n^{\log_{70} 143,640} ) \sim \Theta ( n^{2.79514} )$.
# 
# Now Strassen's algorithm's time complexity is $\Theta ( n^{\lg 7} ) \sim \Theta ( n^{2.80735} )$. Hence all of the alternative algorithms outperform Strassen's algorithm asymptotically, and the fastest algorthm is given when $n$ is assumed to be a power of $72$.
# 
# ## Problem 4.5
# 
# Let,
# 
# $$
# A = (a + i b)(c + id) = (ac - bd) + i (bc + ad), \quad \quad B = bc, \quad \quad C = ad.
# $$
# 
# We get that $ac - bd = A - B - C$ and $ad + bc = C + B$. This is in spirit of Strassen's algorithm as we have cut down on the numbe rof multiplications by 1.
# 
# ## Problem 4.6
# 
# Consider the matrix with rows $[0, X]$ and $[Y,0]$. The square of this matrix has rows $[XY, 0]$ and $[0,YX]$.
