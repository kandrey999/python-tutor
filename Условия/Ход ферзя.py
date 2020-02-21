x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

if abs(x2-x1) == abs(y2-y1) or abs(x2-x1) == 0 or abs(y2-y1) == 0:
    print('YES')
else:
    print('NO')