s = input()
s1 = s.split()
s1.sort()
ans1 = ''
for string in s1:
    ans1 = string + ' '
print(ans1[:-1])
s1.reverse()
ans2 = ''
for string in s1:
    ans2 = string + ' '
print(ans2[:-1])

