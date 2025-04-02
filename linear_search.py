li=list(map(int,input('enter the string : ').split()))
print( li )
a=int(input('enter the number to be searched'))
# for i in range (len(li)):
#     if li[i]==a:
#         index=i 
#     else :
#         flag=0
        
# if flag==0:
#     print('number not found')
# else:
#     print(f'the number {a} is at index {index}')            
    
try:
    index = next(i for i, x in enumerate(li) if x == a)
    print(f'the number {a} is at index {index}')
except StopIteration:
    print('number not found')    