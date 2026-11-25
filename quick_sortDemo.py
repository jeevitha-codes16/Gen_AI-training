
count = 0

def quicksort(arr, low, high):
    global count

    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            count += 1

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        pi = i + 1

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Quick Sort
quicksort(arr, 0, len(arr) - 1)

# Output
print("Sorted array:", arr)
print("Number of iterations:", count)
