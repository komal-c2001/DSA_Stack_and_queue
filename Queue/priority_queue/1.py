
class Patient:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
class Hospital:
    def __init__(self):
        self.queue = []

    # 1. Add Patient (Enqueue)
    def enqueue(self, pid, name, priority):
        if priority not in [1, 2, 3]:
            print("Invalid Priority!")
            return

        p = Patient(pid, name, priority)
        self.queue.append(p)

        # Sort patients according to priority
        self.queue.sort(key=lambda x: x.priority)

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if len(self.queue) == 0:
            print("No patients waiting!")
        else:
            p = self.queue[0]
            print("\nNext Patient:")
            print("Patient ID:", p.pid)
            print("Patient Name:", p.name)
            print("Priority:", p.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if len(self.queue) == 0:
            print("No patients to treat!")
        else:
            p = self.queue.pop(0)
            print("Patient treated:", p.name)

    # 4. Display All Patients
    def display_all(self):
        if len(self.queue) == 0:
            print("No waiting patients!")
        else:
            print("\nWaiting Patients:")
            for p in self.queue:
                print("ID:", p.pid,
                      "Name:", p.name,
                      "Priority:", p.priority)


# Main Program
h = Hospital()
print("\n--- Hospital Emergency Management ---")
print("1. Add Patient")
print("2. Display Next Patient")
print("3. Remove Patient")
print("4. Display All Patients")
print("5. Exit")

while True:
    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))
        h.enqueue(pid, name, priority)

    elif ch == 2:
        h.display_next()

    elif ch == 3:
        h.dequeue()

    elif ch == 4:
        h.display_all()

    elif ch == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
