"""

Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive

"""

arr = [0,2,1]

def partition(arr, low, high):
    pivot = arr[high]
    i = -1
    for j in range(high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)

quick(arr, 0, len(arr)-1)

print(arr)