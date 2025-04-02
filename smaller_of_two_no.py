def saml(a,b):
    if a>b:
        return b
    else:
        return a

sum = lambda x,y :x+y
diff= lambda x,y : x-y

print("The smallest number is :", saml(sum(1,2),diff(1,2)))