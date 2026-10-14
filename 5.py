n = [2, 5, 2, 9, 4, 2, 5, 4, 1, 1]
m = [52, 1, 2, 7, 2, 2, 2, 8, 6, 4, 5, 1]

# for num in m:
#     count = 0

#     for x in n:
#         if x == num:
#             count += 1

#     print(num, "=", count)

hlist =[0]*11
for num in n:
    hlist[num]+=1

for num in m:
    if num<1 or num>10:
        print("O")
    else:
        print(hlist[num])