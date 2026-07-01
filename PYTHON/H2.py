#h2) Toll Plaza Simulation (Circular Queue)

#A toll plaza has a fixed capacity of 5 vehicles.
#  If full, new vehicles must wait Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insert vehicle
    def enqueue(self, vehicle):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print(vehicle, "entered toll.")

    # Remove vehicle
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print(self.queue[self.front], "left toll.")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # Display queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Vehicles in Queue:")

        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size


# Main Program
q = CircularQueue(5)

while True:
    print("\n1.Enter Vehicle")
    print("2.Exit Vehicle")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle number: ")
        q.enqueue(vehicle)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid Choice!")