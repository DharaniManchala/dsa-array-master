"""
LeetCode Problem 75: Sort Colors (Dutch National Flag Algorithm)
Link: https://leetcode.com/problems/sort-colors/

Approach:
We use three pointers (low, mid, high) to sort the array of 0s, 1s, and 2s in-place.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        low = 0         # Position for next 0
        mid = 0         # Current element
        high = len(nums) - 1  # Position for next 2

        while mid <= high:
            if nums[mid] == 0:
                # Swap the 0 to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the correct place
                mid += 1
            else:  # nums[mid] == 2
                # Swap the 2 to the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Example Usage
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print("Sorted array:", nums)
# time complexity: O(n) — We traverse the array once.
# space complexity: O(1) — We sort the array in-place without using extra space