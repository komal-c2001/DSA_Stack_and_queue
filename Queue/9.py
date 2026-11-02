
class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    # 2. Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted element:", self.queue.pop(0))

    # 3. Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

    # 4. Reverse queue using stack
    def reverse(self):
        stack = []

        while len(self.queue) > 0:
            stack.append(self.queue.pop(0))

        while len(stack) > 0:
            self.queue.append(stack.pop())

        print("Queue reversed successfully")

    # 5. Merge two queues
    def merge(self, q2):
        self.queue = self.queue + q2.queue
        print("Queues merged successfully")

    # 6. Check identical queues
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Both queues are identical")
        else:
            print("Queues are not identical")


# Main program
q1 = Queue()
q2 = Queue()
print("\n1. Enqueue")
print("2. Dequeue")
print("3. Display")
print("4. Reverse Queue")
print("5. Merge Two Queues")
print("6. Check Identical Queues")
print("7. Exit")
while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        q1.enqueue(value)

    elif choice == 2:
        q1.dequeue()

    elif choice == 3:
        q1.display()

    elif choice == 4:
        q1.reverse()
        q1.display()

    elif choice == 5:
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            value = int(input("Enter element: "))
            q2.enqueue(value)

        q1.merge(q2)
        q1.display()

    elif choice == 6:
        n = int(input("Enter number of elements in second queue: "))

        q2 = Queue()

        for i in range(n):
            value = int(input("Enter element: "))
            q2.enqueue(value)

        q1.identical(q2)

    elif choice == 7:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
