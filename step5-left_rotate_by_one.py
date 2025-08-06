# Left Rotate Array by One Place
# Author: Dharani Manchala
# Date: August 6, 2025

def left_rotate_by_one(arr):
    """
    Rotates the given array to the left by one position.

    Parameters:
    arr (list): List of integers

    Returns:
    list: Rotated array
    """
    n = len(arr)
    
    # Handle edge case: empty or single-element array
    if n == 0 or n == 1:
        return arr

    # Step 1: Store the first element
    temp = arr[0]

    # Step 2: Shift elements one position to the left
    for i in range(1, n):
        arr[i - 1] = arr[i]

    # Step 3: Place the first element at the end
    arr[n - 1] = temp

    return arr


# ✅ Example usage
if __name__ == "__main__":
    # Example: Before rotation: [1, 2, 3, 4, 5]
    # After rotation: [2, 3, 4, 5, 1]
    input_array = [1, 2, 3, 4, 5]
    print("Original Array:", input_array)

    rotated_array = left_rotate_by_one(input_array)
    print("Left Rotated Array by One:", rotated_array)
# timecomplexity: O(n)
# spacecomplexity: O(1)