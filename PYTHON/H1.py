#H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots numbered 0-7. 
# Each slot holds one product. one product.
#  The warr warehouse manager needs to: check what's at a slot, find a product, update a slot, and check if the belt is full. 
# The conveyor belt - fixed 8 slots

class ConveyorBelt:
    def __init__(self):
        # Fixed size array of 8 slots
        self.belt = ["Empty"] * 8

    # Add or Update product
    def update_slot(self, index, product):
        if 0 <= index < 8:
            self.belt[index] = product
            print("Product updated successfully.")
        else:
            print("Invalid Slot!")

    # Check product at a slot
    def check_slot(self, index):
        if 0 <= index < 8:
            print("Slot", index, "contains:", self.belt[index])
        else:
            print("Invalid Slot!")

    # Find a product
    def find_product(self, product):
        if product in self.belt:
            print(product, "found at slot", self.belt.index(product))
        else:
            print(product, "not found.")

    # Check whether belt is full
    def is_full(self):
        if "Empty" not in self.belt:
            print("Conveyor Belt is FULL.")
        else:
            print("Conveyor Belt is NOT FULL.")

    # Display belt
    def display(self):
        print("\nCurrent Conveyor Belt")
        for i in range(8):
            print("Slot", i, ":", self.belt[i])


# Main Program
obj = ConveyorBelt()

while True:
    print("\n1.Update Slot")
    print("2.Check Slot")
    print("3.Find Product")
    print("4.Check Belt Full")
    print("5.Display Belt")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        index = int(input("Enter slot number (0-7): "))
        product = input("Enter product name: ")
        obj.update_slot(index, product)

    elif choice == 2:
        index = int(input("Enter slot number: "))
        obj.check_slot(index)

    elif choice == 3:
        product = input("Enter product name: ")
        obj.find_product(product)

    elif choice == 4:
        obj.is_full()

    elif choice == 5:
        obj.display()

    elif choice == 6:
        break

    else:
        print("Invalid Choice!")