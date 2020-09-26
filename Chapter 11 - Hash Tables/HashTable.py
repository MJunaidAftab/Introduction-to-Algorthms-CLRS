#!/usr/bin/env python
# coding: utf-8

# In[5]:


from ipynb.fs.full.DLL import Node
from ipynb.fs.full.DLL import Doubly_Linked_List
import random


# In[6]:


class Hash_with_Chaining(object):
    
    def __init__(self,m,U,hashfunction):
        
        self.universe = U
        
        absmin = abs(min(U))
        absmax = abs(max(U))
        depth = max([absmin,absmax])
        
        self.hashvalues = [None]*(depth + 1)
        
        self.hashfunction = hashfunction
        
        self.tablesize = m
        self.dlllist = [None]*m
        
    def getDlllist(self):
        
        return self.dlllist
    
    
    def insert(self, x, hasfunctioninput):
        
        position = self.hashfunction(hasfunctioninput)
        dll = self.dlllist[position]
        
        if dll == None:
            
            A = Doubly_Linked_List()
            A.add(x)
            
            self.dlllist[position] = A
            
            self.hashvalues[abs(x)] = position
            
        else:
            
            dll.add(x)
            self.dlllist[position] = dll
            
            self.hashvalues[abs(x)] = position
            
    def search(self, x):
        
        #position = self.hashvalues[abs(x)]
        position = self.hashfunction(self.tablesize)
        dll = self.dlllist[position]
        
        if dll == None:
            
            print('The doubly linked list is empty.')
            
        else:
            
            Boolean = dll.search(x)
            
            if Boolean == True:
                
                print(x, 'is in the doubly linked list at evalauated at index', position )
                
            else:
                
                print(x, 'is not in the doubly linked list evalauated at index', position)
                
                
    def delete(self,x):
        
        position = self.hashvalues[abs(x)]
        dll = self.dlllist[position]
        
        dll.delete(x)
        self.dlllist[position] = dll


# Note insertion takes $O(1)$ time, and deletion, and search takes $O(l)$ time, where $l$ is the length of the linked list being searched. Note that here are assuming that while the node to be deleted is known, the pointer to that node is NOT available/known, which is implicit in our implementation of the doubly linked list class from before.

# In[7]:


def hashfunction(m):

    position = random.randint(0, m-1)
    
    return position


U = list(range(1,101))

H = Hash_with_Chaining(2,U,hashfunction)

H.insert(U[1],2)
H.insert(U[10],2)
H.insert(U[20],2)
H.insert(U[30],2)
H.insert(U[40],2)
H.insert(U[50],2)
H.insert(U[60],2)
H.insert(U[70],2)
H.insert(U[80],2)
H.insert(U[90],2)

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


# In[8]:


H.search(2)


# In[ ]:




