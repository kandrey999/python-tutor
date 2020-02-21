column1 = int(input('Enter column1: '))
row1 = int(input('Enter row1: '))
column2 = int(input('Enter column2: '))
row2 = int(input('Enter row2: '))
color1 = int(0)
color2 = int(0)

if (column1%2 == 0 and row1%2 != 0) or (column1%2 != 0 and row1%2 == 0):
    color1 = 1


if (column2%2 == 0 and row2%2 != 0) or (column2%2 != 0 and row2%2 == 0):
    color2 = 1

if color1 == color2:
    print('YES')
else:
    print('NO')

    #Решение разработчиков
#     x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')
