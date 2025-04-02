

st = input("Enter the string: ")
st1 = ''

for i in range(len(st)):
    if st[i] not in 'IOUAaeiouE':
        st1 += st[i]

print(st1)

