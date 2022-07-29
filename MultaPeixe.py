kg_peixe = float(input('Kgs de peixe: '))

limite = 50
excesso = kg_peixe - limite
multa = excesso * 4

if kg_peixe <= limite:
    print('Dentro do limite permitido! Sem multa')
else:
    print('Peso excedente: {:.2f} Kg, multa: R${:.2f}.'.format(excesso, multa))