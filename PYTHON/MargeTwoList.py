# Merge Two Sorted Lists

l1 = [10, 30, 50, 70]
l2 = [20, 40, 60, 80]

merg = []
i = 0
j = 0

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merg.append(l1[i])
        i += 1
    else:
        merg.append(l2[j])
        j += 1

while i < len(l1):
    merg.append(l1[i])
    i += 1

while j < len(l2):
    merg.append(l2[j])
    j += 1

print("Merged list is:", merg)
