def longest_subarray_with_sum_k(arr, k):
    """
    Finds the length of the longest subarray with sum equal to k.
    
    Parameters:
    arr (List[int]): The input array of positive integers.
    k (int): The target sum.
    
    Returns:
    int: Length of the longest subarray with sum equal to k.
    """
    start = 0       # Left pointer
    curr_sum = 0    # Current window sum
    max_len = 0     # Maximum subarray length found so far

    for end in range(len(arr)):
        curr_sum += arr[end]  # Expand the window to the right

        # Shrink the window from the left while the sum exceeds k
        while curr_sum > k and start <= end:
            curr_sum -= arr[start]
            start += 1

        # Check if current window's sum is equal to k
        if curr_sum == k:
            max_len = max(max_len, end - start + 1)

    return max_len

# Example usage
arr = [1, 2, 3, 1, 1, 1, 1, 4]
k = 6
print("Length of longest subarray with sum", k, "is:", longest_subarray_with_sum_k(arr, k))

# time complexity: O(n)    # space complexity: O(1)
