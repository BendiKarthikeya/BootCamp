matrix1=[[1,1,1],[2,2,2],[3,3,3]]
matrix2=[[1,0,0],[0,1,0],[0,0,1]]
matrix3=[]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        row=[]
        a=0
        for k in range(len(matrix2)):
            a+=matrix1[i][k]*matrix2[k][j]
        row.append(a)
        matrix3.append(row)
    
print(matrix3)
