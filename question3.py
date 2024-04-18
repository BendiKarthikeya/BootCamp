#A.P of n numbers
# a,d,n=(map(int,input().split()))
# for i in range(n):
#     print((a+(i)*d),end=" ")
a,d,n=(map(int,input().split()))
for i in range(a,a+(n)*d,d):
    print(i,end=" ")