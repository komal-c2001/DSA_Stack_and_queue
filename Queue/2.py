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
    def dequeue(self):
        temp = self.front
        print("Deleted Node : ",temp.data)
        self.front = self.front.next
        if self.front == None: # if there is only one node
            self.rear == None
        temp = None

    def print(self):
        if(self.front == None):
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
que.dequeue()
que.print()
