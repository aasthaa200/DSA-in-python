#count no of digit

n = int(input("enter a number:"))
num = n
count = 0

while num > 0:
    count+=1
    num = num//5
print(count)


                    #time complexity
                    #0log(10 N)