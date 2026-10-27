class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode
    def maximum(self):
        if self.front is None:
            return None
        max_val = self.front.data
        temp = self.front
        while temp is not None:
            if temp.data > max_val:
                max_val = temp.data
            temp = temp.next
        print("Maximum element in queue = ",max_val)
    def print(self):
        if(self.front == self.rear == None):
            print("Queue is empty")
            return
        temp = self.front
        print("Queue Elements")
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()
que = LQueue()
que.enqueue(Node(10))
que.enqueue(Node(20))
que.enqueue(Node(30))
que.enqueue(Node(40))
que.print()
que.maximum()
