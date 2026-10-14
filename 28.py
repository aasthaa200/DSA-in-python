#find first nd last occurence in sorted array

nums=[1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=2
n=len(nums) 
first=-1
last=-1
for i in range(n):
    if nums[i]==target:
        first=i
        break

for i in range(n-1, -1, -1):
    if nums[i]==target:
        last=i
        break

print("First occurrence at index:", first)
print("Last occurrence at index:", last)