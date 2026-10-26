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
    def middle(self):
        slow = self.front
        fast = self.front
        if self.front is None:
            return None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("Middle Element = ",slow.data)
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
que.enqueue(Node(50))
que.print()
que.middle()
