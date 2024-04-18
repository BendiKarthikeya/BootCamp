a=list(map(int,input().split()))
for i in range(len(a)-1):
    adjsum=a[i]+a[i+1]
    print("sum of ", a[i], " and ", a[i+1]," is ", adjsum)