"""You are given an array of integers. Your task is
 to check whether the array is strictly increasing, 
 strictly decreasing, or not sorted.

Alternatively, in basic cases, just check whether the array
 is non-decreasing (each element
 is less than or equal to the next)."""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
arr1 = [1, 2, 2, 3, 4]
arr2 = [5, 4, 3, 2, 1]

print(is_sorted(arr1))  # Output: True
print(is_sorted(arr2))  # Output: False


def is_strictly_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def is_strictly_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True

