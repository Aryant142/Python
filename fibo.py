def fibo(n):
    if n < 2 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
a=int(input("enter the value of  n:"))
for i in  range(a):
    print(fibo(i))
