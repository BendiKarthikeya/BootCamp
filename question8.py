#sum of even indics and odd indics

a=list(map(int,input().split()))
sumEven=0
sumOdd=0
for i in range(len(a)):
    if(i%2==0):
        sumEven+=a[i]
    else:
        sumOdd+=a[i]
print("Even indics is",sumEven,"and Odd indics is",sumOdd)