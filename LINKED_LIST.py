  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    #for printing last Entry only
    def printEnd(self):
        temp = self.head 
        while (temp.next!=None): 
            #print(temp.data) 
            temp = temp.next
        print("Seat No\t\tPRN\t\tName\t\tGender\t\tAge")
        print(temp.data[0],"\t   ",temp.data[1],"\t    ",temp.data[2],"\t\t",temp.data[3],"\t",temp.data[4])
            
    # for display all data
    def printList(self): 
        print("Seat No\t\tPRN\t\tName\t\tGender\t\tAge")
        
        temp = self.head 
        while (temp): 
            print(temp.data[0],"\t   ",temp.data[1],"\t    ",temp.data[2],"\t\t",temp.data[3],"\t",temp.data[4])
            temp = temp.next
    
    # This function is in LinkedList class 
    # Function to insert a new node at the beginning 
    def insertBegin(self, new_data): 
    
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
        if self.head ==None:

            # 3. Make next of new Node as head 
            self.head = new_node
            return
        new_node.next=self.head
        # 4. Move the head to point to new Node  
        self.head = new_node
    # Inserts a new node after the given prev_node. This method is  
    # defined inside LinkedList class shown above */ 
    def insertAfter(self, prev_node, new_data): 
    
        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print("The given previous node must inLinkedList.")
            return
    
        #  2. Create new node & 
        #  3. Put in the data 
        new_node = Node(new_data) 
    
        # 4. Make next of new Node as next of prev_node  
        new_node.next = prev_node.next
    
        # 5. make next of prev_node as new_node  
        prev_node.next = new_node
        print("\n%d is Inserted" %new_data)
    
    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    #  defined inside LinkedList class shown above */ 
    def insertEnd(self, new_data): 
       
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
        
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
                self.head = new_node 
                #print("\n%d is Inserted" %new_data)
                return
        
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
        
        # 6. Change the next of last node 
        last.next =  new_node
        #print("\n%d is Inserted" %new_data)
    
    def deleteNode(self, key): 
          
        # Store head node 
        temp = self.head 
        if temp==None:
            self.head=None
        # If head node itself holds the key to be deleted 
        if (temp is not None): 
            if (temp.data[0] == key): 
                self.head = temp.next
                temp = None
                #print("\n%d is Deleted" %key)
                return
  
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(temp is not None): 
            if temp.data[0] == key: 
                break 
            prev = temp 
            temp = temp.next 
  
        # if key was not present in linked list 
        if(temp == None): 
            return 
  
        # Unlink the node from linked list 
        prev.next = temp.next 
  
        temp = None 
        #print("\n%d is Deleted" %key)

    # for calculating size of list  
    def size(self):
        size=0
        temp=self.head
        while temp != None:
            size+=1
            temp=temp.next
        return size

    # for searching seat no in list
    def linearsearch(self,key):
        if self.head==None:
            print("\nNo Data Is Present in List")
            return
        temp=self.head
        while temp!=None:
            if temp.data[0]==key:
                print("\n%d Seat is available" %key)
                return
            temp=temp.next
        print("\n%d is Seat is not availavle" %key)

    # for assigning present , absent status
    def assign_status(self,newlinkedlist):

        if self.head==None:
            print("\nNo Data is Present")
        size=self.size()
        temp=self.head
        i=1
        while(i<=size):
            newlinkedlist.insertEnd([temp.data[0],"Present"])
            i=i+1
            temp=temp.next
        
        temp1=newlinkedlist.head
        print("\nSeat No.\tStatus")
        while(temp1!=None):
            print(temp1.data[0],"\t\t",temp1.data[1])
            temp1=temp1.next
