
a=[]
n=int(input("Enter the no  of array : "))
for i in range(n):
    s=int(input("Enter the size : "))
    a.append(s)
print("unsorted : ",a)

for i in range(n):
    for j in range(i):
        if(a[j]>a[i]):
            a[i]=a[i]^a[j]
            a[j]=a[i]^a[j]
            a[i]=a[i]^a[j]
            
print("sorted : ",a)