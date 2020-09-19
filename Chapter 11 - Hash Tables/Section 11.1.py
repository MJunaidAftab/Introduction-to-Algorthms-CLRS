#!/usr/bin/env python
# coding: utf-8

# # Direct Address Tables

# Direct addressing is a simple technique that works well when the universe $U$ of keys is reasonably small. Suppose that an application needs a dynamic set in which each element has a key drawn from the universe $U = \{ 0, 1, ..., m - 1\}$, where $m$ is not too large. We shall assume that no two elements have the same key.
# 
# We implement a direct address table.

# In[1]:


class Node(object):
    
    def __init__(self,initdata):
        self.data = initdata
        self.value = None

    def getData(self):
        return self.data

    def getValue(self):
        return self.value
    
    def setData(self,newdata):
        self.data = newdata
        
    def setValue(self,newvalue):
        self.value = newvalue


# In[21]:


import math

class Direct_Address(object):
    
    def __init__(self):
    
        self.universe = U
        
        absmin = abs(min(U))
        absmax = abs(max(U))
        depth = max([absmin,absmax])
        
        
        self.counterlist = [None]*(depth + 1)
        self.valuelist = [None]*(depth + 1)
        self.nodeslist = [None]*(depth + 1)

            
    
    def initialize(self):
        
        for x in self.universe:
            
            absx = abs(x)
            self.counterlist[absx] = 1
      
    
    def search(self, x):
        
        absk = abs(x)
        value = self.valuelist[absx]
        
        return value
    
    def insert(self,x):
        
        absx = abs(x)
        
        if self.counterlist[absx] != None and self.valuelist[absx] == None:
        
            self.valuelist[absx] = x
        
            x = Node(x)
            x.setValue(x)
            self.nodeslist[absx] = x
        
    
    def delete(self,x):
        
        absx = abs(x)
        
        if self.counterlist[absx] != None and self.valuelist[absx] != None:
        
            self.valuelist[absx] = None
        
            x = Node(x)
            self.nodeslist[absx] = x
        
    
    def findmax(self):
        
        maximum = None
        
        for x in self.universe:
            
            absx = abs(x)
            value = self.valuelist[absx]
            
            if value != None:
                
                if maximum == None:
                    
                    maximum = value
                    
                elif value > maximum:
                        
                        maximum = value
                                             
        
        if maximum == None:
            
            print('There is no maximum element in the direct address table.')
            return maximum
        
        return maximum           
        
        
#---------------------------------------------------------------------------------------------------------------#

    def print_data(self):
        
        print(self.valuelist)


# In[23]:


U = [-1,2,4,-3,5,-7,3]

A = Direct_Address()
A.initialize()


A.insert(-1)
A.insert(4)

A.print_data()


# Each of these operations takes $O(1)$ times given how we have stored the data.

# ### 11.1.1
# 
# See the DIRECT_ADRESS class above for an implemention of a procedure that takes $O(m)$ time.

# In[24]:


A.findmax()


# ### 11.1.2
# 
# This is essentially the approach we have taken above to implement the DIRECT_ADDRESS class.

# ### 11.1.3

# In[25]:


class Direct_Address_Rep(object):
    
    def __init__(self):
    
        self.universe = U
        
        absmin = abs(min(U))
        absmax = abs(max(U))
        depth = max([absmin,absmax])
        
        self.counterlist = [None]*(depth + 1)
        self.insertedtimes = [0]*(depth + 1)
        
        self.valuelist = [None]*(depth + 1)
        self.nodeslist = [None]*(depth + 1)
        
    
    def initialize(self):
        
        for x in self.universe:
            
            absx = abs(x)
            
            if self.counterlist[absx] == None:
                
                self.counterlist[absx] = 1
            
            else:
                
                self.counterlist[absx] = self.counterlist[absx] + 1
                
                self.valuelist[absx] = [None]*self.counterlist[absx]
                self.nodeslist[absx] = [None]*self.counterlist[absx]
    
    
    def search(self, x):
        
        absx = abs(x)
        value = self.valuelist[absx]
        
        return value
    
    def insert(self,x):
        
        absx = abs(x)
        
        if self.counterlist[absx] != None:
            
            n = self.counterlist[absx]
            a = self.insertedtimes[absx]
            
            if n == 1 and a < n:
            
                self.valuelist[absx] = x
            
                x = Node(x)
                x.setValue(x)
            
                self.nodeslist[absx] = x
                
                self.insertedtimes[absx] = a + 1
        
            elif n > 1 and a < n:
        
                l = self.valuelist[absx]
                nodes = self.nodeslist[absx]
            
                
                l[a] = x
                
                x = Node(x)
                x.setValue(x)
                nodes[a] = x
                
                self.insertedtimes[absx] = a + 1
    
    
    #We remove the most recent insertion of the key in case it repeats multiple times in U.x
    
    
    def delete(self,x):
        
        absx = abs(x)
        
        if self.counterlist[absx] != None:
            
            n = self.counterlist[absx]
            a = self.insertedtimes[absx]
            
            if n == 1 and a > 0:
                
                self.valuelist[absx] = None
                self.insertedtimes[absx] = 0
                
                x = Node(x)
                
                self.nodeslist[absx] = x

            
            if n > 1 and a > 0:
                
                l = self.valuelist[absx]
                nodes = self.nodeslist[absx]
                
                l[a - 1] = None
                
                x = Node(x)
                nodes[a - 1] = x
                
                self.insertedtimes[absx] = a - 1

    
    def findmax(self):
        
        maximum = None
        
        for x in self.universe:
            
            absx = abs(x)
            a = self.insertedtimes[absx]
            
            if a > 0:
            
                if maximum == None:
                    
                    maximum = x
                    
                elif x > maximum:
                        
                    maximum = x

        if maximum == None:
            
            print('There is no maximum element in the direct address table.')
            return maximum
        
        return maximum           
        
        
#---------------------------------------------------------------------------------------------------------------#

    def print_data(self):
        
        print(self.valuelist)
        print(self.insertedtimes)


# In[26]:


U = [0,1,2,3,4,5,5,6,6,6,6,6,6,7]

A = Direct_Address_Rep()
A.initialize()

A.insert(0)
A.insert(2)
A.insert(4)
A.insert(5)
A.insert(5)
A.insert(5)
A.insert(6)
A.delete(6)
A.insert(0)
A.insert(6)
A.insert(3)
A.insert(6)

A.print_data()


# In[ ]:




