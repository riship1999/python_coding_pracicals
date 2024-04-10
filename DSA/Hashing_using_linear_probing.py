"""
Hashing is a technique used to make search faster.

we use a hash function to set the index of the element 
Hash function  = (i % size)

lets say we want to insert = {32,41,37,24,16} in an array using linear probing ; size = 5
hash function -- > i % size 
for i = 32, (32%5) = 2, so at index=2 we will have 32
for i = 41, (41%5) = 1, so at index=1 we will have 41
for i = 37, (37%5) = 2, so at index=2 we already have 41. This is collision.

To fix collision we have:
Open Addressing --> 1. Linear probing --> Baju wale index me dal do
                    2. Quadratic probing --> square karke index nikalke daldo

LINEAR PROBING hash function --> h(i) = [g(i) + k(i')] % size  , g(i) = i % size
for above case
For i = 37 [(37%5) + i'=0] % size=5 --> 2 (but index=2 is occupied by 32), So using linear probing i'=1
i = 37 [(37%5) + i'=1] % size=5 --> 3, so at index=3 we will have 37

For i = 24 [(24%5) + i'=0] % size=5 --> 4, so at index=4 we will have 24.

For i = 16 [(16%5) + i'=0] % size=5 --> 1 (but index=1 is occupied by 41), 
Now i'=1   [(16%5) + i'=1] % size=5 --> 2 (but index=2 is occupied by 32),
Now i'=2   [(16%5) + i'=2] % size=5 --> 3 (but index=3 is occupied by 37),
Now i'=3   [(16%5) + i'=3] % size=5 --> 4 (but index=4 is occupied by 24),
Now i'=4   [(16%5) + i'=4] % size=5 --> 0 so at index=0 we will have 16.

Now after linear probing our array will look like:
    element --> 16 , 41 , 32 , 37 , 24
    index   --> 0  , 1  , 2  , 3  , 4


"""

class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size #this array is for keys
        self.data = [None] * self.size #this array is for values

    def put(self,key,value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == None: #insert new key,value 
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key: #updating already existing key ka value
                self.data[hash_value] = value
            else:
                # immitating the linear probing mechanism by incrementing/rehashing until we find empty position
                # or index  
                new_hash_value = self.rehash(hash_value)
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    #key already exists so to update that key
                    self.data[new_hash_value] = value

    def __setitem__(self,key,value):
        # this magic method is used to set element using  d['python'] = 45
        self.put(key,value)

    def __getitem__(self,key):
        #this magic method is used to get element using d['python']
        return self.get(key)
    
    def __str__(self):
        for i in range(self.size):
            print(f'{self.slots[i]} : {self.data[i]}')
        return ''

    def get(self,key):
        start = self.hash_function(key)
        current_position = start

        while self.slots[current_position] != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            current_position = self.rehash(current_position)
            if current_position == start:
                return 'Not Found'
        return 'Not found None wala'

            
        
    def rehash(self,old_hash):
        return (old_hash +1) % self.size

    def hash_function(self,key):
        """
        Only immutable data-types can be hashed
        mutable datatypes like list, set, dictionary cannot be hashed

        We are using abs() because key can be a string which can have negative hash value.

        This hash function is used to generate the index position to which key can be inserted in self.slots array
        and to same index position value will be inserted in self.data array
        """
        return abs(hash(key)) % self.size 
    
d = Dictionary(3)
print(d.slots)
print(d.data)
d.put('python',45)
d.put('java',46)
d['cpp'] = 7 # we are able to use this notation because of setitem method
print(d.get('cppp'))
print(d['cpp'])


print(d.slots)
print(d.data)
print(d)

"""
This will give a error
d[[1,2,4]] = 10 
Since list is used as key and lists are mutable so they cannot be hashed

"""
