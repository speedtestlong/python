for i in range(1, 10):
        for j in range(1, i):
            print('\t', end='')
        for j in range(i, 10):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()
