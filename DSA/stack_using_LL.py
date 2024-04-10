"""
Implementing stacks using LL
LL ka insert from head is same as stack
"""
#to create node object we will need node class 
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None #returns the last added item in the stack, for initial state when stack is empty top = None

    def isempty(self):
        return self.top == None
    
    def push(self,val):
        new_node = Node(val) #new_node.data = val, new_node.next = None
        new_node.next = self.top

        self.top = new_node
    
    def peek(self):
        if (self.isempty()):
            return 'Stack Khali hai'
        else:
            return self.top.data
    
    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next

    def size(self):
        curr=self.top
        cnt = 0 
        while curr != None:
            cnt += 1
            curr = curr.next
        return cnt

    def pop(self):
        if (self.isempty()):
            return 'Stack khali hai'
        else:
            data = self.top.data
            self.top = self.top.next
            return data

S = Stack()
print(S.isempty())
S.push(2)
S.push(1)
S.push(30)
print(S.isempty())
S.traverse()
S.pop()
S.traverse()
print(S.peek())
# S.pop()
# S.pop()
print(S.isempty())
print(f'size is {S.size()}')

def reverse_string(string):
    #wapp to reverse a given string using stack
    s = Stack()
    for i in string:
        s.push(i)

    res = ''
    while(not (s.isempty())):
        res = res + s.pop()

    return res

print(reverse_string('hello'))   

def text_editor(string,pattern):
    #given a string = 'hello' an pattern = 'uur' (here u=undo, r=redo), return the string after given pattern

    undo = Stack()  
    redo = Stack()

    for i in string:
        undo.push(i)

    
    for i in pattern:
        if i == 'u':
            data = undo.pop()
            redo.push(data)
            
        else:
            data = redo.pop()
            undo.push(data)

    res = ''
    while(not undo.isempty()):
        res = undo.pop() + res
    return res

print(text_editor('hello','uuur')) 

"""
A celeb is a person who knows no one (0), but everyone knows him (1)
Given a n*n matrix find the celeb
if there is celeb then return ---> the celeb name 
if no one is celeb then return --> no one is celeb
In the below given matrix 1 is celeb
"""



def celeb(lst):
    s = Stack()
    
    for i in range(len(lst)):
        s.push(i)
    
    print(f'2D matrix size is {s.size()}')
    
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if lst[i][j] == 1:
            # i is not celeb
            s.push(j)
        else:
            # j is not celeb
            s.push(i)
    celeb = s.pop() #celeb me 1 hai
    for i in range(len(lst)):
        if i != celeb:
            if lst[i][celeb] == 0 or lst[celeb][i] == 1:
                print('No one is celeb')
                return
    print(f'celeb is {celeb}')
        
    

lst =[
    [0,1,0,1], #0
    [0,0,0,0], #1
    [1,1,0,1], #2
    [1,1,1,0]  #3
]
celeb(lst)


