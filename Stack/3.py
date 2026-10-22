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
    def reverse(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            temp = self.top
            while temp:
                stk1.push(Node(temp.data))
                temp = temp.next
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack Contains..")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
stk = stack()
stk1 = stack()
stk.push(Node(10))
stk.push(Node(20))
stk.push(Node(30))
stk.push(Node(40))
stk.print()
stk.reverse()
stk1.print()


        