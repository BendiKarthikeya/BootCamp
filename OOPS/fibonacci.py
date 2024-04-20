a=0
b=1
n=int(input())
c=a+b
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")