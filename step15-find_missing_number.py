def find_missing_xor(arr, n):
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

arr = [1, 2, 4, 5]
n = 5
print("Missing number:", find_missing_xor(arr, n))
