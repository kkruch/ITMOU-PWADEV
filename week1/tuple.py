s = input()
set1 = set(s)
l1 = list(set1)
l1.sort()
l2 = [] 
for l in l1:
    l2.append(int(l))
print(tuple(l2))
l1.reverse()
l3 = []
for l in l1:
    l3.append(int(l))
print(tuple(l3))
