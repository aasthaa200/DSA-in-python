# rearrange array element by sign

nums=[9, -2, 5, -4, 6, -6, 7, -8]
def rearrange_by_sign(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr.append(arr.pop(i))
    return arr

print(rearrange_by_sign(nums))


#time complexity: O(n) & space complexity: O(1)