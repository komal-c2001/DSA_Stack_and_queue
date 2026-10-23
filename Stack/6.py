class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self,newnode):
        newnode.next = self.top
        self.top = newnode
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            count = 0
            print("Stack Contains..")
            temp = self.top
            while temp:
                print(temp.data)
                count += 1
                temp = temp.next
        print("Count of elements in stack = ",count)
stk = stack()
stk.push(Node(10))
stk.push(Node(20))
stk.push(Node(30))
stk.push(Node(40))
stk.print()


        