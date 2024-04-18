#Check fibonacci sequence or not
a=list(map(int,input().split()))
count=0
if(a[0]==0 and a[1]==1):
    for i in range(2,len(a)):
        if(a[i]==a[i-1]+a[i-2]):
            count+=1
    if(count==len(a)-2):
        print("It is a fibonacci sequence")
    else:
        print("It is a not fibonacci sequence")
else:
    print("It is not  a fibonacci sequence")

