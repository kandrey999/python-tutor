x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

if (abs(y2-y1) == 2 and abs(x2-x1) == 1) or (abs(y2-y1) == 1 and abs(x2-x1) == 2):
    print('YES') 
else:
    print('NO')