#!/usr/bin/env python
# coding: utf-8

# # Stacks 
# 
# Stacks are dynamic sets in which the element removed from the set by the DELETE operation is prespecified. In a stack, the element deleted from the set is the one most recently inserted: the stack implements a last-in, first-out, or LIFO, policy. Put in another way, a stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the SAME end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.” The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest.
# 
# Stacks are fundamentally important, as they can be used to reverse the order of items. For example, every web browser has a Back button. As you navigate from web page to web page, those pages are placed on a stack (actually it is the URLs that are going on the stack). The current page that you are viewing is on the top and the first page you looked at is at the base. If you click on the Back button, you begin to move in reverse order through the pages.
# 
# We will use lists as our primitive Python data structure to implement a stack. The attribute S.TOP indexes the most recently inserted element. The stack consists of S[1,...,S.TOP], where S[1] is the element at the bottom of the stack and S[S.TOP] is the element at the top. Think of pushing a pile of books up when you add a book to a stack; when it's time to take a book out of the stack, we take it out of the bottom.

# In[11]:


class Stack(object):
    
    def __init__(self,stack,bottom):
        self.stack = stack
        self.bottom = bottom
    
    def empty(self,stack):
        
        if self.bottom < 0:
            Boolean = True
            return Boolean
        else:
            Boolean = False
            return Boolean   
    
    def push(self,x):
        
        n = len(self.stack)
        
        if self.bottom == n - 1:
            
            print('Overflow error.')
            return None
        
        else:
        
            self.bottom = self.bottom + 1
        
            #if self.bottom == n:
        
            #    self.stack = self.stack + [x]
            
            #elif self.bottom < n:
            
            self.stack[self.bottom] = x
        
            truncated_stack = self.stack[:self.bottom+1]
        
            return self.stack, truncated_stack 
    
    def pop(self):
        
        boolean = self.empty(self.stack)
        
        if boolean == True:
            
            print('Underflow error.')
            return None
            
        else:
            
            x = self.stack[self.bottom]
            self.bottom = self.bottom - 1
            truncated_stack = self.stack[:self.bottom+1]
            
        return self.stack, truncated_stack, x


# ### 10.1.1

# In[12]:


A = [1,2,3,4,5,6]
books = Stack(A,-1)

A, A_truncated = books.push(4)
print(A,A_truncated)
A, A_truncated = books.push(1)
print(A, A_truncated)
A, A_truncated = books.push(3)
print(A, A_truncated)
A, A_truncated, x = books.pop()
print(A, A_truncated)
A, A_truncated = books.push(8)
print(A, A_truncated)
A, A_truncated, x = books.pop()
print(A, A_truncated)


# Each of the operations in the class STACK takes $O(1)$ time.

# In[15]:


A = [1,2,3,4]
books = Stack(A,-1)

A, A_truncated = books.push(5)
print(A,A_truncated)
A, A_truncated = books.push(6)
print(A, A_truncated)
A, A_truncated = books.push(7)
print(A, A_truncated)
A, A_truncated = books.push(8)
print(A, A_truncated)
#A, A_truncated = books.push(9)
#print(A, A_truncated)


# In[3]:


class Reverse_Stack(object):
    
    def __init__(self,stack,top):
        self.stack = stack
        self.top = top
    
    def empty(self,stack):
        
        n = len(stack)
        if self.top == n:
            Boolean = True
            return Boolean
        else:
            Boolean = False
            return Boolean   
    
    def pull(self,x):
        
        if self.top == -1:
            
            self.top = 1
         
        if self.top == 0:
            
            self.list = [x] + self.list
            
        else:    
    
            self.top = self.top - 1
            self.stack[self.top] = x
        
        truncated_stack = self.stack[self.top:len(self.stack)]
        
        return self.stack, truncated_stack 
    
    def pop(self):
        
        boolean = self.empty(self.stack)
        
        if boolean == True:
            
            print('Underflow error.')
            return None
            
        else:
            
            self.top = self.top + 1
            truncated_stack = self.stack[self.top:len(self.stack)]
            
        return self.stack, truncated_stack


# In[27]:


