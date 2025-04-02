def expo(x,y):
    if y == 0:
        return 1
    else:
        return x*expo(x,y-1)

a=int(input('enter  the value of base : '))
b=int(input('enter  the value of power : '))
print(expo(a,b))
