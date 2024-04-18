#intersection of two arrays
a=[1,2,3,4]
b=[1,5,3,6]
# c=[]
# for i in b:
#     if i in a:
#         c.append(i)
# print(c)
c=[x for x in b if x in a]
print(c)