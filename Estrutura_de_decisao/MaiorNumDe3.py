print('*' * 15)
n1 = int(input('Primeiro numero: '))
print('*' * 15)
n2 = int(input('Segundo numero: '))
print('*' * 15)
n3 = int(input('Terceiro numero: '))
print('*' * 15)

if n1 > n2 and n1 > n3:
    print('Numeros digitados: {}, {}, {}. Maior numero entre os 3: {}'.format(n1,n2, n3, n1))
elif n2 > n1 and n2 > n3:
    print('Numeros digitados: {}, {}, {}. Maior numero entre os 3: {}'.format(n1,n2, n3, n2))
elif n3 > n2 and n3 > n1:
    print('Numeros digitados: {}, {}, {}. Maior numero entre os 3: {}'.format(n1,n2, n3, n3))
