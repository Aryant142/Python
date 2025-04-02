a = int(input('enter  the first number')) 
b = int(input('enter  the second number')) 
c = int(input('enter  the third number')) 
mid=max=min=0
if(a>b and a>c):
    if b>c:
        min,mid,max=c,b,a
    else :
        min,mid,max=b,c,a
elif (b>a and b>c):
     if a>c:
        min,mid,max=c,a,b
else :
    if (b>a):
         min,mid,max=a,b,c
    else :
        mid,mid,max=b,a,c
print (min,mid,max )       
               
            
