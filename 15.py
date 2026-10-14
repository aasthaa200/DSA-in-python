# remove duplicates from sorted array(within position)

nums=[1,1,1,2,2,3,4,5,5,6,6,8,8,9,9,9]
for i in range(len(nums)-1,0,-1):
    if nums[i]==nums[i-1]:
        nums.pop(i) 
print(nums)