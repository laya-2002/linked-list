    #                       Singly Linked List

  # defines the node in a linked list.
class Node: 
    def __init__(self,data):    
        self.data=data 
        self.next=None 


  # defines the linked list and its operations.
class SLL: 
    def __init__(self): 
        self.head=None 
    
      # finds whether any node in linked list has the value.
    def find(self,data): 
        temp=self.head 
        while(temp!=None): 
            if(temp.data==data): 
                return True 
            temp=temp.next 
        return False 
    
      # inserts new node with given value at the end of the linked list.
    def append(self,val): 
        if(self.head==None):    
            self.head=Node(val)    
            return 
        temp=self.head 
        while(temp.next!=None): 
            temp=temp.next
        temp.next=Node(val) 
    
      # inserts new node with given value at the beginning of the linked list.
    def push(self,val): 
        temp=Node(val) 
        temp.next=self.head 
        self.head=temp  
    
      # inserts new node before the node with given value (if the value is present).
    def insertBefore(self,data,val): 
        if(self.head==None): 
            return 
        if(not self.find(data)): 
            return 
        node=Node(val)
        if(self.head.data==data): 
            node.next=self.head 
            self.head=node 
            return 
        temp=self.head 
        while(temp.next!=None): 
            if(temp.next.data==data): 
                node.next=temp.next 
                temp.next=node 
                break 
            temp=temp.next
    
      # inserts new node after the node with given value (if the value is present).
    def insertAfter(self,data,val): 
        if(self.head==None): 
            return 
        if(not self.find(data)): 
            return 
        temp=self.head 
        node=Node(val)
        while(temp!=None): 
            if(temp.data==data): 
                node.next=temp.next 
                temp.next=node 
                break 
            temp=temp.next 
    
      # deletes the first node of the linked list.
    def popFront(self): 
        if(self.head==None): 
            return 
        if(self.head.next==None): 
            self.head=None 
            return 
        self.head=self.head.next 
    
      # deletes the last node of the linked list.
    def pop(self): 
        if(self.head==None): 
            return 
        if(self.head.next==None): 
            self.head=None 
            return 
        temp=self.head 
        while(temp.next.next!=None): 
            temp=temp.next 
        temp.next=None 
    
      # deletes the node present before the node with given value (if the value is present).
    def popBefore(self,data):      
        if(self.head==None): 
            return 
        if(self.head.data==data): 
            return 
        if(not self.find(data)): 
            return 
        if(self.head.next.data==data): 
            self.head=self.head.next 
            return 
        temp=self.head 
        while(temp.next.next!=None): 
            if(temp.next.next.data==data):   
                temp.next=temp.next.next 
                break 
            temp=temp.next 
    
      # deletes the node present after the node with given value (if the value is present).
    def popAfter(self,data): 
        if(self.head==None): 
            return 
        if(self.head.next==None):    
            return 
        if(not self.find(data)):       
            return 
        temp=self.head 
        while(temp.next!=None): 
            if(temp.data==data): 
                temp.next=temp.next.next 
                break 
            temp=temp.next 
        if(temp.data==data): 
            return 
    
      # displays the values of all nodes, one by one.
    def traverse(self): 
        temp=self.head 
        while(temp!=None):      
            print(temp.data,"->",end=" ")     
            temp=temp.next 
        print(None)