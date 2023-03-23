
print('\033[33mPrograma para informar se um número é \033[1mPAR\033[m \033[33mou \033[1mÍMPAR\033[m')

num = int(input('\033[32mDigite um número inteiro positivo: \033[m'))

if (num % 2) == 0:
    print(f'O número \033[1;32m{num}\033[m é \033[1;32mPAR!\033[m')
else:
    print(f'O número \033[1;31m{num}\033[m é \033[1;31mÍMPAR\033[m')
