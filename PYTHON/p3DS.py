
# #c3)The Smart Printer Qucue (Priority Queue]
# An oftice printer handles jobs in order, BUT jobs marked URGENT must be printed
# before normal jobs. Design a system using two queues -- one for urgant, one for
# norma
# and always drain urgent first.


from collections import deque

class SmartPrinterQueue:

    def __init__(self):
        self.urgent = deque()
        self.normal = deque()

    # Add a new print job
    def add_job(self, job, priority):
        if priority.lower() == "urgent":
            self.urgent.append(job)
            print(job, "added to Urgent Queue.")
        else:
            self.normal.append(job)
            print(job, "added to Normal Queue.")

    # Print the next job
    def print_job(self):
        if self.urgent:
            print("Printing Urgent Job:", self.urgent.popleft())
        elif self.normal:
            print("Printing Normal Job:", self.normal.popleft())
        else:
            print("No jobs in the printer queue.")

    # Display both queues
    def display(self):
        print("\nUrgent Queue :", list(self.urgent))
        print("Normal Queue :", list(self.normal))


# Main Program
printer = SmartPrinterQueue()

while True:
    print("\n----- Smart Printer Queue -----")
    print("1. Add Print Job")
    print("2. Print Next Job")
    print("3. Display Queues")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        job = input("Enter Job Name: ")
        priority = input("Enter Priority (Urgent/Normal): ")
        printer.add_job(job, priority)

    elif choice == 2:
        printer.print_job()

    elif choice == 3:
        printer.display()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
