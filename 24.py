#transpose of matrix

mat= [[5, 6, 8],
      [9, 4, 2]]

rows=len(mat)
cols=len(mat[0])
result=[[0] * rows for i in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i]=mat[i][j]

for i in range(len(result)):
    print(result[i])


#time complexity of this code is O(n*m) where n is number of rows and m is number of columns
# & space complexity is O(n*m) where n is number of rows and m is number of columns