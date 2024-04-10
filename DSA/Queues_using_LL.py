"""
Queues work on FIFO
Insertion --> Enqueue() from rear that is tail
Deletion --> Dequeue() from front that is head

"""

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        new_node = Node(value)

        if self.rear == None:

            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.front == None: #self.front will be None when it will try to dequeue from empty queue
            return 'Empty'
        else:
            self.front = self.front.next

    def is_empty(self):
        return self.front == None

    def size(self):
        curr = self.front
        cnt = 0 

        while curr != None:
            cnt += 1
            curr = curr.next
        return cnt

    def traverse(self):
        curr = self.front

        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next

q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
#q.traverse()
q.dequeue()
q.traverse()
print('size',q.size())

