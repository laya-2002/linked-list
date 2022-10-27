    #                       Doubly Linked List

  # defines the node in a linked list.
class Node: 
    def __init__(self,data):     
        self.data=data 
        self.prev=None 
        self.next=None 


  # defines the linked list and its operations.
class DLL: 
    def __init__(self): 
        self.head=None 
        self.tail=None 
    
      # finds whether any node in linked list has the value.      
    def find(self,key): 
        temp=self.head 
        while(temp!=None):     
            if(temp.data==key): 
                return True 
            temp=temp.next 
        return False 

      # inserts new node with given value at the end of the linked list.
    def append(self,val): 
        node=Node(val)
        if(self.head==None): 
            self.head=self.tail=node       
            return 
        node.prev=self.tail 
        self.tail.next=node  
        self.tail=node 

      # inserts new node with given value at the beginning of the linked list.
    def push(self,val): 
        node=Node(val) 
        if(self.head==None):     
            self.head=self.tail=node 
            return 
        node.next=self.head 
        self.head.prev=node 
        self.head=node 

      # inserts new node before the node with given value (if the value is present).
    def insertBefore(self,data,val): 
        if(self.head==None): 
            return 
        if(not self.find(data)): 
            return 
        node=Node(val) 
        if(self.head.data==data): 
            node.next=self.head 
            self.head.prev=node 
            self.head=node 
            return 
        temp=self.head 
        while(temp!=None): 
            if(temp.data==data): 
                node.next=temp 
                node.prev=temp.prev 
                temp.prev.next=node 
                temp.prev=node 
                break 
            temp=temp.next 

      # inserts new node after the node with given value (if the value is present).
    def insertAfter(self,data,val): 
        if(self.head==None): 
            return
        if(not self.find(data)): 
            return 
        node=Node(val) 
        if(self.tail.data==data): 
            node.prev=self.tail 
            self.tail.next=node 
            self.tail=node 
            return 
        temp=self.head 
        while(temp.next!=None): 
            if(temp.data==data): 
                node.prev=temp 
                node.next=temp.next 
                temp.next.prev=node 
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
        self.head.prev=None 

      # deletes the last node of the linked list.
    def pop(self): 
        if(self.head==None): 
            return 
        if(self.head.next==None): 
            self.head=None 
            return 
        self.tail=self.tail.prev 
        self.tail.next=None 

      # deletes the node present before the node with given value (if the value is present).
    def popBefore(self,data): 
        if(self.head==None): 
            return 
        if(self.head.next==None): 
            return 
        if(not self.find(data)): 
            return 
        if(self.head.data==data): 
            return 
        if(self.head.next.data==data): 
            self.head=self.head.next 
            return 
        temp=self.head 
        while(temp.next!=None): 
            if(temp.next.data==data): 
                temp.next.prev=temp.prev
                temp.prev.next=temp.next 
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
        if(self.head.data==data):      
            self.head.next=self.head.next.next 
            self.head.next.prev=self.head 
            return 
        if(self.tail.prev.data==data): 
            self.tail=self.tail.prev 
            self.tail.next=None 
            return 
        temp=self.head.next 
        while(temp!=None): 
            if(temp.prev.data==data):
                temp.prev.next=temp.next  
                temp.next.prev=temp.prev 
                break 
            temp=temp.next 

      # displays the values of all nodes, one by one.
    def traverse(self): 
        temp=self.head 
        print(None,end=" <-> ")
        while(temp!=None): 
            print(temp.data,"<->",end=" ")
            temp=temp.next 
        print(None)
