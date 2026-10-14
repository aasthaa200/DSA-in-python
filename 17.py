# linear search

a=[1,2,3,4,5,6,7,8,9]
i=0
target=9
for i in range (len(a)):
    if a[i]== target:
        print("found at",i)
        break
else:
    print("not found target element")
         


# target is first occuring 10

a=[2,3,5,1,1,4,4,5,6,7,8,9]
i=0
target=1
for i in range (len(a)):
    if a[i]== target:
        print("found at",i)
        break
else:
    print("not found target element")


# target is not found then print -1


a=[1,2,3,4,5,6,7,8,9]
i=0
target=19
for i in range (len(a)):
    if a[i]== target:
        print("found at",i)
        break
else:
    print("-1")