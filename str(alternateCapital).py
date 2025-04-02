s=input("enter the string : ")
s2 =""
print ("the original string is : ", s)
leng=len(s)
for i in range(0,leng):
    if i % 2 == 0 :
        s2+=s[i]
    else:
        s2+=s[i].upper()
print(s2)        
