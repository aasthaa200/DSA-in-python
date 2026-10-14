        #armstrong number
n = 153
num = n
total = 0
nod = len(str(n))

while num > 0:
    digit = num % 10
    total = total + (digit ** nod)
    num = num // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#time complexity
#0log(10 N)