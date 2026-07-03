# Linear Search - Spam Detector

B_list = [10, 20, 30, 40, 50]

sender = int(input("Enter sender ID: "))

found = 0

for i in B_list:
    if i == sender:
        found = 1
        break

if found == 1:
    print("Spam sender found")
else:
    print("No spam")
