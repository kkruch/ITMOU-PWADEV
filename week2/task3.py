a=4
b=5

f1 = list()
f1.append(lambda a,b: a*b)
f1.append(lambda a,b: 2*(a+b))

ans=[]
ans_s=''
for ind,value in enumerate(f1):
    print(ind, f1[ind](a,b))
    ans.append(f1[ind](a,b))
    ans_s += str(f1[ind](a,b)) + ' '
print(ans)
print(ans_s[:-1])
# while i<len(f1):
#     ans.append(f1[i](a,b))
#     ans_s += str(f1[i](a,b)) + ' '
#     print(i, ' ', f1[i](a,b))
#     i += 1

# print(f1[0](a,b),f1[1](a,b))




"""
a = int(input())
b = int(input())
f1 = list()
f1.append(lambda a,b: a*b)
f1.append(lambda a,b: 2*(a+b))

ans=[]
ans_s=''
for ind,value in enumerate(f1):
    print(ind, f1[ind](a,b))
    ans.append(f1[ind](a,b))
    ans_s += str(f1[ind](a,b)) + ' '
print(ans)
print(ans_s[:-1])
"""