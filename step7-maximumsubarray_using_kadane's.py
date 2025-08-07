# def max_subarray_sum(nums):
#     max_so_far = nums[0]           # Initialize to first element
#     max_ending_here = nums[0]      # Running sum

#     for i in range(1, len(nums)):
#         max_ending_here = max(nums[i], max_ending_here + nums[i])
#         max_so_far = max(max_so_far, max_ending_here)

#     return max_so_far

# Leetcode 53: Maximum Subarray
# Approach: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums):
        # Initialize current_sum and max_sum to first element
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Either extend previous subarray or start new from current num
            current_sum = max(num, current_sum + num)

            # Update max_sum if current_sum is higher
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = sol.maxSubArray(nums)
    print("Maximum Subarray Sum:", result)  # Output: 6
    