A = [1,2,3,4,5,6]
books = Reverse_Stack(A,len(A))

A, A_truncated = books.pull(4)
print(A,A_truncated)
A, A_truncated = books.pull(1)
print(A, A_truncated)
A, A_truncated = books.pull(55)
print(A, A_truncated)
A, A_truncated = books.pull(8)
print(A, A_truncated)
A, A_truncated = books.pop()
print(A, A_truncated)


# ### 10.1.2
# 
# Implement two stacks using the STACK and REVERSE STACK classes. One of the stacks can be implemented as the whole array A[1,...,n] using the STACK class; the other stack can be implemented as the empty array [] using the REVERSE STACK class. This will satisfy the criteria. For example:

# In[22]:


A = [1,2,3,4]

books = Stack(A,3)
books2 = Reverse_Stack(A,4)

A, A_truncated = books2.pull(55)
print(A,A_truncated)
A, A_truncated = books2.pull(65)
print(A,A_truncated)
#A, A_truncated = books.push(8)
#print(A, A_truncated)


# # Queues:
# 
# Queues are dynamic sets in which the element removed from the set by the DELETE operation is prespecified. In a queue, the element deleted is always the one that has been in the set for the longest time: the queue implements a first-in, first-out, or FIFO, policy. The FIFO property of a queue causes it to operate like a line of customers waiting to pay a cashier. The queue has a head and a tail. When an element is enqueued, it takes its place at the tail of the queue, just as a newly arriving customer takes a place at the end of the line. The element dequeued is always the one at the head of the queue, like the customer at the head of the line who has waited the longest.

# In[23]:


class Queue(object):
    
    def __init__(self,queue,tail,head):
        self.queue = queue
        self.tail = tail
        self.head = head
    
    def empty(self,queue):
        
        n =  self.tail - self.head + 1
        if n <= 0:
            Boolean = True
        else:
            Boolean = False
        return Boolean
    
    def enqueue(self,x):
        
        n = len(self.queue)
        Boolean = None
        
        if self.tail  >= n - 1:
            
            Boolean = True
            print('Overflow error.')
            return None
        
        elif self.head == -1:
            
            self.head = self.head + 1
        
        self.tail = self.tail + 1
        n = len(self.queue)
        
        #if self.tail == n:
        
        #    self.queue = self.queue + [x]
            
        #elif self.tail < n:
            
        self.queue[self.tail] = x
        
        truncated_queue = self.queue[self.head:self.tail+1]
        
        return self.queue, truncated_queue
 
    def dequeue(self):  
                
        Boolean = None
        if self.head < 0:
            
            Boolean = True
            print('Underflow error.')
            return None
            
        else:
            
            x = self.queue[self.head]
            self.head = self.head + 1
            truncated_queue = self.queue[self.head:self.tail+1]
            
        return self.queue, truncated_queue, x
    
    def size(self):
        
        n = self.tail - self.head + 1
        return n


# ### 10.1.3

# In[24]:


A = [1,2,3,4,5,6]
queue = Queue(A,-1,-1)

A, A_truncated = queue.enqueue(4)
print(A,A_truncated)
A, A_truncated = queue.enqueue(1)
print(A,A_truncated)
A, A_truncated = queue.enqueue(3)
print(A,A_truncated)
A, A_truncated,x = queue.dequeue()
print(A,A_truncated,x)
A, A_truncated = queue.enqueue(8)
print(A,A_truncated)
A, A_truncated, x = queue.dequeue()
print(A,A_truncated,x)


# ### 10.1.4
# 
# See code above.
# 
# ### 10.1.5

# In[25]:


