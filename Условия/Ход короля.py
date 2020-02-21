x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

# if abs(x2-x1) <= 1 and abs(y2-y1) <=1:    
#    print("YES")
# else:
#     print('NO')

if (x2 - x1 == -1 or x2 - x1 == 0 or x2 - x1 == 1) and (y2 - y1 == -1 or y2 - y1 == 0 or y2 - y1 == 1):    
   print("YES")
else:
    print('NO')
