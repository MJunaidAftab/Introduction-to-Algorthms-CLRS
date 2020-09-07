#!/usr/bin/env python
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


# In[3]:


class DoublyLinked_List(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.headclass = None
        self.tailclass = None
        
        #Initially the doubly linked list is empty so it contains no head and tail.
        
    
    def getTail(self):
        
        return self.tailclass
    
    def getHead(self):
        
        return self.headclass
    
    def setTail(self,newtail):
        
        self.tailclass = newtail
        
    def setHead(self,newhead):
        
        self.headclass = newhead
 
    
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
            self.tailclass = x

            return self.headclass.getData(), self.tailclass.getData()
        
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

# In[4]:


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
# The time complexity of the SEARCH function on a list of $n$ elements is $\Theta (n)$ as we run a linear search algorithm. The running time for INSERT function on a list of $n$ elements is $O(1)$. The running time of the DELETE function is $O(n)$. Here we assume that we have implement a linear search to see if there exists a node that has a key value that we would like to be deleted. Of course, if we're given the pointers of the node we wish to delete, then the time complexity of the algorithm would $O(1)$.

# ### 10.2.1
# 
# See the above code for the implementation of the INSERT function in $O(1)$ time using a singly linked list. First note that if we wish to implement the DELETE function to delete either the head or the tail of the singly linked list, we can easily do so in $O(1)$ time. Deleting the head of the list is easy; simply change the $next$ pointer of the head to NONE, and update the head to the node to which the pointer $head.next$ points. To delete the tail of the singly linked list in $O(1)$ time, modify the implementation of the singly linked list to keep track of the node that precedes the tail of the list. Call the pointer pointing to this node $tailminus$. To remove the tail of the list, simply set the pointer $tailminus.next$ to NONE. We use this strategy below to implement a queue using a singly linked list.
# 
# We can, in principle, use the aforementioned strategy to implement the DELETE function in $O(1)$ $time$. We can effevitvely make the node we wish to delete the last node in an appropriate sub-list of our singly linked list; simply keep copies of sub-lists that contain the first node, the first two nodes, the first three nodes etc. Complimentarily, keep copies of the sublists of the remaining elements in the singly linked list. Place these complimentary sub-lists in the the NODE class that corresponds to the last element in the respective sub-list. If the NODE class already contains a complimentayry pair of sub-lists, don't replace the exisiting sub-lists with another pair of complimentary sub-lists; this will ensure that we only remove the first occurence of the node containing the appropriate key. Now simply use the appropriate pair of complimentary sub-lists, remove the last tail node the appropriately chosen sub-list between the top, and make a directed node from the new tail of this sub-list to the head of other sub-list as part of the pair. This gives us the desied singly linked list. The algorithm works in $O(1)$ time, but it may end up using significant memory.
# 
# ### 10.2.2
# 
# We modify the SINGLY LINKED LIST class above to take into account the node preceding the tail node of the list. We refer to this node as TAILMINUS. This will help us easily implement a stack using a singly linked list as noted above.
# 
# Note that here we implemenent a STACK starting from an empty 'array' since a linked list starts off as an empty 'array.'

# In[5]:


class Reverse_Stack_SingleLinked(Node):
    
    def __init__(self):
        self.top = None
    
    def empty(self,stack):
        
        if self.top == None:
            
            Boolean = True
            return Boolean
        
        else:
            
            Boolean = False
            return Boolean
        
    def pull(self,x):
        
        x = Node(x)
        
        if self.top == None:
            
            self.top = x
            
            print(self.top.getData())
            
        else:
            
            oldtop = self.top
            x.setNext(oldtop)
            self.top = x
            
            print(self.top.getData())
    
    def pop(self):
        
        if self.top == None:
            
            print('The stack is empty! There is nothing to be popped')
            return None
        
        elif self.top.getNext() == None:
            
            self.top = None
            print(None)
            
        else:
            
            newtop = self.top.getNext()
            self.top.setNext(None)
            self.top = newtop     
            
            print(self.top.getData())


# In[6]:


books = Reverse_Stack_SingleLinked() #Think of stacking books!

books.pull(4)
books.pull(10)
books.pull(14)
books.pop()
books.pop()
books.pop()
books.pop()
books.pull(100)


# ### 10.2.3

# In[7]:


class Queue_SingleLinked(Node):
    
    def __init__(self):
        self.front = None
        self.rear = None 
    
    def empty(self):
        
        if self.front == None:
            
            Boolean = True
            return Boolean
        
        else:
            
            Boolean = False
            return Boolean
        
    def enqueue(self,x):
        
        x = Node(x)
        
        if self.rear == None: #In this case, self.front == None as well
            
            self.front = x
            self.rear = x
            
            print(self.front.getData(),self.rear.getData())
            
        else:
            
            self.rear.setNext(x)
            self.rear = x
            
            print(self.front.getData(),self.rear.getData())
        
        
    def dequeue(self):
        
        if self.front == None:
            
            print('The queue is empty! There is nothing to dequeue')
            return None
        
        elif self.front == self.rear:
            
            self.front = None
            self.rear = None
            
            print(None,None)
            
        else:         
        
            newfront = self.front.getNext()
            self.front.setNext(None)
            self.front = newfront
            
            print(self.front.getData(),self.rear.getData())


# In[8]:


q = Queue_SingleLinked()
q.enqueue(10) 
q.enqueue(20) 
q.dequeue()  
q.enqueue(30) 
q.enqueue(40) 
q.enqueue(50)


# ### 10.2.5
# 
# Singly, circular linked list.

# In[9]:


class Singly_Linked_List_Circular(object):
    
    def __init__(self):
        self.head = None
        self.headclass = None
        self.tailclass = None
        self.tail = None      
    
    
    def getHead(self):
        
        return self.headclass
    
    def getTail(self):
        
        return self.tailclass   
    
    def setTail(self,newtail):
        
        self.tailclass = newtail
        
    def setHead(self,newhead):
        
        self.headclass = newhead
    
    
    def empty(self):
        
        if self.headclass == None:
            
            print('The singly linked list is empty.')
            Boolean = True
            return Boolean
        
        else:
            
            Boolean = False
            return Boolean
    
    def add(self,x):
        
        x = Node(x)
        
        if self.headclass == None:
            
            self.headclass = x
            self.head = self.headclass.getData()
            self.tailclass = x
            self.tail = self.tailclass.getData()
            
            self.tail.setNext(x)
            
            return self.headclass, self.head
        
        else:   
            
            x.setNext(self.headclass)
            self.headclass = x
            self.tailclass.setNext(self.headclass)
            
            self.head = self.headclass.getData()

            return self.headclass, self.head

            
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
        
    
    #Here we assume that an element with key x is contained in the linked list so we can delete the key
    #and update the pointers. We delete the first instance of x.
    
    ###We implement a special case of the DELETE function here that only correctly deletes
    ###HEAD of the linked list. Therefore, we are able to implement thre DELETE function in O(1) time.
    
    def delete(self):
        
        if self.head.getNext() == None:
            
            self.head = None
            self.headclass = None
            self.tailclass = None
            self.tail = None 
            
        else:  
        
            newheadclass = self.headclass.getNext()
            self.headclass.setNext(None)
            self.headclass = newheadclass
            self.tailclass.setNext(self.headclass)
            
            self.head = self.headclass.getData()
        
            return self.headclass, self.head


# ### 10.2.6
# 
# Assume the two sets are implemented as doubly linked lists. We use Python's built-in data structures here now to solve this problem.

# In[10]:


def Union(A,B):
    
    lastnode_A = A.getTail()
    firstnode_B = B.getHead()
    
    lastnode_A.setNext(firstnode_B)
    firstnode_B.setPrev(lastnode_A)
    
    lastnode_B = B.getTail()
    A.setTail(lastnode_B)
    
    return A


# In[11]:


A = DoublyLinked_List()
B = DoublyLinked_List()

A.add(17)
A.add(20222)
A.add(3000)

B.add(1)
B.add(5)
B.add(20)
B.add(0.9)
B.add(85)

C = Union(A,B)

print(C.getHead().getData())
print(C.getTail().getData())


# ### 10.2.7
# 
# We first write code for a singly linked list w/o implementing the delete function.

# In[169]:


class Singly_Linked_List(object):
    
    def __init__(self):
        self.headclass = None
        self.tailclass = None 
    
    
    def getHead(self):
        
        return self.headclass
    
    def getTail(self):
        
        return self.tailclass   
    
    def setTail(self,newtail):
        
        self.tailclass = newtail
        
    def setHead(self,newhead):
        
        self.headclass = newhead
    
    
    def empty(self):
        
        if self.headclass == None:
            
            print('The singly linked list is empty.')
            Boolean = True
            return Boolean
        
        else:
            
            Boolean = False
            return Boolean
    
    def add(self,x):
        
        x = Node(x)
        
        if self.headclass == None:
            
            self.headclass = x
            self.tailclass = x
            
            return self.headclass
        
        else:   
            
            x.setNext(self.headclass)
            self.headclass = x

            return self.headclass

            
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


# In[170]:


def Reverse_LinkedList(A):
    
    head = A.getHead()
    tail = A.getTail()
    
    x = head
    y = x.getNext()
    
    x.setNext(None)
    tempnode = None
    
    while y != None:
        
        tempnode = y.getNext()
        y.setNext(x)
        x = y
        y = tempnode      
        
    A.setHead(tail)
    A.setTail(head)


# In[171]:


A = Singly_Linked_List()

A.add(1)
A.add(2)
A.add(3)
A.add(4)
A.add(5)
A.add(6)
A.add(7)
A.add(8)
A.add(9)
A.add(10)

Reverse_LinkedList(A)

x = A.getHead()
y = x.getNext()


# In[172]:


while y != None:
    
    print(y.getData())
    y = y.getNext()


# In[ ]:




