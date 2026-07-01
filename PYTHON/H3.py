# H3) The GPS Navigation System (Backtracking)

# You're building a GPS app like Google Maps for a hiking trail The hiker moves through checkpoints if they take a wrong turn, they hit "Go Back" to retum to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again - just like a browser's back forward buttons Operations:

# visit(place)-move to a new place

# back()- go to previous place

# forward() go forward if available

class GPS:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    # Visit new place
    def visit(self, place):
        if self.current is not None:
            self.back_stack.append(self.current)

        self.current = place
        self.forward_stack.clear()

        print("Current Location:", self.current)

    # Go Back
    def back(self):
        if len(self.back_stack) == 0:
            print("No previous location.")
            return

        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()

        print("Current Location:", self.current)

    # Go Forward
    def forward(self):
        if len(self.forward_stack) == 0:
            print("No forward location.")
            return

        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()

        print("Current Location:", self.current)

    # Show current location
    def show(self):
        print("Current Location:", self.current)


# Main Program
gps = GPS()

while True:
    print("\n1.Visit Place")
    print("2.Go Back")
    print("3.Go Forward")
    print("4.Current Location")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        place = input("Enter place name: ")
        gps.visit(place)

    elif choice == 2:
        gps.back()

    elif choice == 3:
        gps.forward()

    elif choice == 4:
        gps.show()

    elif choice == 5:
        break

    else:
        print("Invalid Choice!")