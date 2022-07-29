horas = float(input('Horas trabalhadas: '))
rem_hora = float(input('Remuneração por hora: R$'))
sal_bruto = horas * rem_hora
ir = (sal_bruto / 100) * 11
inss = (sal_bruto / 100) * 8
sindicato = (sal_bruto / 100) * 5
descontos = ir + inss + sindicato
sal_liq = sal_bruto - descontos

print('+ Salário bruto : R$ {}'.format(sal_bruto))
print('- IR (11%) : R$ {}'.format(ir))
print('- INSS (8%): R$ {}'.format(inss))
print('- Sindicato (5%): R$ {}'.format(sindicato))
print('= Salário Líquido: R$ {}'.format(sal_liq))
