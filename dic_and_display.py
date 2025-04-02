a=dict()
n=int(input('enter the number of element  you want to enter:'))

i=1
while i<=n:
    b=input('enter the section : ')
    c=input('enter the stream : ')
    a[b]=c
    i+=1

print('class','\t','section','\t','stream')
for  i in a :
   print('Xl','\t',i,'\t\t',a[i])
