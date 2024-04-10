"""
A Linked List is a collection of Node Objects
A Node Object consists of 2 parts:
data and Next
Data consists of the value
Next consists of the Address of the next node

The first node in linked list is called head 
The last node in linked list is called tail
the next of tail node is None

"""
"""
Lets Create Node class for Node object

"""

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None #Empty LL has self.head None
        self.n = 0 #Total number of nodes in the LL

    def __len__(self):
        return self.n
    
    def __str__(self) -> str:
        curr = self.head
        res = ''
        while curr != None:
            res = f' {res} data = {str(curr.data)} , next = {str(curr.next)} -->'
            curr = curr.next
        return res[:-3]
    
    def insert_head(self,value):
        new_node = Node(value) #creating a new node object, new_node.data = value, new_node.next=None
        print(new_node)
        new_node.next = self.head #For the first node self.head will be None
        print(new_node.next)
        self.head = new_node #reassign self.head as the address of new_node, for eg --> <__main__.Node object at 0x0000018A22431CC0>
        print(self.head)

        self.n += 1

    def append_node_end(self,value):
        new_node = Node(value) #new_node.data = value, new_node.next = None
        if self.head == None:
            #when append_node_end is called on empty LL self.head = None , empty LL
            self.head = new_node
            self.n += 1
        else: 
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node #at this point curr is at last node
            self.n += 1
    
    def insert_after_value(self,after_val,val_to_insert):
        new_node = Node(val_to_insert) # new_node.data = val_to_insert, new_node.next = None
        curr = self.head
        while curr != None:
            if curr.data == after_val:
                new_node.next = curr.next
                curr.next =  new_node
                self.n += 1
                
            curr = curr.next
        else:
            print('after_val nahi h Lodu')
        
    #delete functions
    def clear(self):
        #will make the LL empty
        self.head = None
        self.n = 0
    
    def delete_from_head(self):
        if self.head == None:
            #empty
            print('LL empty nothing to delete')
        self.head = self.head.next
        self.n -= 1

    def delete_from_tail(self):
        if self.head == None:
            #empty
            return 'Empty LL'
        curr = self.head
        if curr.next == None:
            #Kya linked list me sirf ek item hai?
            return self.delete_from_head()
            
        
        while curr.next.next != None:
            curr = curr.next
        
        curr.next = None #curr points second last node at this point
        self.n -= 1

    def delete_item(self,item):
        if self.head == None:
            #empty
            return 'Empty LL'
        curr = self.head
        if curr.data == item:
            return self.delete_from_head()
        while curr.next != None:
            if curr.next.data == item:
                break
            curr = curr.next

        # 2 cases item mil gata
        # item nahi mila
        if curr.next == None:
            return 'not found'
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self,item):
        #will return the index pos of the item
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'Not found'
    
    def __getitem__(self,index):
        #this magic method is used to find value/element from index [] 
        curr = self.head
        pos = 0
        
        while curr != None:
            if index == pos:
                return curr.data
            curr = curr.next
            pos += 1
        return 'index error'
        
    def replace_max_with_val(self,val):
        #Replace the maximum value in the LL with val for example if LL is 1-->2-->19-->4, val = 3 then
        #replace 19 with 3
        curr = self.head
        maximum = curr
        while curr != None:
            if curr.data > maximum.data:
                maximum = curr
            curr = curr.next
        maximum.data = val

    def sum_of_odd_elements_in_LL(self):
        cnt = 0
        su = 0
        curr = self.head
        while curr != None:
            if cnt %2 != 0:
                su = su + curr.data
            curr = curr.next
            cnt += 1
        return f'sum of elements at odd position is {su}'

"""
when needed to go till None ---> while curr != None
when needed to go till last node ---> while curr.next != None
when needed to go till second last node ---> while curr.next.next != None
"""
# write a python program to print LL in reverse order , 
# FROM this LL -->(data=1,next=address of 2 -->data=2,next=address of 3 -->data=3,next=address of 4 --> data=4,next=None)
# TO this LL -->(data=1,next=None <--data=2,next=address of 1 <--data=3,next=address of 2 <-- data=4,next=address of 3)          


L = LinkedList()
L.insert_head(1) 
L.insert_head(2) 
L.insert_head(3)
L.append_node_end(4)
L.insert_head(5)
L.insert_after_value(4,30)
L.replace_max_with_val(20)

print(len(L))   
print(f'after all insert LL {L}')    
print(L.sum_of_odd_elements_in_LL())
# L.delete_from_head()
# L.delete_from_tail()
# L.delete_from_tail()
# L.delete_item(30)
# L.delete_item(2)
# L.delete_item(5)
# print(L.delete_item(500))
# L.delete_item(3)
# print(L.delete_item(300))
#L.delete_item(4)
#print(L.delete_item(1))

# print(f'index of 3 is {L.search(4)}')
# print(f'At index 5 of LL we have {L[5]}')
# print(L.delete_item(1))



# L.delete_from_tail()
# L.delete_from_tail()
# L.delete_from_tail()
# print(L.delete_from_tail())
#L.clear()
    

# a = Node(5)
# print(a.data)
# print(f'a address {id(a)}')
# b = Node(6)
# print(f'b address {id(b)}')
# c = Node(7)
