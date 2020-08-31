#!/usr/bin/env python33
# coding: utf-8

# # Linked Lists
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

# In[2]:


class DoublyLinked_List(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.headclass = None
        self.tailclass = None
        print(self.head, self.tail)
        
        #Initially the doubly linked list is empty so it contains no head and tail.
        
    def empty(self):
        Boolean = self.headclass
        
        if Boolean == None:
            
            print('The doubly linked list is empty.')
            return None
        
        else:
            
            print('The doubly linked list is not empty.')
            return None
    
    def add(self,x):
        
        x = Node(x)
        
        if self.headclass == None:
            
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

# In[3]:


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
# The time complexity of the SEARCH function on a list of $n$ elements is $\Theta (n)$ as we run a linear search algorithm. The running time for INSERT function on a list of $n$ elements is $O(1)$. The running time of the DELETE function is $O(n)$. Here we assume that we have implement a binary search to see if there exists a node that has a key value that we would like to be deleted. Of course, if we're given the pointers of the node we wish to delete, then the time complexity of the algorithm would $O(1)$.

# ### 10.2.4
# 
# ### Singly Linked List

# In[4]:


#We use the same NODE class since all we have to do is that we don't have to initialize the PREV pointers.


class Singly_Linked_List(object):
    
    def __init__(self):
        self.head = None
        self.headclass = None
        self.tailclass = None
        self.tail = None
        print(self.head)
        
        #Initially the singly linked list is empty so it contains no head.
        
    def empty(self):
        Boolean = self.headclass
        
        if Boolean == None:
            
            print('The singly linked list is empty.')
            return None
        
        else:
            
            print('The singly linked list is not empty.')
            return None
    
    def add(self,x):
        
        x = Node(x)
        
        if self.headclass == None:
            
            self.head = x.getData()
            self.headclass = x
            self.tail = x.getData()
            self.headclass = x
            
            return self.head
        
        else:   
            
            self.tailclass.setNext(x)

            PreviousTailNode = self.tailclass
            self.tailclass = x

            return PreviousTailNode.getNext().getData()
        
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
        
        x.setNext(OldHead)
        self.headclass = x
        
        return self.headclass.getData(), self.headclass.getNext().getData()
    
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
                self.headclass = newheadclass               
            
                return self.headclass.getData(), self.headclass.getNext().getData() 
    
    
        nextclass = x.getNext()  
        
        while nextclass !=None:
            
            if nextclass.getData() == k:
                
                if nextclass.getNext() !=None:
                    
                    nextclass.getPrev().setNext(nextclass.getNext())
                    
                    a = nextclass.getPrev().getNext().getData()
                    
                    nextclass.setNext(None)
                    
                    return a
                    
                else:
                    
                    self.tailclass = nextclass.getPrev()
                    self.tailclass.setNext(None)
                    
                    return self.tailclass.getData(), self.tailclass.getNext()
                    
            nextclass = nextclass.getNext()      


# A circularly linked list is similarly implemented by making minor modification to the implementation of the doubly linked list. We skip the details for now.

# ### 10.2.1
# 
# See the above code for the implementation of the INSERT function in $O(1)$ time using a singly linked list. First note that if we wish to implement the DELETE function to delete either the head or the tail of the singly linked list, we can easily do so in $O(1)$ time. Deleting the head of the list is easy; simply change the $next$ pointer of the head to NONE, and update the head to the node to which the pointer $head.next$ points. To delete the tail of the singly linked list in $O(1)$ time, modify the implementation of the singly linked list to keep track of the node that precedes the tail of the list. Call the pointer pointing to this node $tailminus$. To remove the tail of the list, simply set the pointer $tailminus.next$ to NONE. We use this strategy below to implement a queue using a singly linked list.
# 
# We can, in principle, use the aforementioned strategy to implement the DELETE function in $O(1)$ $time$. We can effevitvely make the node we wish to delete the last node in an appropriate sub-list of our singly linked list; simply keep copies of sub-lists that contain the first node, the first two nodes, the first three nodes etc. Complimentarily, keep copies of the sublists of the remaining elements in the singly linked list. Place these complimentary sub-lists in the the NODE class that corresponds to the last element in the respective sub-list. If the NODE class already contains a complimentayry pair of sub-lists, don't replace the exisiting sub-lists with another pair of complimentary sub-lists; this will ensure that we only remove the first occurence of the node containing the appropriate key. Now simply use the appropriate pair of complimentary sub-lists, remove the last tail node the appropriately chosen sub-list between the top, and make a directed node from the new tail of this sub-list to the head of other sub-list as part of the pair. This gives us the desied singly linked list. The algorithm works in $O(1)$ time, but it may end up using significant memory.
# 
# ### 10.2.2

# 
