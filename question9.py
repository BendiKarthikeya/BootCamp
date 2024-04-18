#Check list is palindrome or not
a=list(input().split())
if(a==a[::-1]):
    print("palindrome")
else:
    print("Not a palindrome")