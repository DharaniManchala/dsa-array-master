# 🧠 Time and Space Complexity:
# Time Complexity: O(n) — We are traversing the array a few times linearly.

# Space Complexity: O(n) — We use two extra lists to store positive and negative elements.


class Solution(object):
    def rearrangeArray(self, nums):
        """
        Rearranges array elements such that positives and negatives alternate.
        Extra elements (if any) are appended at the end in the same order.
        
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []

        # Separate positive and negative numbers
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        # Merge alternately
        result = []
        i = j = 0
        while i < len(positive) and j < len(negative):
            result.append(negative[j])
            result.append(positive[i])
            i += 1
            j += 1

        # Append remaining elements
        while j < len(negative):
            result.append(negative[j])
            j += 1
        while i < len(positive):
            result.append(positive[i])
            i += 1

        return result
