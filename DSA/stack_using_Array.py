"""
Implementing Stacks using array
A stack has ---> insertion and deletion from only "one" end.
push() 
pop()
peek() --> returns the top most element in the stack

for empty stack --> self.top = -1

here we are going to use python list as an array (fixed size) to implement stack

python list consists of predefined functions for stack but since we are considering it as array like c++ and java
it will have a fixed size
"""

class Stack:
    def __init__(self,size):
        #for creating a fixed size array we will need the size
        self.size = size #this is size of the array
        self.__stack = [None] * self.size #when size = 3 , array will look like [None , None , None], using this __stack as local stack
        self.top = -1 #empty stack
    
    def push(self,value):
        if self.top == self.size - 1:
            # we have to check this condition because this is a fixed size array
            print("Overflow state")
        else:
            self.top += 1
            self.__stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print('Stack empty')
        else:
            data = self.__stack[self.top]
            self.top -= 1
        
    def peek(self):
        print(self.__stack[self.top])
    
    def traverse(self):
        for i in range(self.top + 1):
            print(self.__stack[i], end=' ')


s = Stack(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.push(10)
s.peek()
s.traverse()