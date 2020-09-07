#!/usr/bin/env python
# coding: utf-8

# # Representing Rooted Trees
# 
# 
# The methods for representing lists given in the previous section extend to any homogeneous data structure. We represent each node of a tree by an object. As with linked lists, we assume that each node contains a key attribute. The remaining attributes of interest are pointers to other nodes, and they vary according to the type of tree.
# 
# We represent a binary tree using the doubly linked list data structure. We implement the binary tree assuming each node has a distinct key.

# In[4]:


class Node(object):
    
    def __init__(self,initdata):
        self.data = initdata
        self.leftchild = None
        self.rightchild = None
        self.parent = None

    def getData(self):
        return self.data

    def getLeftchild(self):
        return self.leftchild
    
    def getRightchild(self):
        return self.rightchild

    def getParent(self):
        return self.parent
    
    def setData(self,newdata):
        self.data = newdata

    def setLeftchild(self,newleftchild):
        self.leftchild = newleftchild
        
    def setRightchild(self,newrightchild):
        self.rightchild = newrightchild
        
    def setParent(self,newparent):
        self.parent = newparent


# In[5]:


class BinaryTree_DLinkedList(object):
    
    def __init__(self):
        self.root = None   
        self.nodedic = {}     

    def getRoot(self):
        
        return self.root
    
    def getNodedic(self):
        
        return self.nodedic
    
    
    def setRoot(self,newroot):
        
        self.root = newroot
   

    def empty(self):
        
        if len(list(self.nodedic)) == 0:
            
            print('The binary tree is empty.')
            return None
        
        else:
            
            print('The binary tree is not empty.')
            return None
    
    
    def add(self,x,left,right,root):
        
        if x in self.nodedic:
            
            x = self.nodedic[x]
            
        else:
            
            x = Node(x)

        if left != None:
            
            if left in self.nodedic:
                
                y = self.nodedic[left]
            
                if self.root == None or self.root.getData() != left:
                
                    y.setParent(x)
                
                x.setLeftchild(y)
                
                self.nodedic[left] = y
                
            else:    
                
                y = Node(left)
                
                if self.root == None or self.root.getData() != left:
                
                    y.setParent(x)
                
                x.setLeftchild(y)
            
                self.nodedic[y.getData()] = y
        
        if right != None:
            
            if right in self.nodedic:
                
                z = self.nodedic[right]
        
                if self.root == None or self.root.getData() != right:
                    
                    z.setParent(x)
                
                x.setRightchild(z)
                
                self.nodedic[right] = z
                
            else:
                
                z = Node(right)
                
                if self.root == None or self.root.getData() != right:
                
                    z.setParent(x)
                
                x.setRightchild(z)
            
                self.nodedic[z.getData()] = z
        
        self.nodedic[x.getData()] = x
        
        if root == True:
            
            self.root = x
            
    def printnodedata(self):
        
        for key in self.nodedic:
            
            x = self.nodedic[key]
        
        
            print('Key =', x.getData())
        
            a = x.getParent()
        
            if a != None:
            
                print('Parent =',a.getData())
            
            else:
            
                print('Parent = None')
            
            b = x.getLeftchild()    
        
            if b != None:
            
                print('Left Child =',b.getData())
            
            else:
            
                print('Left Child = None')
                     
            c = x.getRightchild()
        
            if c != None:
            
                print('Right Child =',c.getData())
            
            else:
            
                print('Right Child = None')
            
            print('-------------------------')   


# ### 10.4.1

# In[6]:


Tree = BinaryTree_DLinkedList()

Tree.add(12,7,4,None)
Tree.add(15,14,None,None)
Tree.add(4,5,None,None)
Tree.add(10,2,21,None)
Tree.add(2,None,None,None)
Tree.add(18,12,10,True)
Tree.add(7,None,None,None)
Tree.add(14,18,15,None)
Tree.add(21,None,None,None)
Tree.add(5,None,None,None)

Tree.printnodedata()


# In[ ]:




