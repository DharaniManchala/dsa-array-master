def largest_subarray_zero_sum(arr):
    sum_index_map = {}
    max_len = 0
    curr_sum = 0
    
    for i, num in enumerate(arr):
        curr_sum += num
        
        if curr_sum == 0:
            max_len = i + 1
        
        if curr_sum in sum_index_map:
            max_len = max(max_len, i - sum_index_map[curr_sum])
        else:
            sum_index_map[curr_sum] = i
    
    return max_len

# Test
arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(largest_subarray_zero_sum(arr))  # Output: 5
