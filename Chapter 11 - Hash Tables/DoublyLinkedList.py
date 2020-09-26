#!/usr/bin/env python
# coding: utf-8

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

