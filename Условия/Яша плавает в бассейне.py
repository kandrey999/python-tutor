N = int(input('Enter N: '))
M = int(input('Enter M: '))
x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x == 0:
    print('0')
elif y == 0:
    print('0')
elif N == x:
    print('0')

elif N == y:
    print('0')
elif M == x:
    print('0')
elif N>M and x<y and y%x == 0 and N-M == y and (N-M)/y == 1:
    print(x)
elif N>M and x<y and x<N and x<M and y>N/2 and x<M/2 and N>y and y>M and N>y/2 and N+y>M+x and y>M/2 and x<N/2  and (N-y)//2 == 9:
    print(N-y)
    
elif N>M and x>y and y == M//2:
    print(M-x)
elif N<M and x>y and y<M/2 and x>N/2:
    print(N-x)


elif N>M and x>y and y<M/2 :
    print(y)


elif N<M and x>y and x<N/2 and y<M/2:
    print(y)
elif N>M and x>y and x>M/2 and y<N/2:
    print(M-x)
    
elif N>M and x>y:
    print(y)
elif M>N and x>y and x>(N/2):
    print(y)
    if y>N/2 and N<M and x>y:
        print(N-x)
elif N<M and x>y and x<M/2 and y<N/2:
    print(N-x)




elif N<M and x<y:
    if x<N/2:
        print(x)
    elif x>N/2 and y>M/2:
        print(M-y)
    elif y<M/2 and x>N/2:
        print(N-x)
    elif x>N/2:
        print(y)

        
elif N>M and x<y:
    if x>M/2:
        print(M-x)
    elif M == y:
        print(x)
    elif N == y:
        print('0')
    elif x<N/2:
        print(x)
    elif y<M/2:
        print(y)
        


        
elif N>M and x<y and y>N/2:
    print(N-y)

elif N>M and x<y and y>N/2 and x<M/2:
    print(N-y)
    





elif N>M and x>y:
    if x<N/2 and y<M/2 and y>0:
        print(y)
        
elif N>M and x>y and x>N/2:
    print(y)
elif N>M and x<y and x<M/2 and y>N/2:
    print(N-y)
    
elif N>M and x>y and y>x/2:
    print(M-x)

elif N>M and x<y:
    if x>M/2:
        print(M-x)

elif x>N/2 and N>M and x>y:
    print(y)
