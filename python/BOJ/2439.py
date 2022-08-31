T = input()

for i in range(int(T), 0, -1):
    for j in range(1, int(T) + 1):    
        if i <= j:
            print('*', end='')
        else :
            print(' ', end='')
    print('')
