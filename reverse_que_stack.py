class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self,newnode):
        newnode.next = self.top
        self.top = newnode
    def pop(self):
            if self.isempty():
                print("Stack is Empty")
            else:
                temp = self.top
                pop_data = temp.data
                self.top = self.top.next
                temp = None
                return pop_data
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack Elements")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print()
class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isempty(self):
        return self.front is None
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return None
        else:
            temp = self.front
            deque_data = temp.data
            self.front = self.front.next
            if self.front == None: # if there is only one node
                self.rear = None
            temp = None
            return deque_data
    def print(self):
        if(self.front == self.rear == None):
            print("Queue is empty")
            return
        temp = self.front
        print("Queue Elements")
        while temp:
            print(temp.data)
            temp = temp.next
        print()
def reverse_stack(s1):
    q1 = LQueue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()
def reverse_queue(q2):
    s2 = stack()
    while not q2.isempty():
        s2.push(Node(q2.dequeue()))
    while not s2.isempty():
            q2.enqueue(Node(s2.pop()))
    q2.print()
stk = stack()
stk.push(Node(10))
stk.push(Node(20))
stk.push(Node(30))
stk.push(Node(40))
stk.print()
print("Reverse Stack Elements")
reverse_stack(stk)

que = LQueue()
que.enqueue(Node(30))
que.enqueue(Node(80))
que.enqueue(Node(90))
que.enqueue(Node(10))
que.print()
print("Reverse queue Elements")
reverse_queue(que)

        
