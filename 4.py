            # find factor


# n = int(input("Enter a number:"))
# num=n
# result=[]
# for i in range(1,num//2):
#     if num% i==0:
#         result.append(i)
# result.append(num)
# print(result)


#time complexity
#0(N/2) ~0(N)

from math import sqrt
n = int(input("Enter a number:"))
num=n
result=[]
for i in range(1,int(sqrt(num))+1):
    if num % i==0:
        result.append(i)
        if (num//i !=i):
            result.append(num//i)
            
print(result)

