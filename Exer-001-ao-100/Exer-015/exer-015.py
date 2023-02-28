
print('Bem vindo a AluCar!\nSua locadora'
      ' de carros preferida!')

# Dados de entrada
nome = input('Qual seu nome? ')
km = float(input('Informe a Kilometragem percorrida: '))
dias = float(input('Informe a quantidade de dias: '))

# Calculo
valor_a_pagar = 60 * dias + 0.15 * km

# Saida
print(f'\nNome do locatário: {nome}.')
print(f'Km percorrido: {km} Km.')
print(f'Dias alugado: {dias} dias.')
print(f'Valor a pagar: R$ {valor_a_pagar :.2f}.\n')
print('Obrigado por utilizar a AluCar!\nVolte sempre!\n')
