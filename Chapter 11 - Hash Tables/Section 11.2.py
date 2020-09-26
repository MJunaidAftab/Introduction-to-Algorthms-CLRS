#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipynb.fs.full.HashTable import Hash_with_Chaining


# ### 11.2.1
# 
# Note that a collision takes place if and only if for each of the $i = 1, ..., n$ elements stored in the array, $T$, we have that for some $j = i + 1, ... , n$, we have that $h(i) = h(j)$. Let $X_{ij}$ be the indicator random variable that assumes the value $1$ if $h(i) = h(j)$. First note that if the key if fixed to be $i$, denote by $N | slot = i$ the numbers of collisions take place in the slot $h(i)$. We have,
# 
# $$
# \mathbb{E} (N | slot = i ) = \mathbb{E} \bigg ( \sum_{j = i + 1}^{n} X_{ij} \bigg ) = \sum_{j = i + 1}^{n} \mathbb{E} ( X_{ij} ) = \sum_{j = i + 1}^{n} \frac{1}{m} = \frac{n - i}{m}.
# $$
# 
# Hence we have a new random variable, $M$, that assumes the values $\frac{n - i}{m}, i = 1, ..., n$. Hence the desired expected value is given by,
# 
# $$
# \mathbb{E} ( N ) = \mathbb{E} \bigg ( \sum_{i = 1}^{n} \sum_{j = i + 1}^{n} X_{ij} \bigg ) = \sum_{i = 1}^{n} \frac{n - i}{m} = \frac{1}{m} \sum_{i = 1}^{n} (n - i) = \frac{1}{m} \sum_{k = 0}^{n - 1} k = \frac{1}{m} \frac{n(n-1)}{2} = \frac{n(n-1)}{2m} = \frac{n \alpha - \alpha}{2} = \frac{\alpha( n - 1)}{2}.
# $$

# ### 11.2.2

# In[2]:


def hashfunction(k):

    position = k % 9
    
    return position


U = list(range(1,101))

H = Hash_with_Chaining(9,U,hashfunction)

H.insert(5,5)
H.insert(28,28)
H.insert(19,19)
H.insert(15,15)
H.insert(20,20)
H.insert(33,33)
H.insert(12,12)
H.insert(17,17)
H.insert(10,10)

D = H.getDlllist()

for index in range(len(D)):

    A = D[index] 
    
    if A == None:
        
        print('The doubly linked list at index', index, 'is empty.')
        print('---------------------------------------------')
    
    else:
    
        x = A.getHead()
        print('The doubly linked list at index', index, 'is given by:')
        print(x.getData())

        while x.getNext() != None:
    
            print(x.getNext().getData())
            x = x.getNext()
            
        print('---------------------------------------------') 


# We see that a key getes mapped to index $i = 0, 1, ..., 8$ if and only if we have that $\text{key} \bmod 9 = i$. Note that we have programmed the doubly linked list such that each new element is insert at the tail end of the list!

# ### 11.2.3
# 
# Using a binary search, we can now implement deletion in $\Theta ( \lg \alpha )$ time. Here, once again we are assuming that the pointer to they key being deleted is unknown, and that the value of the hash function at each key is stored. Insertion now also takes place $\Theta ( \alpha )$ time, since we must sort the keys in each doubly linked list. Both successful and unsuccessful searches again take $\Theta (1 +  \alpha )$ time.
# 
# ### 11.2.5
# 
# Assume the conditions of uniform hashing. As a thought experiment, assume we're hashing *all* the elements in the universe into the hash table. Assume that all the $m$ slots contain at most $n-1$ keys. We then have that the hash table contains at most,
# 
# $$
# m(n-1) = mn - m \; \text{keys} \quad m \geq 1,
# $$
# 
# contrary to the fact that we have $|U| > mn$ and we are hashing into all keys from the universe in the hashtable. So we are a guarnteed that there exists a subset of $n$ keys in the universe that all hash to the same slot. 
# 
# ### 11.2.6
# 
# <font color='red'>This is how we have interpreted the problem: we assume, ex-ante, a number at random is chosen from the $n$ numbers placed in the hash table. Along with the number, we also generate the index which determines at what 'time' the number was added in the hash table. This is a different spin on the original intention on this questions, but oh well...</font> 
# 
# For each chosen key, $i$, that is to be printed, follow the following scheme: pick a linked list at random, and search the linked list for the element. Searching each linked list takes $O(L)$ time. If we don't find this element, discard this list, and now pick another linked list at random repeat the process untill we're done. Let $T$ denote the time it takes for this scheme to run, and $K$ be the event that takes value $i$ if key $i$ is being searched. The time complexity of the algorithm is given by the expression,
# 
# $$
# \mathbb{E}(T) = \mathbb{E} ( \mathbb{E} (T|K) ) = \frac{1}{n} \sum_{i = 1}^{n} \mathbb{E} (T | K = i ).
# $$
# 
# We have that key $i$ can be searched in at most $m$ steps of the recursion procession described above. The probability of the key being searched successfully at the $k^{th}$ step is,
# 
# $$
# \frac{m-1}{m}\frac{m-2}{m-1} \cdots \frac{m-(k-1)}{m-k}\frac{1}{m-(k-1)} = \frac{1}{m}.
# $$
# 
# Assume the keys are aranged in order in which they were added to the hash table. So we know, for example, that key number $n$ has to be the first entry in the doubly linked list in which the key is located; key number $n-1$ is either the first or the second entry in the doubly linked list in which the key is located. So if we're searching for key number $i$, search the first $i$ entries of each doubly linked list.  Hence we have,
# 
# $$
# \mathbb{E} (T | K = i ) = \sum_{j = 1}^{m} O((n - (i - 1) j) P (\text{key i gets searched in j steps}) = O \bigg ( (n - (i - 1) \sum_{j = 1}^{m} \frac{j}{m} \bigg ) = O \bigg ( \frac{(n - (i - 1) m(m+1)}{2m} \bigg ) = O \bigg ( \frac{((n - (i - 1))(m+1)}{2} \bigg ).
# $$
# 
# Hence, we have,
# 
# $$
# \mathbb{E}(T) = \frac{1}{n} \sum_{i = 1}^{n} \mathbb{E} (T | K = i ) = O \bigg ( \frac{(m+1)}{2n} \sum_{i = 1}^{n} n - (i - 1) \bigg ) = O \bigg ( \frac{(m+1)}{2n} \sum_{i = 1}^{n} k \bigg ) = O \bigg ( \frac{(m+1)(n+1)}{4n} \bigg ) = O (1 + 1/n) ( 1 + 1/\alpha) = O (L ( 1 + 1/\alpha)).
# $$
# 
# To make this argument work, note that we need to know both the key and the *index* of the the key being searched. So this algorithm works if we implement it such that the input is the the index from 1 to $n$ of the the key we're trying to fetch and the key itself from the list of values inputted in the hash table. For example, we could have $n = 100$ and $x_{27} = 13091$; so to fetch $13091$ from the list, we'd input the index $27$th and the key $13091$. So we'd have to keep a running list of the keys and the indicies to make this argument work. We can do this by implementing a list in Python from which should take $O(1)$ time to retrieve from memory the key being searched and the corresponding index.

# 
