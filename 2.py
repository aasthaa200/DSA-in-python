#palindrome

n = int(input("Enter a number:"))

num = n
result = 0

while num > 0:
    digit = num % 10
    result = (result * 10) + digit
    num = num // 10

if n == result:
    print("Palindrome")
else:
    print("Not palindrome")

    
#time complexity
#0log(10 N)