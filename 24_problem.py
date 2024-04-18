a,b,c=map(int,input().split())
if(a>b and a>c):
    print("largest is",a)
elif(b>a and b>c):
    print("largest is",b)
elif(c>b and c>a):
    print("largest is",c)