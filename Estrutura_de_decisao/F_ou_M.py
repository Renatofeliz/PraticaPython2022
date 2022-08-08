sexo = str(input('Digite M para Homem ou F para Mulher: '))

if sexo == "m" or sexo == "M":
    print('Sexo Masculino! {}.'.format(sexo))
else:
    if sexo == "f" or sexo == "F":
        print('Sexo Feminino! {}.'.format(sexo))
    elif sexo != 'm' or 'M' or 'f' or 'F':
        print('Sexo invalido!')
