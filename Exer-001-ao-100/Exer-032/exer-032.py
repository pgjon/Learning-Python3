
from datetime import date

print('\033[31m-+' * 7, end='-\n\033[m')
print('\033[33mANO BISSEXTO???\033[m')
print('\033[31m-+' * 7, end='-\n\033[m')

ano = int(
    input('Digite um ano qualquer ou \033[1;32m0\033[m para ano atual do sistema: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    ''' Se o ano divisível por 4 der resto 0 e ano divisível por 100 der resto diferente de 0 ou
    divisível por 400 der resto 0, o ano será bissexto.  '''
    print(f'O ano \033[32m{ano}\033[m é \033[32mBISSEXTO!\033[m')
else:
    print(
        f'O ano \033[32m{ano}\033[m \033[1;31mNÃO\033[m é \033[32mBISSEXTO!\033[m')
