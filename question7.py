#Given a number,print its divisor
nums=[1,2,1,3,2,5]
z=0
x=0
y=0
for i in nums:
    z=z^i
for j in range(len(nums)):
    if(((z>>j) & 1 )%2==1):
        print(j)
        for m in nums:
            if(((m>>j) & 1 )%2==1):
                x=x^m
            else:
                y=y^m
        print(x,y)
        break
    
    
