def binary_search(arr, x, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, x, mid+1, high)
        else:
            return binary_search(arr, x, low, mid-1)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = int(input("Enter a number from the sorted array: "))
result = binary_search(arr, x, 0, len(arr)-1)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in the array")
