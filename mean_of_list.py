li=list(map(int,input('enter the number of a list : ').split()))
print(li)
sum=0
for i in range (len(li)):
    sum+=li[i]
    
print(sum/len(li))    