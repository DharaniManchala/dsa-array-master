def max_subarray_sum(arr):
    max_ending_here = arr[0]  # current sum
    max_so_far = arr[0]       # best sum found so far

    for num in arr[1:]:
        # either add num to existing sum or start fresh from num
        max_ending_here = max(num, max_ending_here + num)
        # update best sum
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(arr))  # Output: 7
