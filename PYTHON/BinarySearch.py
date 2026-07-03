# Binary Search

price = [15000, 25000, 35000, 45000, 55000]
ta = 35000

low = 0
high = len(price) - 1

while low <= high:
    mid = (low + high) // 2

    if price[mid] < ta:
        low = mid + 1
    else:
        high = mid - 1

print("First price =", price[low])
