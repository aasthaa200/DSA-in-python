#print the  matrix in spiral order

matrix=[[5,6,8,1],
        [9,2,4,3],
        [1,3,7,5],
        [2,4,6,8]]

top=0
bottom=len(matrix)-1
left=0
right=len(matrix[0])-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(matrix[top][i],end=" ")
    top+=1

    for i in range(top,bottom+1):
        print(matrix[i][right],end=" ")
    right-=1

    if top<=bottom:
        for i in range(right,left-1,-1):
            print(matrix[bottom][i],end=" ")
        bottom-=1

    if left<=right:
        for i in range(bottom,top-1,-1):
            print(matrix[i][left],end=" ")
        left+=1

print()


#time= 0(n*m) & space complexity =0(i)