# x = 0
# y = 1
# z = 1
# n = int(input(' etner the limit'))
# print(f'The fibonacci series upto {n}')
# print(x,y,end='')
# while z <= n :
#     print(z,end='')
#     x=y
#     y=z
#     z=x+y
    
def fibo(x,y,z,n):
 while z <= n :
    print(z,end='')
    x=y
    y=z
    z=x+y

x = 0
y = 1
z = 1
n = int(input(' etner the limit'))
print(f'The fibonacci series upto {n}')
print(x,y,end='')
fibo(x,y,z,n)
    
    
    
    