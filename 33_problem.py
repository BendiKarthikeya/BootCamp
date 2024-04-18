import math
a,n,r=list(map(int,input().split()))
for i in range(n):
    #print(int(a*(math.pow(r,i))), end=" ")
    print(int(a*(r**i)),end=" ")