class Deque(object):
    
    def __init__(self,dqueue,tail,head):
        self.dqueue = dqueue
        self.tail = tail
        self.head = head
    
    def empty(self,dqueue):
        
        n =  self.tail - self.head + 1
        
        if n <= 0:
            Boolean = True
        else:
            Boolean = False
        
        return Boolean    
    
    def tail_enqueue(self,x):
        
        n = len(self.dqueue)
        
        if self.tail >= n - 1:
            
            Boolean = True
            print('Overflow error.')
            return None
        
        elif self.head == -1:
            
            self.head = self.head + 1
        
        self.tail = self.tail + 1
            
        self.dqueue[self.tail] = x
        
        truncated_dqueue = self.dqueue[self.head:self.tail+1]
        
        return self.dqueue, truncated_dqueue
    
    def head_dequeue(self):
        
        if self.head < 0:
            
            Boolean = True
            print('Underflow error.')
            return None
            
        else:
            
            x = self.dqueue[self.head]
            self.head = self.head + 1
            truncated_dqueue = self.dqueue[self.head:self.tail+1]
            
        return self.dqueue, truncated_dqueue, x
    
    def head_enqueue(self,x):
        
        if self.head == -1:
            
            self.dqueue, truncated_dqueue = self.tail_enqueue(x)
            
            return self.dqueue, truncated_dqueue 
        
        if self.head == 0:
            
            self.dqueue = [x] + self.dqueue
            self.tail = self.tail + 1
            truncated_dqueue = self.dqueue[self.head:self.tail+1]
            
        else:
            
            self.head = self.head - 1
            self.dqueue[self.head] = x
        
        truncated_dqueue = self.dqueue[self.head:self.tail+1]
        
        return self.dqueue, truncated_dqueue
    
    def tail_dequeue(self):
            
        if self.tail == -1:
            
            print('Underflow error.')
            return None
        
        elif self.tail == 0:
            
            self.dqueue, truncated_dqueue = self.head_dequeue(x)
            return self.dqueue, truncated_dqueue 
        
        else:
            
            x = self.dqueue[self.tail]
            self.tail = self.tail - 1
            truncated_dqueue = self.dqueue[self.head:self.tail+1]
            return self.dqueue, truncated_dqueue, x
    
    def size(self):
        
        n = self.tail - self.head + 1
        return n


# In[26]:


A = [1,2,3,4,5,6]
dqueue = Deque(A,-1,-1)

A, A_truncated = dqueue.head_enqueue(4)
print(A,A_truncated)
A, A_truncated = dqueue.head_enqueue(1)
print(A,A_truncated)
A, A_truncated = dqueue.tail_enqueue(3)
print(A,A_truncated)
A, A_truncated = dqueue.tail_enqueue(10)
print(A,A_truncated)
A, A_truncated = dqueue.tail_enqueue(55)
print(A,A_truncated)
A, A_truncated,x = dqueue.tail_dequeue()
print(A,A_truncated,x)
A, A_truncated = dqueue.tail_enqueue(7)
print(A,A_truncated)
A, A_truncated = dqueue.tail_enqueue(8)
print(A,A_truncated)
A, A_truncated = dqueue.tail_enqueue(11)
print(A,A_truncated)
A, A_truncated = dqueue.head_enqueue(-1)
print(A,A_truncated)
A, A_truncated,x = dqueue.head_dequeue()
print(A,A_truncated,x)
A, A_truncated,x = dqueue.tail_dequeue()
print(A,A_truncated,x)


# ### 10.1.6
# 
# Let's implement a queue using the two stack classes. Here we use the STACK abd REVERSE_STACK classes to implement our queue. The two different stack classes allow us to manipulate the head and the tail of the queue independently.

# In[28]:


class Queue_From_Stacks(object):
    
    def __init__(self,queue,tail,head):
        self.queue = queue
        self.tail = tail
        self.head = head
        
    def empty(self,queue):
        
        n =  self.tail - self.head + 1
        if n <= 0:
            Boolean = True
        else:
            Boolean = False
        return Boolean  
    
    def enqueue(self,x):
        
        n = len(self.queue)
        if self.tail >= n - 1:
            
            print('Overflow error.')
            return None
        
        if self.head == -1:
            
            self.head = self.head + 1
        
        books = Stack(self.queue,self.tail)
        self.queue, truncated_queue = books.push(x)
        self.tail = self.tail + 1
        truncated_queue = self.queue[self.head:self.tail+1]
        
        return self.queue, truncated_queue 
    
    def dequeue(self):  
                
        if self.head < 0:
            
            print('Underflow error.')
            return None
            
        else:
            
            x = self.queue[self.head]
            books = Reverse_Stack(self.queue,self.head)
            self.queue, truncated_queue = books.pop()
            self.head = self.head + 1
            truncated_queue = self.queue[self.head:self.tail+1]
            
        return self.queue, truncated_queue, x    


