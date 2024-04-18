matrix=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    sum=0
    for j in range(3):
       sum+=matrix[j][i]
    print("the sum of ",i ,"th column is",sum)
