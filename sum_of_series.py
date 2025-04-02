x = int(input("enter the number : "))
y = int(input("enter the limit : "))
sum=0
for i in range (0,y+1):
    fact=1
    for j in range (1,i+1):
        fact=fact*j
    sum+=(x**i)/fact 
print(sum)       
           
        
        
    
