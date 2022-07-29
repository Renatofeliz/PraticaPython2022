'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

m_q = float(input('Metros² a serem pintados: m²'))

latas = (m_q / 3) / 18
preço = latas * 80

print('{:.2f} latas de tinta para pintar {:.2f}m².'.format(latas, m_q))
print('Preço total: R${:.2f}.'.format(preço))