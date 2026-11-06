
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode

    def print(self):
        if self.front == self.rear == None:
            print("Queue is empty")
            return

        temp = self.front
        print("Queue Elements")

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("None")


def mergeTwoQueue(q1, q2):

    q3 = LQueue()

    p1 = q1.front
    p2 = q2.front

    while p1 and p2:

        if p1.data < p2.data:
            q3.enqueue(Node(p1.data))
            p1 = p1.next

        else:
            q3.enqueue(Node(p2.data))
            p2 = p2.next

    while p1:
        q3.enqueue(Node(p1.data))
        p1 = p1.next

    while p2:
        q3.enqueue(Node(p2.data))
        p2 = p2.next

    return q3


# First Queue
q1 = LQueue()
q1.enqueue(Node(10))
q1.enqueue(Node(30))
q1.enqueue(Node(50))
q1.enqueue(Node(70))

# Second Queue
q2 = LQueue()
q2.enqueue(Node(20))
q2.enqueue(Node(40))
q2.enqueue(Node(60))
q2.enqueue(Node(80))

print("First Queue:")
q1.print()

print("Second Queue:")
q2.print()

# Merge two queues
q3 = mergeTwoQueue(q1, q2)

print("Merged Queue:")
q3.print()
