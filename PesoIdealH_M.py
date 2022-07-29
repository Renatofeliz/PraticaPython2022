H_Man = float(input('Altura Cm: '))
H_Woman = float(input('Altura Cm: '))

p_i_h = (72.7 * H_Man) - 58
p_i_m = (62.1 * H_Woman) - 44.7

print('Peso ideal Homem: Kg{:.2f}, Peso ideal Mulher: Kg{:.2f}.'.format(p_i_h, p_i_m))

