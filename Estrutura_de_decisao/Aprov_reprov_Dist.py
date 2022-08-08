m1 = int(input('Nota 1: '))
m2 = int(input('Nota 2: '))

media = (m1 + m2) / 2

if media >= 7 and media  < 10:
    print('Aprovado!')
else:
    if media < 7:
        print('Reprovado!')
    elif media == 10:
        print('Aprovado com Distinção!')        