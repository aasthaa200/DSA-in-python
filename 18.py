19# merge 2 sorted array

a=[1,1,2,4,5,5,6,8,9]
b=[2,3,3,3,5,6,6]
c=[]
i=0
j=0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        if c== [] or c[-1] != a[i]:
            c.append(a[i])
        i+=1
    else:
        if c== [] or c[-1] != b[j]:
            c.append(b[j])
        j+=1

while i < len(a):
    if c== [] or c[-1] != a[i]:
        c.append(a[i])
    i+=1

while j < len(b):
    if c== [] or c[-1] != b[j]:
        c.append(b[j])
    j+=1

print(c)

#time complexity is O(n+m) where n and m are the lengths of the two arrays.