def count_subarrays(arr, k):
    prefix_sum = 0
    prefix_count = {0: 1}  # prefix_sum 0 occurs once initially
    count = 0

    for num in arr:
        prefix_sum += num

        # Check if there’s a previous prefix that makes sum k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]

        # Store the current prefix_sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

# Example
arr = [1, 2, 3]
k = 3
print(count_subarrays(arr, k))  # Output: 2
