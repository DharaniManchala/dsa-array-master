# LeetCode 136: Single Number
# Given an array where every element appears twice except for one, find that single one.
# Approach: XOR all elements. Duplicates cancel out to 0.
# Time: O(n), Space: O(1)

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
