'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando 
este link (em minutos).'''

mb = int(input('Tamanho do arquivo em MB: '))
print('Tamanho do arquivo {:.2f} Mb'.format(mb))
velocidade_net = int(input('Velocidade daconexão de internet em Mbps:'))
print('Velocidade da conexão: Mbps- {:.0f}'.format(velocidade_net))
velocidade_download = mb / (velocidade_net / 8)
print('Velocidade que vai ser feito o download aproximada: {:.2f} segundos.'.format(velocidade_download))
minutos = velocidade_download / 60
print('Aproximadamente {:.0f} Minutos.'.format(minutos))
kbps = velocidade_net / 8
print('{:.2f} Kbps'.format(kbps))
