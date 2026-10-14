#  right rotate a array by 1 

nums=[1,8,2,6,4,9]

n=len(nums)
temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]

    nums[0] = temp

print(nums)


#time complexity=0(n)
#space complexity=o(1)