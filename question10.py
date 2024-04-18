#Find the prefix sum

a=list(map(int,input().split()))
pref=[0]*len(a)
pref[0]=a[0]
for i in range(1,len(a)):
    pref[i]=pref[i-1]+a[i]
print(pref)              