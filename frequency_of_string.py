l=[3,21,5,6,3,8,21,6]
l1 = []
l2 = []
for i in l:
    if i not in l1:
        l1.append(i)
        x = l.count(i)
        l2.append(x)
print('number', '\t', 'frequency')
for i in range(len(l1)):
    print(l1[i], '\t', l2[i])
    
