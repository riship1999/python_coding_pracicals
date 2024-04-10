"""
Creating C- type array using python and implementing python list like functions - append(), insert(), 
search() etc
"""

import ctypes

class MeraList():
    def __init__(self):
        self.size = 1  #indicates the size of array
        self.n = 0 #indicates the number of elements in an array 

        self.A = self.__make_array(self.size) #creates a C type array of size = self.size

    def __make_array(self,capacity):
        #returns/creates a C type array (static, referential) of size = capacity
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        # __len__() magic method is triggered when obj is passed as argument to len --> len(obj)
        return self.n 
    
    def append(self,value):
        if self.size == self.n:
            # when the current arrray is full
            self.__resize(self.size*2)
        
        self.A[self.n] = value
        self.n += 1   

    def pop(self):
        if self.n == 0:
            return "Empty List"
        
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def find_index(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in the list'
    
    def insert(self,index,value):
        if 0<=index<self.n:
            if self.size == self.n:
                self.__resize(self.size*2)


            for i in range(self.n,index,-1):
                self.A[i] = self.A[i-1]
            self.A[index]=value
            self.n = self.n+1
            return f' at index {index} the value {value} inserted'
        else:
            return 'IndexErr'
    
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1

    def remove(self,element):
        for i in range(self.n):
            if self.A[i] == element:
                self.__delitem__(i)

    
    def __resize(self,new_capacity):
        #create an new array of size new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of purana array to new array B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __getitem__(self,index):
        #It will return the item from the index when it is called as object[index] using [] brackets 
        if 0<=index<self.n:
            return self.A[index]
            


    def __str__(self) -> str:
        #should print something like [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + f'{self.A[i]},'
        return f'[{result[:-1]}] len = {self.n}'
    

L = MeraList()
L.append('hello')
L.append(10)
L.append(3.5)
L.append(40)
print(L)
print(len(L))
del L[1]
L.remove(3.5)
print(L)
print(len(L))
