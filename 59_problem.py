a=[1,2,3,4]
b=[1,5,3,6]
c=a
for i in b:
    if i not in a:
        c.append(i)

print(c)
# a = [1, 2, 3, 4]
# b = [1, 5, 3, 6]
# c = a + [x for x in b if x not in a]

# print(c)
