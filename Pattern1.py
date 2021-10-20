n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(i):
        print('B',end='')
    print('A',end='')
    for j in range(i):
        print('B',end='')
    print()