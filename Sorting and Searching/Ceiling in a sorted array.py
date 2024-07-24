def ceilSearch(arr, low, high, x):
    if x <= arr[low]:
        return arr[low]
    if x > arr[high]:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == x:
        return arr[mid]
    elif arr[mid] < x:
        if mid + 1 <= high and arr[mid + 1] >= x:
            return arr[mid + 1]
        else:
            return ceilSearch(arr, mid + 1, high, x)
    else:
        if mid - 1 >= low and arr[mid - 1] < x:
            return arr[mid]
        else:
            return ceilSearch(arr, low, mid - 1, x)

# Example usage
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
result = ceilSearch(arr, 0, len(arr) - 1, x)
print(result)  # Output: 8
