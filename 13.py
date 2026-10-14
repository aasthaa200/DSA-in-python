# find second largest element in an array

nums=[1,5,75,85,7,26,76,96,2]
largest=float("-inf")
s_largest=float("-inf")

n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])

    for i in range(0,n):
         if nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]

print(s_largest)

# nums=[1,5,75,85,7,26,76,96,2]
# largest=float("-inf")
# s_largest=float("-inf") 

# n=len(nums)
# for i in range(0,n):
#     if nums[i] > largest:
#         s_largest=largest
#         largest=nums[i]
#     elif nums[i] > s_largest and nums[i] != largest:
#         s_largest=nums[i]
# print(s_largest)