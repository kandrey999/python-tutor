a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a==b==c:
    print('3')
elif a==b or a==c or c==b:
    print('2')
else:
    print('0')