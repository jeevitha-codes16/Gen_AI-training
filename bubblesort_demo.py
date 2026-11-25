
n = int(input("Enter number of elements: "))

a = []

print("Enter the elements:")
for i in range(n):
    a.append(int(input()))

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("Sorted array:", a)
