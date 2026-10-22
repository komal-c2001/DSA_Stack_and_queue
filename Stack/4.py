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
    def compare_two_Stack(self):
        if stk.isempty() or stk1.isempty():
            print("Stack is Empty")
        else:
            temp = stk.top
            temp1 = stk1.top
            while temp and temp1:
                if(temp.data != temp1.data):
                    print("Two stack is not same")
                    return 
                temp = temp.next
                temp1 = temp1.next
            print("Two stack is same")
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
stk1.push(Node(10))
stk1.push(Node(20))
stk1.push(Node(30))
stk1.push(Node(50))
stk.print()
stk.compare_two_Stack()


        