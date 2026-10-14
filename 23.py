#longest consuctive sequence

nums=[100, 4, 200, 1, 3, 2]

nums.sort()
count=0
last_smallest=float('-inf')
longest=0
for i in range(0,len(nums)):
    if nums[i] == last_smallest:
        continue
    if nums[i] == last_smallest + 1:
        count += 1
    else:
        count = 1
    last_smallest = nums[i]
    longest = max(longest, count)
    if nums[i]+1==nums[i+1]:
        count+=1
        if count>longest:
            longest=count
    elif nums[i]!=nums[i+1]:
        count=0

print(longest)