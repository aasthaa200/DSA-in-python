# set matrix to zero
mat=[[5, 6, 8, 1],
     [9, 0, 2, 4],
     [0, 3, 7, 5],
     [1, 2, 3, 4]]

def mark_infinity(mat):
    rows=len(mat)
    cols=len(mat[0])
    row_flag=[False]*rows
    col_flag=[False]*cols

    for i in range(rows):
        for j in range(cols):
            if mat[i][j]==0:
                row_flag[i]=True
                col_flag[j]=True

    for i in range(rows):
        for j in range(cols):
            if row_flag[i] or col_flag[j]:
                mat[i][j]=0

mark_infinity(mat)
print("Matrix after setting zeros:")
for i in range(len(mat)):
    print(mat[i])

#time complexity of this code is O(n*m) where n is number of rows and m is number of columns & space complexity is O(n+m) where n is number of rows and m is number of columns