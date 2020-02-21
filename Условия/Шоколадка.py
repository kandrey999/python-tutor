n = int(input('Enter n: '))
m = int(input('Enter m: '))
k = int(input('Enter k: '))

if (k%m == 0 and m*n >= k) or (k%n == 0 and m*n >= k):
    print('YES')
else:
    print('NO')