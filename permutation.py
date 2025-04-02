def fac(a):
    if a == 0 or a == 1:  
        return 1
    else:
        return a * fac(a - 1) 

def perm(a, b):
    if b == 0:
        return 1
    else:
        return fac(a) // fac(a - b)  

x = int(input('Enter the value of a: '))
y = int(input('Enter the value of b: '))
print(perm(x, y))
