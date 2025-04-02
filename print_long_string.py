st=input("enter the string :")
maxleng=0
x=st.split()
for i in x:
    a=len(i)
    if a>maxleng :
        maxleng=a
        max=i

print(f'The longest substring is of "{a}" letter and in word it is "{max}"')
   
        