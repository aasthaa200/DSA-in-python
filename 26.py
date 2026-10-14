#rotate matrix by 90 degree

matrix=[[5,6,8],
        [9,2,4],
        [1,3,7]]

n=len(matrix)
for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in range(0,n):
        matrix[i].reverse() 

print(matrix)
