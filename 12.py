#largest element in an array 

nums=[4,2,8,2,75,62,72,52]

largest=nums[0]
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])

print(largest)

#time complexity=0(n)