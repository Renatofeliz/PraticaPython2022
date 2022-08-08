n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('Maior numero: {}.'.format(n1))
else:
    if n2 > n1:
        print('Maior numero: {}.'.format(n2))  
    elif n1 == n2:
        print('Numero iguais! {} = {}.'.format(n1,n2))         