l1=[-12,11,-13,-5,6,-7,5,-3,-6]
l2=[]
l3=[]
l4=[]
for i in range (len(l1)):
    if l1[i]>=0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
l4=l3+l2
print(l4)        

# for example
# [-12, -13, -5, -7, -3, -6, 11, 6, 5]

