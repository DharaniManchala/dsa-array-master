def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)  # For O(1) lookups
    max_length = 0

    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count how many next consecutive numbers are present
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            max_length = max(max_length, current_streak)

    return max_length

# 🔍 Example Usage
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive sequence length:", longestConsecutive(nums))  # Output: 4

# 🕒 Time Complexity: O(n)
# 📦 Space Complexity: O(n)
# The time complexity is O(n) because we traverse the set of numbers once.
# The space complexity is O(n) due to the storage of numbers in a set.