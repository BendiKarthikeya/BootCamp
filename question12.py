#zip function
name=['a','b','c']
marks=[10,30,92]
l=[(n,m) for n,m in zip(name,marks)]

a=[1,2,3,4]
b=[5,6,7,8]
l=[x+y for x,y in zip(a,b)]


#2D array
m=int(input())
n=int(input())
matrix=[[0 for j in range(m)] for i in range(n) ]

#Transpose matrix
[[row[j] for row in matrix] for j in range(m)]
