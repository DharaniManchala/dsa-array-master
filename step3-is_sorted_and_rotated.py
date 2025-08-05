def issorted(arr):
    if not arr:
        return True
    n=len(arr)
    for i in range(1,n):
        if arr[i]>arr[(i+1)%n]:
            count+=1
    return count <= 1
#Time Complexity: O(n)

# Space Complexity: O(1) (no extra space used)



            
 