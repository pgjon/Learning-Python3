
# CABEÇALHO
print('\033[35m*-' * 8, end='*\033[m\n')
print('\033[31mRADAR ELETRÔNICO!'
      '\nLIMITE DE VELOCIDADE \033[1m80 Km/h\033[m')
print('\033[35m*-' * 8, end='*\033[m\n\n')

vel = float(input('\033[36mDigite a velocidade que passou pelo RADAR: \033[m'))

if vel > 80:
    print('\033[31mEXCESSO DE VELOCIDADE!!\nVOCÊ RECEBERÁ UMA MULTA!\033[m')
    multa = (vel - 80) * 7
    print(f'Velocidade do veículo: {vel} Km/h')
    print(f'Multa a pagar: R$ {multa :.2f}')
else:
    print('\033[32mPARABÉNS!!\033[m :) Você dirige com cautela!')
    print('Sem excesso de \033[32mVELOCIDADE.\033[m')
    print(f'Velocidade do veículo: {vel} Km/h')
