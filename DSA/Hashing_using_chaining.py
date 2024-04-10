"""
To fix collision we have:
Open Addressing --> 1. Linear probing --> Baju wale index me dal do
                    2. Quadratic probing --> square karke index nikalke daldo

Closed Addressing --> 1. Chaining 
In chaining we create array of linked list. 
we have a fixed index which is bucket index where we keep on adding linked list Node. 

"""

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None #Empty LL has self.head None
        self.n = 0 #Total number of nodes in the LL

    def size(self):
        return self.n

    
    def insert_head(self,value):
        new_node = Node(value) #creating a new node object, new_node.data = value, new_node.next=None
        
        new_node.next = self.head #For the first node self.head will be None
        print(new_node.next)
        self.head = new_node #reassign self.head as the address of new_node, for eg --> <__main__.Node object at 0x0000018A22431CC0>
        print(self.head)

        self.n += 1

    def append_node_end(self,key,value):
        new_node = Node(key,value) #new_node.data = value, new_node.next = None
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

    
    

    def delete_item(self,key):
        if self.head == None:
            #empty
            return 'Empty LL'
        curr = self.head
        if curr.key == key:
            return self.delete_from_head()
        while curr.next != None:
            if curr.next.key == key:
                break
            curr = curr.next

        # 2 cases item mil gata
        # item nahi mila
        if curr.next == None:
            return 'not found'
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self,key):
        #will return the index pos of the item
        curr = self.head
        pos = 0
        while curr != None:
            if curr.key == key:
                return pos
            curr = curr.next
            pos += 1
        return -1
    
    def traverse(self):
        
        curr = self.head
        
        while curr != None:
            print(curr.key, '-->', curr.value, end= ' ' )
            curr = curr.next
        return ' '
            
        
    
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
    
    def get_node_at_index(self,index):
        temp = self.head
        cnt = 0
        while temp != None:
            if cnt == index:
                return temp 
            temp = temp.next
            cnt += 1
        

#-------------------------------------------------------------------------------#
class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # create array of LL
        self.buckets = self.make_array(self.capacity)

    def make_array(self,capacity):
        L =[]

        for i in range(capacity):
            L.append(LinkedList()) # creating a list/array of linked list objects
        return L
    
    def put(self,key, value):
        bucket_index = self.hash_function(key)
        print(bucket_index)

        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            #insert new element
            self.buckets[bucket_index].append_node_end(key,value)
            self.size += 1

            load_factor = self.size/self.capacity
            print(load_factor)
            if (load_factor >= 2):
                self.rehash()
        else:
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value
            
            #update ka case

    def delete(self,key):
        bucket_index = self.hash_function(key)

        self.buckets[bucket_index].delete_item(key)

        self.size -= 1


    def __setitem__(self,key,value):
        self.put(key,value)

    def __getitem__(self,key):
        return self.get(key)
    
    def __delitem__(self,key):
        return self.delete(key)

    

    def get(self,key):
        bucket_index = self.hash_function(key)
        res = self.buckets[bucket_index].search(key)

        if res==-1:
            return 'Not Found'
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.value
        
    def rehash(self):
        self.capaciy = self.capacity * 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        for i in old_buckets:
            for j in range(i.size()):
                node = i.get_node_at_index(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item,value_item)


    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search(key)   #this is LL object inside Bucket array
        
        return node_index

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity
    
D = Dictionary(2)
D.put('python', 34)
D.put('Java',56)
D.put('php',563)
res = D['python']
res1 = D.get('Java')

print(f'for php it is {res}')

del D['php']
print(D['php'])


print(f'for Java it is {res1}')
    