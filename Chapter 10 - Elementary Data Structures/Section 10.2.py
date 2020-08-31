#!/usr/bin/env python
# coding: utf-8

# # Linked List
# 
# linked list is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object.
# 
# Each element of a DOUBLY linked list $L$ is an object with an attribute $key$ and two other pointer attributes: $next$ and $prev$. Given an element $x$ in the list, $x.next$ points to its successor in the linked list, and $x.prev$ points to its predecessor. If $x. prev  = NIL$, the element $x$ has no predecessor and is therefore the first element, or head, ofthe list. If $x.next = NIL$, the element $x$ has no successor and is therefore the last element, or tail, of the list. In a SINGLY linked, we omit the $prev$ pointer. A SORTED list is stored in ascending order. In a CIRCULAR list, the $prev$ pointer of the head of the list points to the tail, and the $next$ pointer of
# the tail of the list points to the head.y
# 
# We work, for the most part, with doubly linked, unsorted/unorderd lists. We first implement the NODE class. The idea is that each element in the linked list can be represented as a node, and directed edges emanating from the node are the $prev$ and $next$ pointers that point towards the previous and next elements respectively in the list.

# In[1]:


class Node(object):
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
    def setPrev(self,newprev):
        self.prev = newprev


# The special Python reference value NONE will play an important role in the Node class and later in the linked list itself. A reference to NONE will denote the fact that there is no next node. Note that a node is initially created with next set to None.

# We first write an auxilliary class.

# In[49]:


class DoublyLinked_List(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.headclass = None
        self.tailclass = None
        print(self.head, self.tail)
        
        #Initially the doubly linked list is empty so contains no head and tail.
        
    def empty(self):
        Boolean = self.head
        
        if Boolean == None:
            
            print('The doubly linked list is empty.')
            return None
        
        else:
            
            print('The doubly linked list is not empty.')
            return None
    
    def add(self,x):
        
        x = Node(x)
        
        if self.head == None:
            
            self.head = x.getData()
            self.headclass = x
            
            self.tail = x.getData()
            self.tailclass = x
            
            return self.head, self.tail
        
        else:   
            
            self.tailclass.setNext(x)
            x.setPrev(self.tailclass)

            PreviousTailNode = self.tailclass
            a = PreviousTailNode.getNext().getData()
            self.tailclass = x

            return self.tailclass.getPrev().getData(), PreviousTailNode.getNext().getData()
        
    #SEARCH finds the first NODE with key k in list L by a simple linear search,  returning a pointer to 
    #this node.
    
    def search(self,k):
  
        x = self.headclass
        
        if x.getData() == k:
            
            return x, x.getData()
        
        else:
            
            dummyclass = x.getNext()
            
            while dummyclass != None:
                
                if dummyclass.getData() == k:
                    
                    return dummyclass, dummyclass.getData()
                
                dummyclass = dummyclass.getNext()
            
            Boolean = None
            
            return Boolean  
        
        
    #We implement an INSERT function that interests an element x as the new head of the linked list.
    
    def insert(self,x):
        
        x = Node(x)
        OldHead = self.headclass
        
        OldHead.setPrev(x)
        x.setNext(OldHead)
        self.headclass = x
        
        return self.headclass.getData(), self.headclass.getNext().getData(), OldHead.getPrev().getData()
    
    #Here we assume that an element with key x is contained in the linked list so we can delete the key
    #and update the pointers. We delete the first instance of x.
    
    def delete(self,k):
        
        x = self.headclass
        
        if x.getData() == k:
            
            newheadclass = x.getNext()
            
            if newheadclass == None:
                
                self.head = None
                self.headclass = None 
                self.tailclass = None
                self.tail = None
                
            else:
                
                x.setNext(None)
                newheadclass.setPrev(None)
                self.headclass = newheadclass
                
            
                return self.headclass.getData(), self.headclass.getNext().getData() 
    
    
        nextclass = x.getNext()  
        
        while nextclass !=None:
            
            if nextclass.getData() == k:
                
                if nextclass.getNext() !=None:
                    
                    nextclass.getPrev().setNext(nextclass.getNext())
                    nextclass.getNext().setPrev(nextclass.getPrev())
                    
                    a = nextclass.getPrev().getNext().getData()
                    b = nextclass.getNext().getPrev().getData()
                    
                    nextclass.setNext(None)
                    nextclass.setPrev(None)
                    
                    return a, b
                    
                else:
                    
                    self.tailclass = nextclass.getPrev()
                    self.tailclass.setNext(None)
                    nextclass.setPrev(None)
                    
                    return self.tailclass.getData(), self.tailclass.getNext(),self.tailclass.getPrev().getData()
                    
            nextclass = nextclass.getNext()    


# We first test the DOUBLY_LINKED_LIST class above by running some code to both generate and manipulate a doubly linked list.

# In[50]:


linkedlist = DoublyLinked_List()

n, p = linkedlist.add(31)
print(n,p)
n, p = linkedlist.add(77)
print(n,p)
n, p = linkedlist.add(17)
print(n,p)
n, p = linkedlist.add(93)
print(n,p)
n, p = linkedlist.add(26)
print(n,p)
n, p = linkedlist.add(54)
print(n,p)

print('--------------------------------------------------')

print(linkedlist.search(26))

print('--------------------------------------------------')

h, n, p =  linkedlist.insert(1)
print(h, n, p)

print('--------------------------------------------------')

a, b = linkedlist.delete(1)
print(a, b)

print('--------------------------------------------------')

a, b = linkedlist.delete(17)
print(a, b)

print('--------------------------------------------------')

a, b, c = linkedlist.delete(54)
print(a, b, c)


# ### Time Complexity of the Functions:
# 
# The time complexity of the SEARCH function on a list of $n$ elements is $\Theta (n)$ as we run a linear search algorithm. The running time for SEARCH function on a list of $n$ elements is $O(1)$. The running time of the DELETE function is also $O(1)$ since we only perform a number of constant time operations.

# In[ ]:




