n = int(input(' enter the value : '))
x = 0
y=n
sum =0
i=0
while(n>0):
    x =(n%2)
    sum=sum+x*(10**i)     
    n=n//2
    i+=1    
print(f"the binary no. of {y} is : ",sum)    



    
    
    
    