''' Faça um algoritmo que leia o salário de um funcionário e mostre
    seu novo salário, com 15% de aumento.   '''

print('Seja bem vindo!\n'
      'Banco de cadastro para aumento salarial.')

nome = input('Informe seu nome: ')
empresa = input('Nome da empresa: ')
cargo = input('Ocupação: ')
sal = float(input('Salário atual: R$ '))

novo_sal = float(sal + sal * 0.15)

print('\nDados do funcionário:\n'
      f'Nome: {nome}\n'
      f'Empresa: {empresa}\n'
      f'Ocupação: {cargo}\n'
      f'Salário Atual: R$ {sal}\n\n'
      f'Parabéns {nome}! Você recebeu aumento de 15%.'
      f'\nSeu novo salário é: R$ {novo_sal :.2f}'
      )