# In[29]:


A = [1,2,3,4,5,6]
queue = Queue_From_Stacks(A,-1,-1)

A, A_truncated = queue.enqueue(4)
print(A,A_truncated)
A, A_truncated = queue.enqueue(1)
print(A,A_truncated)
A, A_truncated = queue.enqueue(3)
print(A,A_truncated)
A, A_truncated,x = queue.dequeue()
print(A,A_truncated,x)
A, A_truncated = queue.enqueue(8)
print(A,A_truncated)
A, A_truncated, x = queue.dequeue()
print(A,A_truncated,x)


# If we are constrained to use the first class to implement the STACK procedure, then note that another way to implement a queue using two stacks is as follows:
# 
# Consider two stacks $A$ and $B$. ENQUEUE pushes elements on  $B$. DEQUEUE pops elements from  $A$. If 
# $A$ is empty, the contents of $B$ are transfered to $A$ by popping them out of $B$ and pushing them to $A$. That way they appear in reverse order and are popped in the original. 
# 
# Let's implement this alternative idea.

# In[79]:


class Queue_From_Stacks2(object):
    
    def __init__(self,queue,tail,head):
        self.queue = queue
        self.tail = tail
        self.head = head
        
    def empty(self,queue):
        
        n =  self.tail - self.head + 1
        if n <= 0:
            Boolean = True
            return Boolean
        else:
            Boolean = False
            return Boolean
    
    def enqueue(self,x):
        
        if self.head == -1:
            
            self.head = self.head + 1
        
        books = Stack(self.queue,self.tail)
        self.queue, truncated_queue = books.push(x)
        self.tail = self.tail + 1
        truncated_queue = self.queue[self.head:self.tail+1]
        
        return self.queue, truncated_queue     
    
    
    def dequeue(self,running_stack,running_bottom):
        
        n = len(running_stack)
        books = Stack(self.queue,self.tail)
        books2 = Stack(running_stack,running_bottom)
            
        if n == 0:
            
            for key in range(self.tail,self.head-1,-1):
                
                stack, truncated_stack, x = books.pop()
                running_stack, truncated_running_stack = books2.push(x)
                running_bottom = running_bottom + 1
                truncated_running_stack = running_stack[:running_bottom+1]
                
            a, b, x = books2.pop()  
            running_bottom = running_bottom - 1
            running_stack = b
            
            z = self.head
            
            for key in range(running_bottom,-1,-1):
                
                self.queue[z] = running_stack[key]
                z = z + 1
                
            self.tail = z - 1
            truncated_queue = self.queue[self.head:self.tail+1]
            
            return running_stack, running_bottom, self.queue, truncated_queue
        
        else:
            
            a, b, x = books2.pop()  
            running_bottom = running_bottom - 1
            running_stack = b
            
            self.head = self.head + 1
            self.queue = self.queue[self.head:self.tail+1]
            truncated_queue = self.queue[self.head:self.tail+1]
            
            return running_stack, running_bottom, self.queue, truncated_queue         


# In[80]:


A = []
queue = Queue_From_Stacks2(A,-1,-1)
running_stack = []
running_bottom = -1

A, A_truncated = queue.enqueue(1)
print(A,A_truncated)
A, A_truncated = queue.enqueue(2)
print(A,A_truncated)
A, A_truncated = queue.enqueue(3)
print(A,A_truncated)
A, A_truncated = queue.enqueue(4)
print(A,A_truncated)
A, A_truncated = queue.enqueue(5)
print(A,A_truncated)
running_stack, running_bottom, A, A_truncated = queue.dequeue(running_stack,running_bottom)
print(A,A_truncated,running_stack, running_bottom)
A, A_truncated = queue.enqueue(6)
print(A,A_truncated)
running_stack, running_bottom, A, A_truncated = queue.dequeue(running_stack,running_bottom)
print(A,A_truncated,running_stack, running_bottom)


# ### 10.1.7

# In[ ]:




