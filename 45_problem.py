n=input()
count=0
for i in range(len(n)//2):
     if(n[i]==n[len(n)-i-1]):
        count+=1

if(count==len(n)//2):
    print("Palindrome")
else:
    print("Not Palindrome")