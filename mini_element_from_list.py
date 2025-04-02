li=list(map(int,input('enter the list of number : ').split()))
l=len(li)
index=0
print(li)
mini=li[0]
for i in range (1,l):
    if li[i]<mini:
        mini=li[i]
        index=i
  
print(f"the smallest element is {mini} which is at index {index}")   
    
#for largest element 
# for i in range (1,l):
#     if li[i]>mini:
#         mini=li[i]
#         index=i
# print(f"the largest element is {mini} which is at index {index}")
