import math

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
x3 = int(input('Enter x3: '))
y3 = int(input('Enter y3: '))

ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
per = ab + bc + ac
poluper = per / 2
s = math.sqrt(poluper * (poluper - ab) * (poluper - bc) * (poluper - ac) )
if s == 0:
    print('Такого треугольника нет')
    print('Площадь треугольника = ', s) 
else:
    print('Периметр треугольника = ', per)

