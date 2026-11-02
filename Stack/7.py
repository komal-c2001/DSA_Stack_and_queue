
class Stack:
    def __init__(self):
        self.stack = []

    # 1. Push operation
    def push(self, value):
        self.stack.append(value)
        print(value, "is pushed into stack")

    # 2. Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", self.stack.pop())

    # 3. Display operation
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)

    # 4. Reverse String using Stack
    def reverse_string(self, string):
        temp = []

        for ch in string:
            temp.append(ch)

        reverse = ""
        while len(temp) > 0:
            reverse += temp.pop()

        print("Reversed String:", reverse)

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        temp = []

        while len(self.stack) > 0:
            temp.append(self.stack.pop())

        self.stack = temp
        print("Stack reversed successfully")


# Main program
s = Stack()
print("\n1. Push")
print("2. Pop")
print("3. Display")
print("4. Reverse String")
print("5. Reverse Stack")
print("6. Exit")
while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        string = input("Enter string: ")
        s.reverse_string(string)

    elif choice == 5:
        s.reverse_stack()
        s.display()

    elif choice == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
