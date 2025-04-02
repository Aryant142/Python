def inc(x):
    return (lambda x:x+1)(x)
a=2
print('BEFORE INCREMENT : ',a)
b=inc(a)
print('AFTER INCREMENT :',b)
