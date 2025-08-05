"""🔍 Finding the Largest Element in an Array
✅ Problem Statement:
Given an array of n integers, find the largest (maximum) element.

🧠 Logic:
Initialize a variable max_element with the first element of the array.

Traverse the array from index 1 to n-1.

At each step, compare the current element with max_element.

If the current element is greater, update max_element."""
def largestelement(arr):
    if not arr:
        return None
    max_element=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_element:
            max_element=arr[i]
            
    return max_element
# Example usage:
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Largest element in the array:", largestelement(arr))  # Output: 9

    # timecomplexity: O(n)
    # spacecomplexity: O(1)