    #                       Circular Singly Linked List

  # defines the node in a linked list.
class Node: 
    def __init__(self,data): 
        self.data=data 
        self.next=None


  # defines the linked list and its operations.
class CSLL: 
    def __init__(self): 
        self.head=None 
        self.tail=None 

      # finds whether any node in linked list has the value.
    def find(self,val): 
        if(self.head==None): 
            return False 
        temp=self.head 
        while(temp.next!=self.head): 
            if(temp.data==val): 
                return True 
            temp=temp.next 
        if(temp.data==val): 
            return True 
        return False 

      # inserts new node with given value at the end of the linked list.
    def append(self,val): 
        node=Node(val)
        if(self.head==None):    
            self.head=self.tail=node   
            self.tail.next=self.head 
            return 
        node.next=self.head 
        self.tail.next=node 
        self.tail=node 

      # inserts new node with given value at the beginning of the linked list.
    def push(self,val): 
        node=Node(val)
        if(self.head==None):    
            self.head=self.tail=node    
            self.tail.next=self.head 
            return 
        node.next=self.head 
        self.tail.next=node
        self.head=node 

      # deletes the last node of the linked list.
    def pop(self): 
        if(self.head==None): 
            return 
        if(self.head==self.tail): 
            self.head=None 
            return
        temp=self.head 
        while(temp.next.next!=self.head):       
            temp=temp.next 
        temp.next=self.head 
        self.tail=temp 

      # deletes the first node of the linked list.
    def popFront(self): 
        if(self.head==None): 
            return 
        if(self.head==self.tail): 
            self.head=None 
            return 
        self.tail.next=self.head.next 
        self.head=self.head.next 

      # displays the values of all nodes, one by one.
    def traverse(self): 
        if(self.head==None): 
            print("None")
            return 
        temp=self.head 
        while(temp.next!=self.head): 
            print(temp.data,end=" -> ") 
            temp=temp.next 
        print(temp.data,end=" -> ")
        print()