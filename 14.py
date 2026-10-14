# check the array is sorted or not

nums=[1,12,3,4,5,6,7,8,9]
n=len(nums)
is_sorted=True
for i in range(1,n):
    if nums[i] < nums[i-1]:
        is_sorted=False
        break
print(is_sorted)

#time complexity=0(n)