"""🧠 Intuition (Logic)
Since the array is already sorted, duplicates will be next to each other.

We can use the two-pointer technique:

One pointer i to track the last position of the unique value.

The second pointer j to iterate through the array.

If nums[j] != nums[i], it's a new unique number. Increment i and place it at nums[i].

"""
def removeduplicates(arr):
    if not arr:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    new_length = removeduplicates(arr)
    print("Array after removing duplicates:", arr[:new_length])  # Output: [1, 2, 3, 4, 5]
    
    # timecomplexity: O(n)
    # spacecomplexity: O(1)