
# ax**2+bx+c
a=int(input('enter the  value of a : '))
b=int(input('enter the  value of b : '))
c=int(input('enter the  value of c :'))
d=int(b**2-4*a*c)
if  d>0:
    print('the roots are real')
    print('the +ve root is '(-b+d**0.5)/2*a)
    print('the -ve root is '(-b-d**0.5)/2*a)
elif d==0:
    print('the roots are equal')
    print( 'the equal roots are root is '(-b/2*a))
else:
   print('the roots are imginary')




