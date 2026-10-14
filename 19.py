# move zero to the end of list


nums=[1,5,3,2,0,2,4,0,2,0,2]

i=0
j=1
if len(nums)==1:
    print(nums)
while i<len(nums) and j<len(nums):
    if nums[i]==0 and nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j+=1
    elif nums[i]!=0:
        i+=1
        j+=1
    else:

        j+=1

print(nums)


# if len(nums)==1:
#     print(nums)

# i=0
# j=1 
# while j<len(nums):
#     if nums[i]==0 and nums[j]!=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1
#         j+=1
#     elif nums[i]!=0:
#         i+=1
#         j+=1
#     else:
#         j+=1

# print(nums)



# time complexity is O(n) and space complexity is O(1)